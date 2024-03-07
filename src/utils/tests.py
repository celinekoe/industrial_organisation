from linearmodels.panel import PanelOLS

import config as Config

def prep_panel(df, control=None, control_col=None):
  # Convert df to long data format for panel regression
  # Time column needs to be an int
  df[Config.time_exog_label] = df.index.astype('int')
  df = df.melt(id_vars=[Config.time_exog_label],
               var_name=Config.entity_exog_label,
               value_name='value') \
                .dropna().reset_index(drop=True)

  # Panel regression requires multi-index with entity and time for entity and time effects
  df[Config.entity_label] = df[Config.entity_exog_label]
  df[Config.time_label] =  df[Config.time_exog_label]
  df.set_index([Config.entity_label, Config.time_label], inplace=True)

  # Normalise time column or constant coefficient will be silly
  df[Config.time_exog_norm_label] = df[Config.time_exog_label] - (Config.start_year)

  # Add a constant to the regression
  df[Config.const_exog_label] = 1

  # Add control
  if control is not None:
    df[control_col] = df[Config.time_exog_label].map(control)
    df[control_col] = df[control_col].astype('float') 

  # print(df)
  return df

def panel(df, control_col=None):
  # Specify panel regression model

  # Specify endog_col
  endog_col = 'value'
  endog_df = df[endog_col]

  # exog_cols = [Config.const_exog_label, Config.time_exog_norm_label, Config.entity_exog_label]
  exog_cols = [Config.const_exog_label, Config.time_exog_norm_label]

  # Specify exog_cols
  if control_col is not None:
    exog_cols = exog_cols + [control_col]

  exog_df =  df[exog_cols]

  model = PanelOLS(endog_df, exog_df, entity_effects=True)

  # Clustering assumes heterogeneity within entities but independence between entitites
  results = model.fit(cov_type='clustered', cluster_entity=True)
  print(f'results: {results}')

  coefficients = results.params
  # print(coefficients.year_norm)

  sorted_coefficients = coefficients.reindex(coefficients.abs().sort_values(ascending=False).index)
  print(sorted_coefficients)

  return results