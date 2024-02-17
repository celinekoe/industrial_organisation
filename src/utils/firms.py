import pandas as pd
import whois

def get_country(headquarters):
  country = None
  if isinstance(headquarters, str):
    tokens = headquarters.split(',')
    country = tokens[len(tokens) - 1].strip()

  return country

def get_tags(industries):
  firm_tags = []
  if isinstance(industries, str):
    firm_tags = [tag.strip() for tag in industries.split(',')]

  return firm_tags

def enrich_firms(firms):
  firms['Country'] =  firms['Headquarters Location'].apply(get_country)
 
  firms['Founded Year'] = firms['Founded Date'].astype(str).str[:4] # use this instead of datetime as there are pre-epoch date
  firms['Founded Year'] = pd.to_numeric(firms['Founded Year'], errors='coerce')
 
  firms['Exit Year'] = firms['Exit Date'].astype(str).str[:4] # use this instead of datetime as there are pre-epoch date
  firms['Exit Year'] = pd.to_numeric(firms['Exit Year'], errors='coerce')
 
  firms['Tags'] =  firms['Industries'].apply(get_tags)
  firms['Tag Groups'] =  firms['Industry Groups'].apply(get_tags)

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

def enrich_science(firms, science_map):
  science_tag_groups = [key for key, value in science_map.items() if value]
  print(science_tag_groups)
  firms['Science'] = firms['Tag Groups'].apply(lambda tag_groups: any(tag_group in science_tag_groups for tag_group in tag_groups))
  return firms