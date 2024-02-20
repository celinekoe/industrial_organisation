import constants.firm as FirmConstants
import constants.industry as IndustryConstants
import constants.investor as InvestorConstants
import constants.visual as VisualConstants

import utils.common as CommonUtils
import utils.dataframe as DataframeUtils

import visual.visualiser as Visualiser
import visual.firm as FirmVisuals

class Optics:
  def get_bubble_scale(year_count):
    max_count = year_count.max()
    current_count = max_count
    for year in range(VisualConstants.end_year, 0, -1):
      if year in year_count:
        current_count = year_count[year]
        break

    return current_count / max_count

class Hangar:
  def __init__(self):
    self.ig_bomber = None
    self.i_bomber = None
    self.f_bomber = None

  def ready_ig_bomber(self, firms):
    self.ig_bomber = IndustryGroupBomber(firms)

  def ready_i_bomber(self, firms):
    self.i_bomber = IndustryBomber(firms)

  # def ready_f_bomber(self, firms):
  #   self.f_bomber = FundingBomber(firms)

class IndustryGroupBomber:
  def __init__(self, firms):
    self.bubble_zones = []
    self.targets = []  

    self.industry_groups = self._get_mission()
    self.year_count_map = {}
    self.year_count_growth_map = {}
    self._scout(firms)

  def _get_mission(self):
    return list(IndustryConstants.industry_group_industry_map.keys())
  
  def _scout(self, firms):
    for industry_group in self.industry_groups:
      industry_group_firms = DataframeUtils.filter_industry_group(firms, industry_group)
      industry_group_year_count, industry_group_year_count_growth = \
        DataframeUtils.get_year_count(
          industry_group_firms, FirmConstants.year_label,
          VisualConstants.start_year, VisualConstants.end_year
        )
      self.year_count_map[industry_group] = industry_group_year_count
      self.year_count_growth_map[industry_group] = industry_group_year_count_growth

      industry_group_max_count = industry_group_year_count.max()
      if industry_group_max_count > VisualConstants.bubble_min_size and \
        VisualConstants.bubble_scale > Optics.get_bubble_scale(industry_group_year_count):
          self.bubble_zones.append(industry_group)

  def identify_targets(self, macro):
    for industry_group in self.industry_groups:
      signal = macro.regression_bomb(
        self.year_count_growth_map[industry_group]
      )
      if signal:
        self.targets.append(industry_group)

  def bomb_targets(self, macro):
    for industry_group in self.targets:
      FirmVisuals.plot_year_count(self.year_count_map[industry_group], macro, industry_group)
      FirmVisuals.plot_year_count_growth(self.year_count_growth_map[industry_group], macro, industry_group)

      macro.regression(
        self.year_count_growth_map[industry_group],
        'Growth %',
        industry_group
      )

class IndustryBomber:
  def __init__(self, firms):
    self.bubble_zones = []
    self.targets = []  

    self.industries = self._get_mission()
    self.year_count_map = {}
    self.year_count_growth_map = {}
    self._scout(firms)

  def _get_mission(self):
    industries = [industry for industry_group_industries in IndustryConstants.industry_group_industry_map.values() for industry in industry_group_industries]
    industries = list(set(industries))
    return sorted(industries)
  
  def _scout(self, firms):
    for industry in self.industries:
      industry_firms = DataframeUtils.filter_industry(firms, industry)
      industry_year_count, industry_year_count_growth = \
        DataframeUtils.get_year_count(
          industry_firms, FirmConstants.year_label,
          VisualConstants.start_year, VisualConstants.end_year
        )
      self.year_count_map[industry] = industry_year_count
      self.year_count_growth_map[industry] = industry_year_count_growth

      industry_max_count = industry_year_count.max()
      if industry_max_count > VisualConstants.bubble_min_size and \
        VisualConstants.bubble_scale > Optics.get_bubble_scale(industry_year_count):
          self.bubble_zones.append(industry)

  def identify_targets(self, macro):
    print(self.year_count_growth_map)

    for industry in self.industries:
      print(industry)
      print(self.year_count_growth_map[industry].head(5))
      # signal = macro.regression_bomb(
      #   self.year_count_growth_map[industry]
      # )
      # if signal:
      #   self.targets.append(industry)

  def bomb_targets(self, macro):
    for industry in self.targets:
      FirmVisuals.plot_year_count(self.year_count_map[industry], macro, industry)
      FirmVisuals.plot_year_count_growth(self.year_count_growth_map[industry], macro, industry)

      macro.regression(
        self.year_count_growth[industry],
        'Growth %',
        industry
      )

def get_industry_group_industries(industry_group):
  return IndustryConstants.industry_group_industry_map[industry_group]

def visualise_bubble(industry_firms, industry, industry_year_count, fed_rate):
  industry_public_year_count = DataframeUtils.get_public_year_count(industry_firms)
  
  industry_bubble = {
    'All': industry_year_count,
    'Private Funded': industry_public_year_count[InvestorConstants.private_funded_label],
    'Public Funded': industry_public_year_count[InvestorConstants.public_funded_label],
    'Interest Rate': fed_rate,
  }

  Visualiser.plot_dict(industry_bubble, f"Bubble: {industry}", '')