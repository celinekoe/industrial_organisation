import pandas as pd
import whois

import constants.labels as Labels
import constants.industry as IndustryConstants

import utils.date as DateUtils
import utils.datatype as dtUtils
import utils.location as LocationUtils

def enrich_firms(firms):
  firms[Labels.country] =  firms[Labels.firm_location].apply(LocationUtils.get_country)

  firms = DateUtils.set_year(firms, Labels.firm_founded_date, Labels.firm_founded_year)
  firms = DateUtils.set_year(firms, Labels.firm_exit_date, Labels.firm_exit_year)
  firms = DateUtils.set_year(firms, Labels.firm_closed_date, Labels.firm_closed_year)

  firms[Labels.industries] =  firms[Labels.industries].apply(dtUtils.string_to_list)
  firms[Labels.industry_groups] =  firms[Labels.industry_groups].apply(dtUtils.string_to_list)
  firms[Labels.STEM] = firms[Labels.industries].apply(lambda industries: any(industry in IndustryConstants.STEM_industries for industry in industries))

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
  firms[Labels.firm_domain_created_year] =  firms[Labels.firm_website].apply(get_domain_created_year_from_map, args=(domain_created_year,))
  firms[Labels.firm_founded_year].fillna(firms[Labels.firm_domain_created_year], inplace=True)
  return firms

def get_public_funded(top_investors, public_funded_investors):
  if isinstance(top_investors, str):
    top_investors = dtUtils.string_to_list(top_investors)
    for top_investor in top_investors:
      if top_investor in public_funded_investors:
        return True
  
  return False

def enrich_public_funded(firms, public_funded_investors):
  firms[Labels.public_funded] = firms[Labels.firm_top_investors].apply(get_public_funded, args=(public_funded_investors,))
  return firms

def filter_for_profit(firms):
  firms = firms[firms[Labels.firm_type] == 'For Profit']
  return firms

def filter_founded_year(firms, start_year, end_year):
  firms = firms[pd.notna(firms[Labels.firm_founded_year])]
  firms = firms[firms[Labels.firm_founded_year] >= start_year]
  firms = firms[firms[Labels.firm_founded_year] < end_year]
  return firms
