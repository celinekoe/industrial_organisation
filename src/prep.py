
import pandas as pd
import numpy as np
import copy

import constants as Const
import utils.args as Args
import utils.file as File
import utils.logger as Logger

import utils.domain as Domain
import utils.firms as Firms

def prep_country(args):
  country_dir = File.get_country_dir(f"{args['country_name']}")
  firms = Firms.enrich_firms(File.read_dir(country_dir))

  File.write_pickle(f"{args['country_name']}_firms", firms)

def prep_domain(args):  
  domain_created_year_map = File.read_pickle('domain_created_year_map')
  if domain_created_year_map is None:
    domain_created_year_map = {}

  firms = File.read_pickle(f"{args['country_name']}_firms")
  undated_firms = firms[pd.isna(firms['Founded Year'])] # Only get the domain created year of firms we don't have date information for
  undated_firms = undated_firms[undated_firms['Website'].notnull()]

  domain_created_year_map = Domain.get_domain_created_year_map(undated_firms['Website'], domain_created_year_map, p=200, c=10)

  File.write_pickle(f"domain_created_year_map", domain_created_year_map)

def prep_industry(args):
  tag_dir = File.get_tag_dir(args['name'])
  firms = Firms.enrich_firms(File.read_dir(tag_dir))

  File.write_pickle(f"{args['name']}_firms", firms)

def prep_real_gdp():
  real_gdp = File.read_real_gdp(Const.real_gdp_dir)
  print(real_gdp)

  File.write_pickle(f"real_gdp", real_gdp)

def prep_fed_rate():
  fed_rate = File.read_fed_rate(Const.fed_rate_dir)
  File.write_pickle(f"fed_rate", fed_rate)

def prep_pop():
  country_pop = File.read_ceic_dir(Const.ceic_pop_dir)
  File.write_pickle(f"country_pop", country_pop)

@Logger.timer
def main(args):
  if args['country']:
    if args['country_all']:
      dir_names = File.read_dir_dir_names(Const.crunchbase_country_dir)
      for dir_name in dir_names:
        new_args = copy.deepcopy(args)
        new_args.pop('all', None)
        new_args['country'] = True
        new_args['country_name'] = dir_name
        prep_country(new_args)
    else:
      prep_country(args)

  if args['domain']:
    prep_domain(args)

  if args['industry']:
    prep_industry(args)

  if args['macro']:
    prep_real_gdp()
    prep_fed_rate()
    # prep_pop()    

if __name__ == "__main__":
  args = Args.get_args()
  
  main(args)