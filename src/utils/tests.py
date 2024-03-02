from linearmodels.panel import PanelOLS

import config as Config

def _get_valid_loc(series):
  valid_loc = 0

  if series.isna().any():
    last_year_index = series.index[series.isna()].max()
    valid_loc = series.index.get_loc(last_year_index) + 1

  return valid_loc

def _get_valid_series(series):
  valid_index = _get_valid_loc(series)
  valid_series = series[valid_index:]

  return valid_series

def get_valid_map(map):
  # Get initial min length, including invalid values
  min_length = min(len(series) for series in map.values())
  for key, series in map.items():
    valid_series = _get_valid_series(series)
    if len(valid_series) < min_length:
      min_length = len(valid_series)

  print(min_length)

  # Get map with matching min length
  valid_map = {}
  indices = None
  for key, series in map.items():
    valid_series = _get_valid_series(series)
    valid_map[key] = series.tail(min_length)

    if indices is None:
      indices = valid_series.index

  return valid_map

def prep_panel(df, control=None, control_col=None):
  # Convert df to long data format for panel regression
  # Time column needs to be an int
  df[Config.time_exog_label] = df.index.astype('int')
  df = df.melt(id_vars=[Config.time_exog_label],
               var_name=Config.entity_exog_label,
               value_name='value') \
                .dropna().reset_index(drop=True)
  
  # Get rolling mean
  df['rolling_value'] = df['value'].rolling(window=Config.window_size).mean()

  # Panel regression requires multi-index with entity and time for entity and time effects
  df[Config.entity_label] = df[Config.entity_exog_label]
  df[Config.time_label] =  df[Config.time_exog_label]
  df.set_index([Config.entity_label, Config.time_label], inplace=True)

  # Normalise time column or constant coefficient will be silly
  df[Config.time_exog_norm_label] = df[Config.time_exog_label] - (Config.start_year + Config.window_size - 1) + 1

  # Add a constant to the regression
  df[Config.const_exog_label] = 1

  # Add control
  if control is not None:
    df[control_col] = df[Config.time_exog_label].map(control)
    df[control_col] = df[control_col].astype('float') 

  # print(df)
  return df

def panel(df, control_col=None, entities=False, rolling=True):
  # Specify panel regression model

  # Specify endog_col
  endog_col = None

  if rolling:
    endog_col = 'rolling_value'
  else:
    endog_col = 'value'

  endog_df = df[endog_col]

  if entities:
    exog_cols = [Config.const_exog_label, Config.time_exog_norm_label, Config.entity_exog_label]
    entity_effects = False
  else:
    exog_cols = [Config.const_exog_label, Config.time_exog_norm_label]
    entity_effects = True

  # Specify exog_cols
  if control_col:
    exog_cols = exog_cols + [control_col]

  exog_df =  df[exog_cols]

  model = PanelOLS(endog_df, exog_df, entity_effects=entity_effects)

  # Clustering assumes heterogeneity within entities but independence between entitites
  results = model.fit(cov_type='clustered', cluster_entity=True)
  print(f'results: {results}')

  return results