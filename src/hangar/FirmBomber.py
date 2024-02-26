import constants.config as Config

import constants.config as Config
import constants.firm as FirmConstants

import hangar.Navigation as Navigation
import hangar.Optics as Optics

import utils.dataframe as dfUtils

class FirmBomber:
  def __init__(self):
    self.identified = False
    self.crashes = []
    self.explosions = []
    self.walks = []

    self.industry_groups = Navigation.get_industry_groups()
    self.industries = Navigation.get_industries()

    self.ig_map = {}
    self.i_map = {}
    self.year_count_map = {}
    self.year_count_growth_map = {}

  def _refurbish(self, refurb):
    self.identified = refurb.identified
    self.crashes = refurb.crashes
    self.explosions = refurb.explosions
    self.walks = refurb.walks

    self.industry_groups = refurb.industry_groups
    self.industries = refurb.industries

    self.ig_map = refurb.ig_map
    self.i_map = refurb.i_map
    self.year_count_map = refurb.year_count_map
    self.year_count_growth_map = refurb.year_count_growth_map

  def _scout_one(self, firms):
    year_count, year_count_growth = \
      dfUtils.get_year_count(
        firms, FirmConstants.year_label,
        Config.start_year, Config.end_year
      )
    
    return year_count, year_count_growth

  def _identify_one(self, value_series, growth_series, label):
    max_value = value_series.max()

    crash = False
    explosion = False
    null = False

    try:
      if max_value > Config.count_threshold:
        crash = Optics.crash(value_series)
        explosion = Optics.explosion(growth_series)
        p_value, lag, null = Optics.adf(growth_series)
        # null_any, null_subsets =  Optics.rolling_adf(ig_year_count_growth)

    except Exception as e:
      print(f'identify failed for {label} with error: ', e)

    return crash, explosion, null

  def reset_identify(self):
    self.identified = False
    self.crashes = []
    self.explosions = []
    self.walks = []