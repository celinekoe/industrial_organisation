import argparse 

from utils.logger import timer

import utils.firms as Firms
import utils.tags as Tags
import utils.file as File
import utils.validator as Validator

def prep_args():
  parser = argparse.ArgumentParser()
  parser.add_argument('-c', '--country', action='store_true', help='Set parameter to country')
  parser.add_argument('-n', '--name', type=str, help='Specify parameter by name')
  parser.add_argument('-v', '--validate', action='store_true', default=False, help='Enable validation')
  args = parser.parse_args()

  return vars(args)

def get_firms_path(args):
  if args['country']:
    return f"data/country/{args['name']}"

def get_pickle_path(args, file_name):
  if args['country']:
    return f"{args['name']}_{file_name}"

@timer
def main():
  args = prep_args()

  firms_path = get_firms_path(args)
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
    File.write_pickle(get_pickle_path(args, "firms"), firms)
    File.write_pickle(get_pickle_path(args, "tags"), tags)
    File.write_pickle(get_pickle_path(args, "tags_count"), tags_count)
    File.write_pickle(get_pickle_path(args, "tags_percent"), tags_percent)
    File.write_pickle(get_pickle_path(args, "years_count"), years_count)
    File.write_pickle(get_pickle_path(args, "tags_years_count"), tags_years_count)
    File.write_pickle(get_pickle_path(args, "tags_years_percent"), tags_years_percent)

if __name__ == "__main__":
  main()