import argparse
import re
import sys

from constants import crunchbase_country_dir, pickle_dir

def get_args():
  parser = argparse.ArgumentParser()
  parser.add_argument('-c', '--country', action='store_true', help='Set parameter to country')
  parser.add_argument('-n', '--name', type=str, help='Specify parameter by name')

  script_name = re.sub(r'\.py$', '', sys.argv[0])

  if script_name == 'prep':
    parser.add_argument('-a', '--all', action='store_true', help='Specify parameter as all')
    parser.add_argument('-v', '--validate', action='store_true', default=False, help='Enable validation')
  
  if script_name == 'country':
    parser.add_argument('-p', '--plot', action='store_true', default=False, help='Enable plots')
  
  args = parser.parse_args()
  args.name = args.name.lower() if args.name else None

  return vars(args)

def get_crunchbase_path(args):
  if args['country']:
    return f"{crunchbase_country_dir}/{args['name']}"

def get_pickle_path(args, file_name):
  if args['country']:
    return f"{args['name']}_{file_name}"
