import statsmodels.tsa.stattools as stattools 
import statsmodels.tsa.ar_model as ar_model
import warnings

import constants.config as Config
import matplotlib.pyplot as plt

import utils.dataframe as dfUtils

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

def accept_null(p):
  accept = False
  if p:
    accept = p > Config.p_accept_threshold

  return accept

def reject_null(p):
  reject = False
  if p:
    reject = p < Config.p_reject_threshold

  return reject

def get_rolling_subsets(series):
  valid_series = _get_valid_series(series)

  rolling_subsets = []
  valid_series_length = len(valid_series)
  for i in range(valid_series_length - Config.window_size + 1):
    subset = valid_series[i:i + Config.window_size]
    rolling_subsets.append(subset)

  return rolling_subsets

def explosion(growth_series):
  explosion = False

  max_growth = growth_series.max() / 100
  if max_growth > Config.growth_threshold:
      explosion = True

  return explosion

def adf(series):
  valid_series = _get_valid_series(series)

  result = stattools.adfuller(valid_series, autolag='AIC')
  p_value = result[1]
  lags = result[2]

  return p_value, lags

def kpss(series):
  valid_series = _get_valid_series(series)

  warnings.filterwarnings("ignore", category=UserWarning)
  kpss_stat, p_value, lags, critical_values = stattools.kpss(valid_series)

  return p_value, lags

def ar(series, i, lags=1):
  valid_series = _get_valid_series(series)
  # AutoReg doesn't work with year index
  valid_series.reset_index(drop=True, inplace=True)

  model = ar_model.AutoReg(valid_series, lags=lags)
  result = model.fit()

  beta = result.params[1]
  p_value = result.pvalues[1]
  
  return beta, p_value