
import constants.config as Config
import constants.firm as FirmConstants
import constants.industry as IndustryConstants
import constants.investor as InvestorConstants
import constants.visual as VisualConstants

import utils.common as CommonUtils
import utils.dataframe as dfUtils
import visual.visualiser as Visualiser

# All

def plot(firms, macro, industry=None):
  firm_year_count, firm_year_count_growth = \
    dfUtils.get_year_count(firms, FirmConstants.year_label, Config.start_year, Config.end_year)

  Visualiser.plot(firm_year_count,
                  CommonUtils.prepend_string('Firm: Count', industry), 'Count',
                  highlight=macro.recessions)
  Visualiser.plot(firm_year_count_growth,
                  CommonUtils.prepend_string('Firm: Count: Growth', industry), 'Growth %',
                  highlight=macro.recessions)
  
def plot_macro(firms, macro, industry=None):
  firm_year_count, firm_year_count_growth = \
    dfUtils.get_year_count(firms, FirmConstants.year_label,
                                  Config.start_year, Config.end_year)
  
  macro.regression(
    firm_year_count_growth,
    'Growth %',
    industry
  )

def plot_year_count(year_count, macro, industry=None):
  Visualiser.plot(year_count,
                  CommonUtils.prepend_string('Firm: Count', industry), 'Count',
                  highlight=macro.recessions)
  
def plot_year_count_growth(year_count_growth, macro, industry=None):
  Visualiser.plot(year_count_growth,
                  CommonUtils.prepend_string('Firm: Count: Growth', industry), 'Growth %',
                  highlight=macro.recessions)

# STEM

def plot_STEM(firms, macro):
  STEM_year_count, STEM_year_count_growth = \
    dfUtils.get_STEM_year_count(firms,
                                      FirmConstants.year_label,
                                      {True: IndustryConstants.STEM_label, False: IndustryConstants.not_STEM_label},
                                      Config.start_year, Config.end_year)

  Visualiser.plot_dict(STEM_year_count_growth, log_scale=False, colors=VisualConstants.STEM_colors, highlight=macro.recessions)

def plot_STEM_macro(firms, macro):
  STEM_year_count, STEM_year_count_growth = \
    dfUtils.get_STEM_year_count(firms,
                                      FirmConstants.year_label,
                                      {True: IndustryConstants.STEM_label, False: IndustryConstants.not_STEM_label},
                                      Config.start_year, Config.end_year)

  macro.regression(
    STEM_year_count_growth[IndustryConstants.STEM_label],
    'Growth %'
  )
  macro.regression(
    STEM_year_count_growth[IndustryConstants.not_STEM_label],
    'Growth %'
  )

# Public Funded

def plot_public_funded(firms, macro, industry=None):
  public_funded_year_count, public_funded_year_count_growth = \
    dfUtils.get_public_funded_year_count(firms,
                                                FirmConstants.year_label,
                                                {True: InvestorConstants.public_funded_label, False: InvestorConstants.private_funded_label},
                                                Config.start_year, Config.end_year)
  Visualiser.plot_dict(
    public_funded_year_count_growth,
    CommonUtils.prepend_string('Public Funded', industry), 'Count',
    log_scale=False,
    colors=VisualConstants.public_funded_colors, highlight=macro.recessions
  )

def plot_public_funded_macro(firms, macro, industry=None):
  public_funded_year_count, public_funded_year_count_growth = \
    dfUtils.get_public_funded_year_count(firms,
                                                FirmConstants.year_label,
                                                {True: InvestorConstants.public_funded_label, False: InvestorConstants.private_funded_label},
                                                Config.start_year, Config.end_year)
  
  macro.regression(
    public_funded_year_count_growth[InvestorConstants.public_funded_label],
    'Growth %',
    CommonUtils.prepend_string('Public Funded', industry)
  )
  macro.regression(
    public_funded_year_count_growth[InvestorConstants.private_funded_label],
    'Growth %',
    CommonUtils.prepend_string('Private Funded', industry)
  )

# STEM and Public Funded

def stack_STEM_public_funded(firms):
  STEM_year_percent = dfUtils.get_STEM_year_percent(firms, FirmConstants.year_label)
  public_funded_year_percent = dfUtils.get_public_funded_year_percent(firms, FirmConstants.year_label)
  STEM_public_year_percent = dfUtils.get_STEM_public_year_percent(firms, FirmConstants.year_label)

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

# Industry Group

def plot_industry_group(firms, industry_group, macro):
  industry_group_firms = dfUtils.filter_industry_group(firms, industry_group)

  plot(industry_group_firms, macro, industry_group)
  # plot_macro(industry_group_firms, macro, industry_group)
  plot_public_funded(industry_group_firms, macro, industry_group)
  # plot_public_funded_macro(industry_group_firms, macro, industry_group)

def plot_industry(firms, industry, macro):
  industry_firms = dfUtils.filter_industry(firms, industry)

  plot(industry_firms, macro, industry)
  # plot_macro(industry_firms, macro, industry)
  plot_public_funded(industry_firms, macro, industry)
  # plot_public_funded_macro(industry_firms, macro, industry)


def plot_industry_group_industries(firms, industry_group, macro):
  industry_group_firms = dfUtils.filter_industry_group(firms, industry_group)
  print("TODO")