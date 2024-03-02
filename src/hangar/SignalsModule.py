import numpy as np

import config as Config
import utils.tests as tests
import utils.dataframe as dfUtils

class Signals():
  def __init__():
    pass

  def _identify_rolling(self, series, i):
    rolling_year = []
    rolling_coef = []

    rolling_subsets = tests.get_rolling_subsets(series)
    
    for idx, subset in enumerate(rolling_subsets):
      ar_coef, ar_coef_p = tests.ar(subset)
      rolling_year.append(subset.index[0])
      rolling_coef.append(ar_coef)

    self.rolling_coef_map[i] = dfUtils.list_to_series(rolling_year, rolling_coef)

  def _identify_one(self, i):
    max_count = self.year_count_map[i].max()
    min_count = Config.min_count

    try:
      if max_count > min_count:
        self._identify_rolling(self.year_count_share_map[i], i)
      
    except Exception as e:
      print(f'identify failed for {i} with error: ', e)

  def _identify_trend(self):
    year_coefs = []
    for year in Config.year_range:
      coefs = []
      for i, rolling_coef in self.rolling_coef_map.items():
        coef = rolling_coef[year]
        if not np.isnan(coef):
          coefs.append(coef)

      if len(coefs) > 0 and len(coefs) > Config.min_industries:
        mean_coef = sum(coefs) / len(coefs)
        year_coefs.append(mean_coef)
      else:
        year_coefs.append(None)

    self.trend = dfUtils.list_to_series(Config.year_range, year_coefs)

  def identify(self):
    for idx, i in enumerate(self.targets):
      if self.return_after and idx > self.return_after:
        break

      self._identify_one(i)

    self._identify_trend()