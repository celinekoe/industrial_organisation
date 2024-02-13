import pandas as pd

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
  firms['Tags'] =  firms['Industries'].apply(get_tags)
  firms['Tag Groups'] =  firms['Industry Groups'].apply(get_tags)

  # firms = firms[firms['Company Type'] == 'For Profit']
  # firms = firms[pd.notna(firms['Founded Year'])]
  # return firms.reset_index(drop=True)
  return firms