import pandas as pd

import constants.firm as FirmConstants
import constants.funding as FundingConstants
import constants.investor as InvestorConstants
import constants.industry as IndustryConstants
import utils.common as CommonUtils
import utils.location as LocationUtils

def enrich_industry_group(industries, industry_industry_group_map):
  industry_groups = []
  for industry in industries:
    if industry in industry_industry_group_map:
      industry_groups.extend(industry_industry_group_map[industry])
  return list(set(industry_groups))

def enrich(funding):
  funding['Country'] =  funding['Organization Location'].apply(LocationUtils.get_country)

  funding[FirmConstants.industries_label] =  funding['Organization Industries'].apply(CommonUtils.string_to_list)

  industry_industry_group_map = CommonUtils.flip_list_dict(IndustryConstants.industry_group_industry_map)
  funding[FirmConstants.industry_groups_label] =  funding[FirmConstants.industries_label].apply(enrich_industry_group, args=(industry_industry_group_map,))
  funding[IndustryConstants.STEM_label] = funding[FirmConstants.industries_label].apply(lambda industries: any(industry in IndustryConstants.STEM_industries for industry in industries))

  funding['Investors'] = funding['Investor Names'].apply(CommonUtils.string_to_list)

  funding[FundingConstants.year_label] = funding[FundingConstants.date_label].astype(str).str[:4] # use this instead of datetime as there are pre-epoch date
  funding[FundingConstants.year_label] = pd.to_numeric(funding[FundingConstants.year_label], errors='coerce')

  return funding

def get_public_funded(investors, public_funded_investors):
  for investor in investors:
    if investor in public_funded_investors:
      return True
  
  return False

def enrich_public_funded(funding, public_funded_investors):
  funding[InvestorConstants.public_funded_label] = funding['Investors'].apply(get_public_funded, args=(public_funded_investors, ))
  return funding

def filter_announced_year(funding, start_year, end_year):
  funding = funding[pd.notna(funding[FundingConstants.year_label])]
  funding = funding[funding[FundingConstants.year_label] >= start_year]
  funding = funding[funding[FundingConstants.year_label] < end_year]

  return funding

def filter_currency(funding, currency):
  return funding[funding['Money Raised Currency'] == currency] 
