
import pandas as pd

import constants.dirs as DirConstants

import models.firm as FirmModel
import models.investor as InvestorModel
import models.funding as FundingModel

import utils.args as Args
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

  domain_created_year = Domain.get_domain_created_year_map(undated_firms['Website'], domain_created_year, pool_size=200, chunk_size=10)

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

def prep_real_gdp():
  real_gdp = File.read_real_gdp(DirConstants.real_gdp_dir)

  File.write_pickle(f"real_gdp", real_gdp)

def prep_fed_rate():
  fed_rate = File.read_fed_rate(DirConstants.fed_rate_dir)
  File.write_pickle(f"fed_rate", fed_rate)

@Logger.timer
def main(args):
  if args['country']:
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
    
if __name__ == "__main__":
  args = Args.get_prep_args()
  
  main(args)