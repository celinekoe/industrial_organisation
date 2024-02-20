import numpy as np
import pandas as pd

import constants.industry as IndustryConstants
import constants.investor as InvestorConstants

# Fill

def fill_range(series, start_year, end_year):
    filled_index = pd.Index(range(start_year, end_year + 1))
    series = series.reindex(filled_index, fill_value=None)

    return series

# Count

def _get_grouped_count(df, group_col):
  return df.groupby(group_col).size()

def get_grouped_count_percent(df, group_col):
  grouped_count_percent = _get_grouped_count(df, group_col) \
    .groupby(level=0).apply(lambda x: x / float(x.sum()) * 100) \
    .reset_index(level=0, drop=True) \
    .unstack()
  return grouped_count_percent

def get_year_count(df, year_col, start_year=None, end_year=None):
  year_count = _get_grouped_count(df, [year_col])
  if start_year and end_year:
    year_count = fill_range(year_count, start_year, end_year)
  
  year_count_growth = get_growth(year_count)

  return year_count, year_count_growth

def get_grouped_year_count(df, year_col, group_col, rename_col_dict=None, start_year=None, end_year=None):
  grouped_year_count = _get_grouped_count(df, [year_col, group_col]) \
    .unstack() \
    .reset_index() \
    .set_index(year_col)
  if start_year and end_year:
    grouped_year_count = fill_range(grouped_year_count, start_year, end_year)

  grouped_year_count_growth = grouped_year_count.pct_change() * 100

  if rename_col_dict:
    grouped_year_count = grouped_year_count.rename(columns=rename_col_dict)
    grouped_year_count_growth = grouped_year_count_growth.rename(columns=rename_col_dict)

  return grouped_year_count, grouped_year_count_growth

def get_STEM_year_count(df, year_col, rename_col_dict=None):
  return get_grouped_year_count(df, year_col, IndustryConstants.STEM_label, rename_col_dict)

def get_public_funded_year_count(df, year_col, rename_col_dict=None, start_year=None, end_year=None):
  public_funded_year_count, public_funded_year_count_growth = \
    get_grouped_year_count(df, year_col,
                           InvestorConstants.public_funded_label, rename_col_dict,
                           start_year, end_year)

  return public_funded_year_count, public_funded_year_count_growth

# Sum

def get_grouped_sum(df, group_col, sum_col):
  return df.groupby(group_col)[sum_col].sum()

def get_grouped_sum_percent(df, group_col, sum_col):
  grouped_sum_percent = get_grouped_sum(df, group_col, sum_col) \
    .groupby(level=0).apply(lambda x: x / float(x.sum()) * 100) \
    .reset_index(level=0, drop=True) \
    .unstack()
  return grouped_sum_percent

def get_year_sum(df, year_col, sum_col, start_year=None, end_year=None):
  year_sum = get_grouped_sum(df, [year_col], sum_col)
  if start_year and end_year:
    year_count = fill_range(year_count, start_year, end_year)

  year_sum_growth = get_growth(year_sum)

  return year_sum, year_sum_growth

def get_grouped_year_percent(df, year_col, group_col, rename_col_dict=None):
  grouped_count_percent = get_grouped_count_percent(df, [year_col, group_col])
  
  if rename_col_dict:
    grouped_count_percent = grouped_count_percent.rename(columns=rename_col_dict)

  return grouped_count_percent

# Growth

def get_growth(series):
  growth = series.pct_change() * 100
  growth.replace([np.inf, -np.inf], None, inplace=True)
  
  return growth

# Percent

def get_STEM_public_year_percent(df, year_col, sum_col=None):
  if not sum_col:
    STEM_public_year_percent = get_grouped_count_percent(df, [year_col, IndustryConstants.STEM_label, InvestorConstants.public_funded_label]) 
  else:
    STEM_public_year_percent = get_grouped_sum_percent(df, [year_col, IndustryConstants.STEM_label, InvestorConstants.public_funded_label], sum_col) 

  STEM_public_year_percent = STEM_public_year_percent \
    .unstack() \
    .reset_index() \
    .set_index(year_col)

  return STEM_public_year_percent

def get_STEM_year_percent(firms, year_col, sum_col=None):
  if not sum_col:
    return get_grouped_count_percent(firms, [year_col, IndustryConstants.STEM_label])
  else:
    return get_grouped_sum_percent(firms, [year_col, IndustryConstants.STEM_label], sum_col)

def get_public_funded_year_percent(firms, year_col, sum_col=None):
  if not sum_col:
    return get_grouped_count_percent(firms, [year_col, InvestorConstants.public_funded_label])
  else:
    return get_grouped_sum_percent(firms, [year_col, InvestorConstants.public_funded_label], sum_col)

# Filter
def filter_industry_group(firms, industry_group):
  industry_group_firms = firms[firms['Tag Groups'].apply(lambda firm_industry_group: industry_group in firm_industry_group)]
  return industry_group_firms

def filter_industry(firms, industry):
  industry_firms = firms[firms['Tags'].apply(lambda firm_industry: industry in firm_industry)]
  return industry_firms

def filter_STEM(firms, STEM=True):
  return firms[firms[IndustryConstants.STEM_label].fillna(False) == STEM]

def filter_public_funded(firms, public=True):
  return firms[firms[InvestorConstants.public_funded_label].fillna(False) == public]

