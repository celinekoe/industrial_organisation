
import copy

from constants import crunchbase_country_dir

import utils.args as Args
import utils.file as File
import utils.logger as Logger
import utils.validator as Validator

import utils.firms as Firms
import utils.tags as Tags

def prep(args):
  firms_path = Args.get_crunchbase_path(args)
  firms = Firms.enrich_firms(File.read_dir(firms_path))
  Validator.validate_firms(firms, skip=(not args['validate']))

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

  if args['country']:
    File.write_pickle(args, "firms", firms)
    File.write_pickle(args, "tags", tags)
    File.write_pickle(args, "tags_count", tags_count)
    File.write_pickle(args, "tags_percent", tags_percent)
    File.write_pickle(args, "years_count", years_count)
    File.write_pickle(args, "tags_years_count", tags_years_count)
    File.write_pickle(args, "tags_years_percent", tags_years_percent)

@Logger.timer
def main(args):
  if args['country']:
    if args['all']:
      dir_names = File.read_dir_dir_names(crunchbase_country_dir)
      for dir_name in dir_names:
        new_args = copy.deepcopy(args)
        new_args.pop('all', None)
        new_args['country'] = True
        new_args['name'] = dir_name
        prep(new_args)
    else:
      prep(args)

if __name__ == "__main__":
  args = Args.get_args()
  
  main(args)