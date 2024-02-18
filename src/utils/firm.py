import pandas as pd
import whois

import utils.location as LocationUtils
import utils.string as StringUtils

def enrich_firms(firms):
  firms['Country'] =  firms['Headquarters Location'].apply(LocationUtils.get_country)
 
  firms['Founded Year'] = firms['Founded Date'].astype(str).str[:4] # use this instead of datetime as there are pre-epoch date
  firms['Founded Year'] = pd.to_numeric(firms['Founded Year'], errors='coerce')
 
  firms['Tags'] =  firms['Industries'].apply(StringUtils.string_to_list)
  firms['Tag Groups'] =  firms['Industry Groups'].apply(StringUtils.string_to_list)

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

def enrich_founded_year(firms, domain_created_year_map):
  firms['Domain Created Year'] =  firms['Website'].apply(get_domain_created_year_from_map, args=(domain_created_year_map,))
  firms['Founded Year'].fillna(firms['Domain Created Year'], inplace=True)
  return firms

def enrich_stem(firms, stem_tags):
  firms['Science'] = firms['Tags'].apply(lambda tags: any(tag in stem_tags for tag in tags))
  return firms

def get_public_funded(top_investors, public_investor_list):
  if isinstance(top_investors, str):
    top_investors = StringUtils.string_to_list(top_investors)
    for top_investor in top_investors:
      if top_investor in public_investor_list:
        return True
  
  return False

def enrich_public_funded(firms, public_investor_list):
  firms['Public Funded'] = firms['Top 5 Investors'].apply(get_public_funded, args=(public_investor_list,))
  return firms
