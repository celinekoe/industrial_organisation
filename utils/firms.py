import pandas as pd

from utils.ds import get_flat_list

def enrich_firms(firms):
  founded_date = pd.to_datetime(firms['Founded Date'])
  firms['Founded Year'] = founded_date.dt.year

  return firms

def get_firm_tags(firm):
  firm_tags = []
  if isinstance(firm['Industries'], str):
    firm_tags = [tag.strip() for tag in firm['Industries'].split(',')]

  return firm_tags

def get_firms_tags(firms):
  firm_tags_list = []

  for firm_index, firm in firms.iterrows():
    firm_tags = get_firm_tags(firm)
    firm_tags_list.append(firm_tags)

  return get_flat_list(firm_tags_list)