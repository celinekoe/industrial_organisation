import argparse
import re
import sys

from constants import crunchbase_country_dir, pickle_dir

def get_args():
  parser = argparse.ArgumentParser()

  script_name = re.sub(r'\.py$', '', sys.argv[0])

  if script_name == 'prep':
    parser.add_argument('-c', '--country', action='store_true', help='Load country directory')
    parser.add_argument('-n', '--name', type=str, help='Specify file to load')
    parser.add_argument('-a', '--all', action='store_true', help='Load all files')
    parser.add_argument('-v', '--validate', action='store_true', default=False, help='Enable validation')
  
  if script_name == 'country':
    parser.add_argument('-c', '--country', action='store_true', help='Load country data')
    parser.add_argument('-n', '--name', type=str, help='Specify country to analyse')
    parser.add_argument('-p', '--plot', action='store_true', default=False, help='Enable plots')

  if script_name == 'tag':
    parser.add_argument('-c', '--country', action='store_true', help='Load country data')
    parser.add_argument('--region', type=str,help='Region to load')
    parser.add_argument('--countries', nargs='+',help='Countries to load')

    parser.add_argument('-t', '--tag', action='store_true', help='Load tag data')
    parser.add_argument('--tags', nargs='+',help='Tags to load')

    parser.add_argument('-n', '--name',  type=str, help='Tag to analyse')
    parser.add_argument('-p', '--plot', action='store_true', default=False, help='Enable plots')
  
  args = parser.parse_args()
  args.name = args.name.lower() if args.name else None

  return vars(args)

