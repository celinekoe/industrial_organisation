
import pandas as pd
import copy

import constants.dirs as Const
import utils.args as Args
import utils.domain as Domain
import utils.file as File
import utils.logger as Logger

import utils.firm as Firms
import utils.investor as Investors
import utils.funding as FundingUtils

def prep_country(args):
  country_dir = File.get_country_dir(f"{args['country_name']}")
  firms = Firms.enrich_firms(File.read_companies_dir(country_dir))

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

def prep_investors():
  investors_dir = File.get_investors_dir()
  investors = Investors.enrich(File.read_investors_dir(investors_dir))
  print(f"investors: {investors}")

  File.write_pickle(f"investors", investors)

def prep_funding():
  funding_dir = File.get_funding_dir()
  funding = FundingUtils.enrich(File.read_funding_dir(funding_dir))
  print(f"funding: {funding}")

  File.write_pickle(f"funding", funding)

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
      dir_names = File.read_companies_dir_dir_names(Const.country_dir)
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

  if args['funding']:
    prep_funding()

  if args['investors']:
    prep_investors()

  if args['macro']:
    prep_real_gdp()
    prep_fed_rate()
    # prep_pop()    

if __name__ == "__main__":
  args = Args.get_prep_args()
  
  main(args)