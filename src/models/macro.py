import pandas as pd

import config as Config

class Macro:
  def __init__(self, real_gdp, fed_rate):
    range_index = pd.Index(range(Config.start_year, Config.end_year))

    self.real_gdp = real_gdp
    self.real_gdp = real_gdp.reindex(range_index)
    self.real_gdp_growth = real_gdp.pct_change() * 100

    self.fed_rate = fed_rate
    self.fed_rate = fed_rate.reindex(range_index)

    self.recessions = self.real_gdp_growth[self.real_gdp_growth < 0].index.tolist()
