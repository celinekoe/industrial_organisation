import hangar.Frame as Frame

import constants.firm as FirmConstants
import constants.fund as FundConstants

class FirmBomber(Frame.Bomber):
  def __init__(self, firms=None, macro=None, return_after=None, refurb=None):
    super().__init__(macro)
    if refurb:
      self._refurbish(refurb)
    else:
      self.frame = 'Firm'
      self.scout(firms, return_after)

  def scout(self, firms, return_after=None):
    super().scout(firms, FirmConstants.year_label, return_after)

  def identify(self, return_after=None):
    super().identify(return_after)
  
  def report(self):
    super().report()

class FundBomber(Frame.Bomber):
  def __init__(self, funds=None, macro=None, return_after=None, refurb=None):
    super().__init__(macro)
    if refurb:
      self._refurbish(refurb)
    else:
      self.frame = 'Fund'
      self.scout(funds, return_after)

  def scout(self, funds, return_after=None):
    super().scout(funds, FundConstants.year_label, return_after)

  def identify(self, return_after=None):
    super().identify(return_after)
  
  def report(self):
    super().report()
