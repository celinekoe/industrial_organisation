
import copy

from models.country import Country

import constants as Const
import utils.args as Args
import utils.file as File
import utils.logger as Logger

import utils.firms as Firms
import utils.tags as Tags

def prep_country(args):
  crunchbase_dir = File.get_country_dir(args['name'])
  firms = Firms.enrich_firms(File.read_dir(crunchbase_dir))

  tags = Firms.get_firms_tags(firms)

  tags_count = Tags.init_tags_(tags)
  years_count = Tags.init_years_()

  tags_years_count = Tags.init_tags_years_(tags)

  for firm_index, firm in firms.iterrows():
    firm_tags = Firms.get_firm_tags(firm)

    founded_year = firm['Founded Year']
    years_count[founded_year] = years_count[founded_year] + 1 

    for index, tag in enumerate(tags):
      if tag in firm_tags:
        tags_years_count[tag][founded_year] = tags_years_count[tag][founded_year] + 1 
        tags_count[tag] = tags_count[tag] + 1

  tags_percent = Tags.get_tags_percent(tags, tags_count, firms)
  tags_years_percent = Tags.get_tags_years_percent(tags, tags_years_count, years_count)

  country = Country(args['name'])
  country.set_firms(firms)
  country.set_tags(tags)
  country.set_tags_(tags_count, tags_percent)
  country.set_years_(years_count)
  country.set_tags_years_(tags_years_count, tags_years_percent)

  country.pickle()

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
    if args['all']:
      dir_names = File.read_dir_dir_names(Const.crunchbase_country_dir)
      for dir_name in dir_names:
        new_args = copy.deepcopy(args)
        new_args.pop('all', None)
        new_args['country'] = True
        new_args['name'] = dir_name
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