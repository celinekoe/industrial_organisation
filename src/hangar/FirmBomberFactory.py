import constants.labels as Labels
import hangar.BomberFactory as BomberFactory

class FirmBomber(BomberFactory.Bomber):
  def __init__(self, firms=None, targets=None, target_col=None, return_after=None, refurb=None):
    super().__init__(targets, target_col, return_after)
    if refurb:
      self._refurbish(refurb)
    else:
      self.frame = 'Firms'
      self.year_col = Labels.firm_founded_year
      self.scout(firms)