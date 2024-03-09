
import config as Config
import utils.dataframe as dfUtils

class Bomber():
  def __init__(self, targets, target_col, return_after):
    self.frame = ''
    self.year_col = None
    self.targets = targets
    self.target_col = target_col
    self.return_after = return_after

    self.i_map = {}
    self.year_count = None
    self.year_growth = None
    self.year_volatility = None

    self.year_count_map = {}
    self.year_growth_map = {}
    self.year_beta_map = {}

  def _refurbish(self, refurb):
    props = [attr for attr in dir(refurb) if not attr.startswith('__') and not callable(getattr(refurb, attr))]
    for prop in props:
      setattr(self, prop, getattr(refurb, prop))

  def scout(self, df):
    self.year_count, self.year_growth = dfUtils.get_year_count(df, self.year_col)
    self.year_volatility = self.year_growth.rolling(window=Config.window_size).std()

    for idx, i in enumerate(self.targets):
      if self.return_after and idx > self.return_after:
        break

      self.i_map[i] = dfUtils.filter(df, i, self.target_col)
      self.year_count_map[i], self.year_growth_map[i] = dfUtils.get_year_count(self.i_map[i], self.year_col)
      self.year_beta_map[i] = self.year_growth_map[i].rolling(window=Config.window_size).std()