import pandas as pd
import whois

import constants.firm as FirmConstants
import constants.industry as IndustryConstants
import constants.investor as InvestorConstants

import utils.date as DateUtils
import utils.location as LocationUtils
import utils.common as CommonUtils

def enrich_firms(firms):
  firms['Country'] =  firms['Headquarters Location'].apply(LocationUtils.get_country)

  firms = DateUtils.set_year(firms, FirmConstants.founded_date_label, FirmConstants.year_label)

  firms[IndustryConstants.industry_label] =  firms[IndustryConstants.industry_label].apply(CommonUtils.string_to_list)
  firms[IndustryConstants.industry_group_label] =  firms[IndustryConstants.industry_group_label].apply(CommonUtils.string_to_list)
  firms[IndustryConstants.STEM_label] = firms[IndustryConstants.industry_label].apply(lambda industries: any(industry in IndustryConstants.STEM_industries for industry in industries))

  return firms

def get_domain_created_year(url):
  domain_created_year = None

  if url and url != 'nan':
    try:
      domain = whois.whois(url)

      creation_date = domain.creation_date
      if isinstance(creation_date, list):
        creation_date = creation_date[0]

      creation_date = pd.to_datetime(creation_date, errors='coerce')
      if creation_date is not None:
        print(f"success: {url}")
        domain_created_year = creation_date.year
    except Exception as e:
      print(f"error: {url}")

  return domain_created_year

def get_domain_created_year_from_map(url, url_map):
  return url_map.get(url)

def enrich_founded_year(firms, domain_created_year):
  firms['Domain Created Year'] =  firms['Website'].apply(get_domain_created_year_from_map, args=(domain_created_year,))
  firms['Founded Year'].fillna(firms['Domain Created Year'], inplace=True)
  return firms

def get_public_funded(top_investors, public_funded_investors):
  if isinstance(top_investors, str):
    top_investors = CommonUtils.string_to_list(top_investors)
    for top_investor in top_investors:
      if top_investor in public_funded_investors:
        return True
  
  return False

def enrich_public_funded(firms, public_funded_investors):
  firms[InvestorConstants.public_funded_label] = firms['Top 5 Investors'].apply(get_public_funded, args=(public_funded_investors,))
  return firms

def filter_for_profit(firms, for_profit=True):
  firms = firms[firms['Company Type'] == 'For Profit']
  return firms

def filter_founded_year(firms, start_year, end_year):
  firms = firms[pd.notna(firms['Founded Year'])]
  firms = firms[firms['Founded Year'] >= start_year]
  firms = firms[firms['Founded Year'] < end_year]
  return firms
