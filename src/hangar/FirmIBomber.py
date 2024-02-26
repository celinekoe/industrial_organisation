import utils.dataframe as dfUtils

from hangar.FirmBomber import FirmBomber

class FirmIBomber(FirmBomber):
  def __init__(self, firms=None, return_after=None, refurb=None):
    super().__init__()
    if refurb:
      self._refurbish(refurb)
    else:
      self._scout(firms, return_after)

  def _scout(self, firms, return_after):
    for idx, i in enumerate(self.industries):
      if return_after and idx > return_after:
        break

      i_firms = dfUtils.filter_industry(firms, i)
      i_year_count, i_year_count_growth = self._scout_one(i_firms)

      self.i_map[i] = i_firms
      self.year_count_map[i] = i_year_count
      self.year_count_growth_map[i] = i_year_count_growth

  def identify(self):
    if not self.identified:
      for i in self.industries:
        i_year_count = self.year_count_map[i]
        i_year_count_growth = self.year_count_growth_map[i]

        crash, explosion, walk = self._identify_one(i_year_count, i_year_count_growth, i)

        if crash:
          self.crashes.append(i)

        if explosion:
          self.explosions.append(i)

        if walk:
          self.walks.append(i)

      self.identified = True
    else:
      print('Already identified!')
  
  def reidentify(self):
    self.reset_identify()
    self.identify()

  def report(self):
    print(f'crashes: {len(self.crashes)}')
    print(self.crashes)
    print(f'explosions: {len(self.explosions)}')
    print(self.explosions)
    print(f'walks: {len(self.walks)}')
    print(self.walks)
    # for ig in self.industry_groups:
    #   ig_i = IndustryConstants.industry_group_industry_map[ig]
