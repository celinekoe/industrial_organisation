import argparse
import re
import sys

def get_args():
  parser = argparse.ArgumentParser()

  script = re.sub(r'\.py$', '', sys.argv[0])

  if script == 'prep':
    parser.add_argument('-c', '--country', action='store_true', help='Load country data')
    parser.add_argument('--country-all', action='store_true', default=False, help='Load all country data')
    parser.add_argument('--country-name', type=str, help='Country to load')

    parser.add_argument('-i', '--industry', action='store_true', help='Load industry data')
    parser.add_argument('-m', '--macro', action='store_true', help='Load macro data')

    parser.add_argument('-d', '--domain', action='store_true', help='Load domain data')
      
  if script == 'country':
    parser.add_argument('-c', '--country', action='store_true', help='Load country data')
    parser.add_argument('-n', '--name', type=str, help='Specify country to analyse')
    parser.add_argument('-p', '--plot', action='store_true', default=False, help='Enable plots')

  if script == 'industry':
    parser.add_argument('-i', '--industry', action='store_true', help='Load industry data')
    parser.add_argument('-n', '--name', type=str, help='Specify industry to analyse')
    parser.add_argument('-p', '--plot', action='store_true', default=False, help='Enable plots')
    parser.add_argument('--top', type=int, default=10, help='Default number of labels to plot')

  if script == 'tag':
    parser.add_argument('-c', '--country', action='store_true', help='Load country data')
    parser.add_argument('--region', type=str,help='Region to load')
    parser.add_argument('--countries', nargs='+',help='Countries to load')

    parser.add_argument('-t', '--tag', action='store_true', help='Load tag data')
    parser.add_argument('--tags', nargs='+',help='Tags to load')

    parser.add_argument('-n', '--name',  type=str, help='Tag to analyse')
    parser.add_argument('-p', '--plot', action='store_true', default=False, help='Enable plots')

  args = parser.parse_args()
  # args.name = args.name.lower() if args.name else None

  return vars(args)

