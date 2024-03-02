import pandas as pd

import constants.labels as Labels
import constants.industry as IndustryConstants

import utils.date as DateUtils
import utils.datatype as dtUtils
import utils.location as LocationUtils

def enrich_industry_group(industries, industry_industry_group_map):
  industry_groups = []
  for industry in industries:
    if industry in industry_industry_group_map:
      industry_groups.extend(industry_industry_group_map[industry])
  return list(set(industry_groups))

def enrich(funding):
  funding[Labels.country] = funding[Labels.fund_location].apply(LocationUtils.get_country)

  funding[Labels.industries] =  funding[Labels.fund_industries].apply(dtUtils.string_to_list)

  industry_industry_group_map = dtUtils.flip_list_dict(IndustryConstants.industry_group_industry_map)
  funding[Labels.industry_groups] =  funding[Labels.industries].apply(enrich_industry_group, args=(industry_industry_group_map,))
  funding[Labels.STEM] = funding[Labels.industries].apply(lambda industries: any(industry in IndustryConstants.STEM_industries for industry in industries))

  funding = DateUtils.set_year(funding, Labels.fund_announced_date, Labels.fund_announced_year)

  return funding

def get_public_funded(investors, public_funded_investors):
  if isinstance(investors, str):
    investors = dtUtils.string_to_list(investors)
    for investor in investors:
      if investor in public_funded_investors:
        return True
  
  return False

def enrich_public_funded(funding, public_funded_investors):
  funding[Labels.public_funded] = funding[Labels.fund_investors].apply(get_public_funded, args=(public_funded_investors, ))
  return funding

def filter_announced_year(funding, start_year, end_year):
  funding = funding[pd.notna(funding[Labels.fund_announced_year])]
  funding = funding[funding[Labels.fund_announced_year] >= start_year]
  funding = funding[funding[Labels.fund_announced_year] < end_year]

  return funding
