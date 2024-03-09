import constants.labels as Labels
import utils.dataframe as dfUtils

import hangar.BomberFactory as BomberFactory

class FirmBomber(BomberFactory.Bomber):
  def __init__(self, firms=None, targets=None, target_col=None, return_after=None, refurb=None):
    super().__init__(targets, target_col, return_after)

    if refurb:
      self._refurbish(refurb)
    else:
      self.frame = Labels.firm_frame
      self.year_col = Labels.firm_founded_year

      self.year_exit_col = Labels.firm_exit_year
      self.year_exit = None
      self.year_exit_growth = None
      
      self.year_closed_col = Labels.firm_closed_year
      self.year_closed = None
      self.year_closed_growth = None

      self.scout(firms)
      self._scout_failed(firms)

  def _scout_failed(self, df):
    self.year_exit, self.year_exit_growth = dfUtils.get_year_count(df, self.year_exit_col)
    self.year_closed, self.year_closed_growth = dfUtils.get_year_count(df, self.year_closed_col)

