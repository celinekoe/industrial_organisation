import constants.labels as Labels
import hangar.BomberFactory as BomberFactory

class FundBomber(BomberFactory.Bomber):
  def __init__(self, funds=None, targets=None, target_col=None, return_after=None, refurb=None):
    super().__init__(targets, target_col, return_after)
    if refurb:
      self._refurbish(refurb)
    else:
      self.frame = Labels.fund_frame
      self.year_col = Labels.fund_announced_year
      self.month_col = Labels.fund_announced_month
      self.scout(funds)
