
import hangar.ScoutModule as ScoutModule

class Bomber(ScoutModule.Scouter):
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
    self.year_count_growth_map = {}
    self.year_count_growth_beta_map = {}

  def _refurbish(self, refurb):
    props = [attr for attr in dir(refurb) if not attr.startswith('__') and not callable(getattr(refurb, attr))]
    for prop in props:
      setattr(self, prop, getattr(refurb, prop))

  def scout(self, df):
    super().scout(df)

  def report(self):
    return self.year_count_growth_beta_map