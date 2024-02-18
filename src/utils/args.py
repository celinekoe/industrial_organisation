import argparse

def get_prep_args():
  parser = argparse.ArgumentParser()

  parser.add_argument('-c', '--country', action='store_true', help='Load country data')
  parser.add_argument('--country-all', action='store_true', default=False, help='Load all country data')
  parser.add_argument('--country-name', type=str, help='Country to load')

  parser.add_argument('-i', '--investors', action='store_true', help='Load investors data')

  parser.add_argument('-d', '--domain', action='store_true', help='Load domain data')

  parser.add_argument('-m', '--macro', action='store_true', help='Load macro data')

  args = parser.parse_args()

  return vars(args)

