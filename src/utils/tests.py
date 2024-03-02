import statsmodels.tsa.ar_model as ar_model
import statsmodels.tsa.stattools as stattools 
import linearmodels.panel as panel
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

def _get_valid_map(map):
  # Get keys
  keys = list(map.keys())

  # Get initial min length, including invalid values
  min_length = min(len(series) for series in map.values())
  for key, series in map.items():
    valid_series = _get_valid_series(series)
    if len(valid_series) < min_length:
      min_length = len(valid_series)

  # Get map with matching min length
  valid_map = {}
  indices = None
  for key, series in map.items():
    valid_series = _get_valid_series(series)
    valid_map[key] = series.tail(min_length)

    if indices is None:
      indices = valid_series.index

  return valid_map, keys, indices

def get_rolling_subsets(series):
  valid_series = _get_valid_series(series)

  rolling_subsets = []
  valid_series_length = len(valid_series)
  for i in range(valid_series_length - Config.window_size + 1):
    subset = valid_series[i:i + Config.window_size]
    rolling_subsets.append(subset)

  return rolling_subsets

def adf(series):
  valid_series = _get_valid_series(series)

  result = stattools.adfuller(valid_series, autolag='AIC')
  p_value = result[1]
  lags = result[2]

  return p_value, lags

def ar(series):
  valid_series = _get_valid_series(series)
  # AutoReg doesn't work with year index
  valid_series.reset_index(drop=True, inplace=True)

  model = ar_model.AutoReg(valid_series, lags=Config.lag)
  result = model.fit()

  beta = result.params[1]
  p_value = result.pvalues[1]
  
  return beta, p_value

def panel(df, time_col, value_col):
  # Convert df to long data format for panel regression
  # Time column needs to be an int
  df[time_col] = df.index.astype('int')
  df = df.melt(id_vars=[time_col],
          var_name=value_col,
          value_name='value') \
            .dropna().reset_index(drop=True)
  
  # Exaggerate peaks with rolling mean
  df['rolling_value'] = df['value'].rolling(window=Config.window_size).mean()

  # Panel regression requires multi-index with entity and time for entity and time effects
  df['entity'] = df[value_col]
  df['time'] =  df[time_col]
  df.set_index(['entity', 'time'], inplace=True)

  # Add a constant to the regression
  df['const'] = 1

  # print(df)

  # Panel regression
  exog = df[['const', 'year']]
  model = panel.PanelOLS(df['rolling_value'], exog, entity_effects=True)

  # Clustering assumes heterogeneity within entities but independence between entitites
  results = model.fit(cov_type='clustered', cluster_entity=True)
  print(f'results: {results}')

  estimated_effects = results.estimated_effects
  entity_effects = estimated_effects.groupby(level=0).mean()

  # print(estimated_effects)
  # print(entity_effects)

  # time_effects = {}
  # for index in entity_effects.index:
  #     if index == spy_index:
  #       entity_estimated_effects = estimated_effects.loc[index]
  #       entity_effect = entity_effects.loc[index, 'estimated_effects']
  #       print(entity_estimated_effects)
  #       print(entity_effect)
  #       time_effect = entity_estimated_effects - entity_effect
  #       time_effects[index] = time_effect
  #       Visualiser.plot(time_effect)
