
import copy

import constants as Const
import utils.args as Args
import utils.file as File
import utils.logger as Logger

import utils.firms as Firms

def prep_country(args):
  country_dir = File.get_country_dir(f"{args['country_name']}")
  firms = Firms.enrich_firms(File.read_dir(country_dir))
  print(firms)

  File.write_pickle(f"{args['country_name']}_firms", firms)

def prep_industry(args):
  tag_dir = File.get_tag_dir(args['name'])
  firms = Firms.enrich_firms(File.read_dir(tag_dir))

  File.write_pickle(f"{args['name']}_firms", firms)

def prep_gdp():
  country_gdp = File.read_ceic_dir(Const.ceic_gdp_dir)
  File.write_pickle(f"country_gdp", country_gdp)

def prep_fed_rate():
  fed_rate = File.read_ceic_dir(Const.ceic_fed_rate_dir)
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

  if args['industry']:
    prep_industry(args)

  if args['macro']:
    # prep_gdp()
    prep_fed_rate()
    # prep_pop()    

if __name__ == "__main__":
  args = Args.get_args()
  
  main(args)