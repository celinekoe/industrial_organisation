import constants.labels as Labels
import hangar.BomberFactory as BomberFactory

class FundBomber(BomberFactory.Bomber):
  def __init__(self, funds=None, targets=None, target_col=None, return_after=None, refurb=None):
    super().__init__(targets, target_col, return_after)
    if refurb:
      self._refurbish(refurb)
    else:
      self.frame = 'Funds'
      self.year_col = Labels.fund_announced_year
      self.scout(funds)
