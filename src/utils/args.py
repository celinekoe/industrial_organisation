import argparse

def get_prep_args():
  parser = argparse.ArgumentParser()

  parser.add_argument('-c', '--country', action='store_true', help='Prep firm data by country')
  parser.add_argument('--country-name', type=str, help='Country to Prep')

  parser.add_argument('-d', '--domain', action='store_true', help='Prep firm domain data')

  parser.add_argument('-i', '--investors', action='store_true', help='Prep investor data')

  parser.add_argument('-f', '--funding', action='store_true', help='Prep funding data')

  parser.add_argument('-m', '--macro', action='store_true', help='Prep macro data')

  args = parser.parse_args()

  return vars(args)

