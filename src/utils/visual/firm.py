
import constants.firm as FirmConstants
import constants.industry as IndustryConstants
import constants.investor as InvestorConstants
import constants.visual as VisualConstants

import utils.dataframe as DataframeUtils
import utils.visual.visualiser as Visualiser

def _prepend_industry(title, industry):
  if industry:
    title = f'{industry} {title}'
  return title

def plot(firms, macro, industry=None):
  firm_year_count, firm_year_count_growth = \
    DataframeUtils.get_year_count(firms, FirmConstants.year_label, VisualConstants.start_year, VisualConstants.end_year)

  Visualiser.plot(firm_year_count,
                  _prepend_industry('Firm: Count', industry), 'Count',
                  highlight=macro.recessions)
  Visualiser.plot(firm_year_count_growth,
                  _prepend_industry('Firm: Count: Growth', industry),
                  'Count',
                  highlight=macro.recessions)

def plot_macro(firms, macro, industry=None):
  firm_year_count, firm_year_count_growth = \
    DataframeUtils.get_year_count(firms, FirmConstants.year_label, VisualConstants.start_year, VisualConstants.end_year)
  
  macro.regression(firm_year_count_growth,
                   _prepend_industry('Firm: Count: Growth', industry))

def plot_STEM(firms, macro):
  STEM_year_count, STEM_year_count_growth = \
    DataframeUtils.get_STEM_year_count(firms,
                                      FirmConstants.year_label,
                                      {True: IndustryConstants.STEM_label, False: IndustryConstants.not_STEM_label},
                                      VisualConstants.start_year, VisualConstants.end_year)

  Visualiser.plot_dict(STEM_year_count_growth, log_scale=False, colors=VisualConstants.STEM_colors, highlight=macro.recessions)

def plot_STEM_macro(firms, macro):
  STEM_year_count, STEM_year_count_growth = \
    DataframeUtils.get_STEM_year_count(firms,
                                      FirmConstants.year_label,
                                      {True: IndustryConstants.STEM_label, False: IndustryConstants.not_STEM_label},
                                      VisualConstants.start_year, VisualConstants.end_year)

  macro.regression(STEM_year_count_growth[IndustryConstants.STEM_label], 'STEM Firm: Count: Growth')
  macro.regression(STEM_year_count_growth[IndustryConstants.not_STEM_label], 'Not STEM Firm: Count: Growth')

def plot_public_funded(firms, macro):
  public_funded_year_count, public_funded_year_count_growth = \
    DataframeUtils.get_public_funded_year_count(firms,
                                                FirmConstants.year_label,
                                                {True: InvestorConstants.public_funded_label, False: InvestorConstants.private_funded_label},
                                                VisualConstants.start_year, VisualConstants.end_year)
  Visualiser.plot_dict(public_funded_year_count_growth, log_scale=False, colors=VisualConstants.public_funded_colors, highlight=macro.recessions)

def plot_public_funded_macro(firms, macro):
  public_funded_year_count, public_funded_year_count_growth = \
    DataframeUtils.get_public_funded_year_count(firms,
                                                FirmConstants.year_label,
                                                {True: InvestorConstants.public_funded_label, False: InvestorConstants.private_funded_label},
                                                VisualConstants.start_year, VisualConstants.end_year)

  macro.regression(public_funded_year_count_growth[InvestorConstants.public_funded_label], 'Public Funded Firm: Count: Growth')
  macro.regression(public_funded_year_count_growth[InvestorConstants.private_funded_label], 'Private Funded Firm: Count: Growth')
  
def stack_STEM_public_funded(firms):
  STEM_year_percent = DataframeUtils.get_STEM_year_percent(firms, FirmConstants.year_label)
  public_funded_year_percent = DataframeUtils.get_public_funded_year_percent(firms, FirmConstants.year_label)
  STEM_public_year_percent = DataframeUtils.get_STEM_public_year_percent(firms, FirmConstants.year_label)

  Visualiser.stack(STEM_year_percent,
                  'STEM Firms: Count: Percent', '%',
                  VisualConstants.STEM_stack_labels,
                  colors=VisualConstants.STEM_colors)
  Visualiser.stack(public_funded_year_percent,
                  'Public Funded Firms: Count: Percent', '%',
                  VisualConstants.public_funded_stack_labels,
                  colors=VisualConstants.public_funded_colors)
  Visualiser.stack(STEM_public_year_percent,
                  'STEM Public Funded Firms: Count: Percent', '%',
                  ['Not STEM Private Funded', 'STEM Private Funded', 'Not STEM Public Funded', 'STEM Public Funded'],
                  colors=VisualConstants.STEM_public_year_percent_colors)

def plot_industry_group(firms, industry_group, macro):
  industry_group_firms = DataframeUtils.filter_industry_group(firms, industry_group)
  filtered_rows = industry_group_firms[industry_group_firms['Founded Year'] == 2019]

  # plot(industry_group_firms, macro)
  plot_macro(industry_group_firms, macro)
  # plot_public_funded(industry_group_firms, macro)
  # plot_public_funded_macro(industry_group_firms, macro)

  # industry_group_year_count = DataframeUtils.get_year_count(industry_group_firms, FirmConstants.year_label)
  # industry_group_public_year_count = DataframeUtils.get_public_year_count(industry_group_firms)
  # industry_group_public_year_percent = DataframeUtils.get_public_funded_year_percent(industry_group_firms)

  # Visualiser.plot(industry_group_year_count, f"{industry_group}: Firms Founded", 'Count')
  # Visualiser.plot_dict(industry_group_public_year_count, f"{industry_group}: Firms Founded", 'Log Count', public_funded_colors)
  # Visualiser.stack(industry_group_public_year_percent, f"{industry_group}: Public Funded Firms (Percent)", public_funded_stack_labels, colors=public_funded_colors)

  # industry_group_industries = DataframeUtils.get_industry_group_industries(industry_group)
  # for industry in industry_group_industries:
  #   visualise_industry(firms, industry, fed_rate)