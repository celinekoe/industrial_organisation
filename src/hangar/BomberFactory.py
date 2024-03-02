
import hangar.DisplayModule as DisplayModule
import hangar.ScoutModule as ScoutModule
import hangar.SignalsModule as SignalsModule

class Bomber(DisplayModule.Display, ScoutModule.Scouter, SignalsModule.Signals):
  def __init__(self, targets, target_col, return_after):
    self.frame = ''
    self.year_col = None
    self.targets = targets
    self.target_col = target_col
    self.return_after = return_after

    self.i_map = {}
    self.year_count = None
    self.year_count_growth = None
    self.year_count_growth_beta = None

    self.year_count_map = {}
    self.year_count_beta_map = {}
    self.year_count_growth_map = {}
    self.year_count_growth_lagged_map = {}
    self.year_count_growth_beta_map = {}
    self.year_count_share_map = {}
    self.year_count_share_beta_map = {}
    self.year_count_share_growth_map = {}
    self.year_count_share_growth_beta_map = {}

    self.rolling_coef_map = {}
    self.trend = None

  def _refurbish(self, refurb):
    props = [attr for attr in dir(refurb) if not attr.startswith('__') and not callable(getattr(refurb, attr))]
    for prop in props:
      setattr(self, prop, getattr(refurb, prop))

  def scout(self, df):
    super().scout(df)

  def identify(self):
    super().identify()

  def report(self, macro):
    super().report(macro)

  def detailed_report(self, macro):
    super().detailed_report(macro)

  def sample(self, i, macro, detailed=False):
    super().sample(i, macro, detailed)