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
  founded_date = pd.to_datetime(firms['Founded Date'])

  firms['Country'] =  firms['Headquarters Location'].apply(get_country)
  firms['Founded Year'] = founded_date.dt.year
  firms['Tags'] =  firms['Industries'].apply(get_tags)

  return firms

# def get_firm_tags(firm):
#   firm_tags = []
#   if isinstance(firm['Industries'], str):
#     firm_tags = [tag.strip() for tag in firm['Industries'].split(',')]

#   return firm_tags

# def get_firms_tags(firms):
#   firm_tags_list = []

#   for firm_index, firm in firms.iterrows():
#     firm_tags = get_firm_tags(firm)
#     firm_tags_list.append(firm_tags)

#   return get_flat_list(firm_tags_list)