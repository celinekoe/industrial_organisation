import visual.visualiser as Visualiser

class Macro:
  def __init__(self, real_gdp, fed_rate):
    self.real_gdp = real_gdp
    self.real_gdp_growth = real_gdp.pct_change() * 100
    self.fed_rate = fed_rate
    self.recessions = self.real_gdp_growth[self.real_gdp_growth < 0].index.tolist()

  def _get_first_valid_index(self, series):
    invalid_indices = series.index[(series.isnull()) | (series == 0)]
    last_invalid_index = invalid_indices[-1]
    first_valid_index = last_invalid_index + 1

    return series.index.get_loc(first_valid_index)

  def plot(self):
    Visualiser.plot(self.real_gdp, 'Real GDP 2014p', 'USD mn')
    Visualiser.plot(self.real_gdp_growth, 'Real GDP Growth 2014p', '%')
    Visualiser.plot(self.fed_rate, 'Interest Rate', '% pa')

  def regression(self, series, series_label, group_label):
    valid_index = self._get_first_valid_index(series)

    series_fed_rate = [series[valid_index:], self.fed_rate[valid_index:]]
    series_fed_rate_label = [series_label, 'Interest Rate']

    Visualiser.regression(series_fed_rate, series_fed_rate_label, group_label)
