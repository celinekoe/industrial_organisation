import constants.firm as FirmConstants
import constants.industry as IndustryConstants
import constants.investor as InvestorConstants

import utils.dataframe as DataUtils
import visual.visualiser as Visualiser

class Industry:
  def __init__(self):
    self.industry_groups = self.get_industry_groups()

  def get_industry_groups():
    return list(IndustryConstants.industry_group_industry_map.keys())

def get_industry_group_industries(industry_group):
  return IndustryConstants.industry_group_industry_map[industry_group]

def get_industries():
  industries = [industry for industry_group_industries in IndustryConstants.industry_group_industry_map.values() for industry in industry_group_industries]
  industries = list(set(industries))
  return sorted(industries)

def visualise_bubble(industry_firms, industry, industry_year_count, fed_rate):
  industry_public_year_count = DataUtils.get_public_year_count(industry_firms)
  
  industry_bubble = {
    'All': industry_year_count,
    'Private Funded': industry_public_year_count[InvestorConstants.private_funded_label],
    'Public Funded': industry_public_year_count[InvestorConstants.public_funded_label],
    'Interest Rate': fed_rate,
  }

  Visualiser.plot_dict(industry_bubble, f"Bubble: {industry}", '')

def visualise_industry(firms, industry, fed_rate, end_year, bubble_params):
  industry_firms = DataUtils.filter_industry(firms, industry)
  industry_year_count = DataUtils.get_year_count(industry_firms, FirmConstants.year_label)
  
  industry_max_count = industry_year_count.max()
  industry_current_count = industry_max_count
  for year in range(args['end_year'], 0, -1):
    if year in industry_year_count:
      industry_current_count = industry_year_count[year]
      break
  industry_bubble_scale = industry_current_count / industry_max_count

  if industry_max_count > args['bubble_min_count'] and args['bubble_scale'] > industry_bubble_scale:
    visualise_bubble(industry_firms, industry, industry_year_count, fed_rate)

def visualise_industry_group(firms, industry_group, fed_rate):
  industry_group_firms = DataUtils.filter_industry_group(firms, industry_group)

  industry_group_year_count = DataUtils.get_year_count(industry_group_firms, FirmConstants.year_label)
  industry_group_public_year_count = DataUtils.get_public_year_count(industry_group_firms)
  industry_group_public_year_percent = DataUtils.get_public_funded_year_percent(industry_group_firms)

  Visualiser.plot(industry_group_year_count, f"{industry_group}: Firms Founded", 'Count')
  Visualiser.plot_dict(industry_group_public_year_count, f"{industry_group}: Firms Founded", 'Log Count', public_funded_colors)
  Visualiser.stack(industry_group_public_year_percent, f"{industry_group}: Public Funded Firms (Percent)", public_funded_stack_labels, colors=public_funded_colors)

  industry_group_industries = DataUtils.get_industry_group_industries(industry_group)
  for industry in industry_group_industries:
    visualise_industry(firms, industry, fed_rate)