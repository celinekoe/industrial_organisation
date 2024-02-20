
import pandas as pd
import copy

import constants.dirs as Const

import models.firm as FirmModel
import models.investor as InvestorModel
import models.funding as FundingModel

import utils.prep.args as Args
import utils.prep.macro as MacroUtils
import utils.domain as Domain
import utils.file as File
import utils.logger as Logger


def prep_country(args):
  country_dir = File.get_country_dir(f"{args['country_name']}")
  firms = FirmModel.enrich_firms(File.read_companies_dir(country_dir))
  print(f"firms: {firms}")

  File.write_pickle(f"{args['country_name']}_firms", firms)

def prep_domain(args):  
  domain_created_year = File.read_pickle('domain_created_year')
  if domain_created_year is None:
    domain_created_year = {}

  firms = File.read_pickle(f"{args['country_name']}_firms")
  undated_firms = firms[pd.isna(firms['Founded Year'])] # Only get the domain created year of firms we don't have date information for
  undated_firms = undated_firms[undated_firms['Website'].notnull()]

  domain_created_year = Domain.get_domain_created_year_map(undated_firms['Website'], domain_created_year, p=200, c=10)

  File.write_pickle(f"domain_created_year", domain_created_year)

def prep_investors():
  investors_dir = File.get_investors_dir()
  investors = InvestorModel.enrich(File.read_investors_dir(investors_dir))
  print(f"investors: {investors}")

  File.write_pickle(f"investors", investors)

def prep_funding():
  funding_dir = File.get_funding_dir()
  funding = FundingModel.enrich(File.read_funding_dir(funding_dir))
  print(f"funding: {funding}")

  File.write_pickle(f"funding", funding)

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
    MacroUtils.prep_real_gdp()
    MacroUtils.prep_real_gdp_growth()
    MacroUtils.prep_fed_rate()
    
if __name__ == "__main__":
  args = Args.get_prep_args()
  
  main(args)