from math import isnan
from pathlib import Path
import pandas as pd
import numpy as np

from constants import tags_path, firms_path, year_range
from utils.ds import get_flat_list, get_top_n, sort_keys_by_value, filter_by_key_list
from utils.file import read_dir_as_df, write_pickle
from utils.log import timer
from utils.tags import get_tags_years_percent, init_tags_years_, init_tags_, get_tags_percent, init_years_tags_, get_years_tags_percent, init_tags_rel_tags_, get_tags_rel_tags_percent
from utils.validate import validate_firms

def get_firm_tags(firm):
  firm_tags = []
  if isinstance(firm['Industries'], str):
    firm_tags = [tag.strip() for tag in firm['Industries'].split(',')]

  return firm_tags

def get_tags(firms):
  firm_tags_list = []

  for firm_index, firm in firms.iterrows():
    firm_tags = get_firm_tags(firm)
    firm_tags_list.append(firm_tags)

  return get_flat_list(firm_tags_list)

def enrich_firms(firms):
  founded_date = pd.to_datetime(firms['Founded Date'])
  firms['Founded Year'] = founded_date.dt.year

  return firms

@timer
def main():
  firms = enrich_firms(read_dir_as_df("data/by_country/singapore"))
  validate_firms(firms, skip=True)

  tags = get_tags(firms)
  tags_years_count = init_tags_years_(tags)
  tags_count = init_tags_(tags)
  years_tags_count = init_years_tags_(tags)
  years_count = {year: 0 for year in year_range}
  tags_rel_tags_count = init_tags_rel_tags_(tags)

  for firm_index, firm in firms.iterrows():
    firm_tags = get_firm_tags(firm)

    founded_year = firm['Founded Year']
    years_count[founded_year] = years_count[founded_year] + 1 

    for index, tag in enumerate(tags):
      if tag in firm_tags:
        tags_years_count[tag][founded_year] = tags_years_count[tag][founded_year] + 1 
        tags_count[tag] = tags_count[tag] + 1

        years_tags_count[founded_year][tag] = years_tags_count[founded_year][tag] + 1

    for outer_tag in firm_tags:
      for inner_tag in firm_tags:
        if outer_tag != inner_tag:
          tags_rel_tags_count[outer_tag][inner_tag] = tags_rel_tags_count[outer_tag][inner_tag] + 1

  tags_years_percent = get_tags_years_percent(tags, tags_years_count, years_count)
  tags_percent = get_tags_percent(tags, tags_count, firms)
  print(tags_percent['Biotechnology'])

  years_tags_percent = get_years_tags_percent(tags, years_tags_count, years_count)



  write_pickle("firms", firms)
  write_pickle("tags", tags)
  write_pickle("tags_count", tags_count)
  write_pickle("tags_percent", tags_percent)
  write_pickle("tags_years_count", tags_years_count)
  write_pickle("tags_years_percent", tags_years_percent)
  write_pickle("years_count", years_count)
  write_pickle("years_tags_count", years_tags_count)
  write_pickle("years_tags_percent", years_tags_percent)
    
if __name__ == "__main__":
  main()