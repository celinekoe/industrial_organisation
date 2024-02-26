import pandas as pd

import constants.config as Config
import constants.visual as VisualConstants

import visual.visualiser as Visualiser

class Macro:
  def __init__(self, real_gdp, fed_rate):
    range_index = pd.Index(range(Config.start_year, Config.end_year))

    self.real_gdp = real_gdp
    self.real_gdp = real_gdp.reindex(range_index)
    self.real_gdp_growth = real_gdp.pct_change() * 100

    self.fed_rate = fed_rate
    self.fed_rate = fed_rate.reindex(range_index)

    self.recessions = self.real_gdp_growth[self.real_gdp_growth < 0].index.tolist()

  def _get_first_valid_index(self, series):
    first_valid_index = series.first_valid_index()
    return series.index.get_loc(first_valid_index)

  def plot(self):
    Visualiser.plot(self.real_gdp, 'Real GDP 2014p', 'USD mn')
    Visualiser.plot(self.real_gdp_growth, 'Real GDP Growth 2014p', '%')
    Visualiser.plot(self.fed_rate, 'Interest Rate', '% pa')

  def plot_macro(self, series, series_label):
    series_macro_map = {
      series_label: series,
      'Fed Rate': self.fed_rate
    }
    Visualiser.plot_dict(series_macro_map, log_scale=False, colors=VisualConstants.STEM_colors, highlight=self.recessions)

  def regression(self, series, series_label, group_label):
    valid_index = self._get_first_valid_index(series)

    series_fed_rate = [series[valid_index:], self.fed_rate[valid_index:]]
    series_fed_rate_label = [series_label, 'Interest Rate']
    Visualiser.regression(series_fed_rate, series_fed_rate_label, group_label)

  def regression_bomb(self, series, series_label):
    signal = False
    try:
      valid_index = self._get_first_valid_index(series)
      series_fed_rate = [series[valid_index:], self.fed_rate[valid_index:]]
      signal = Visualiser.regression_bomb(series_fed_rate)
    except Exception as e:
      print(f'bomb failed for {series_label} with error: ', e)

    return signal
