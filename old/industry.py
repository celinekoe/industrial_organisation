import pandas as pd

from constants import year_range

import utils.args as Args
import utils.file as File
import utils.logger as Logger
import utils.visualiser as Visualiser

def get_top_country_year_count(top_firms):
  top_country_year_count = top_firms.groupby(['Founded Year', 'Country']).size().unstack()
  return top_country_year_count[top_country_year_count.sum().sort_values(ascending=False).index]

def get_top_country_year_percent(top_firms):
  top_country_year_percent = top_firms.groupby(['Founded Year', 'Country']).size() \
    .groupby(level=0).apply(lambda x: x / float(x.sum()) * 100) \
    .reset_index(level=0, drop=True) \
    .unstack()
  return top_country_year_percent[top_country_year_percent.sum().sort_values(ascending=False).index]

def stats(args, n=30):
  firms = File.read_pickle(f"{args['name']}_firms")

  country_count = firms['Country'].value_counts()
  year_count = firms['Founded Year'].value_counts().sort_index()

  top_country_count = country_count.head(n)
  top_firms = firms[firms['Country'].isin(top_country_count.index)]
  top_country_year_count = get_top_country_year_count(top_firms)
  top_country_year_percent = get_top_country_year_percent(top_firms)

  print(top_country_count.index.tolist())
  File.write_csv("top_country_count", top_country_count.index.tolist())

  # top_country_count_excl_us = country_count[country_count.index != 'United States'].head(n)
  # top_firms_excl_us = firms[firms['Country'].isin(top_country_count_excl_us.index)]
  # top_country_year_count_excl_us = get_top_country_year_count(top_firms_excl_us)
  # top_country_year_percent_excl_us = get_top_country_year_percent(top_firms_excl_us)

  if args['plot']:
    # Visualiser.pie(country_count)
    # Visualiser.show()

    # Visualiser.plot(year_count)
    # Visualiser.show()

    # Visualiser.plot_(top_country_year_count)
    # Visualiser.show()

    # Visualiser.plot_(top_country_year_percent)
    # Visualiser.show()

    # Visualiser.plot_(top_country_year_count_excl_us)
    # Visualiser.show()

    # Visualiser.plot_(top_country_year_percent_excl_us)
    # Visualiser.show()
    print()


  return

@Logger.timer
def main(args):
 
  if args['top']:
    stats(args, args['top'])
  else:
    stats(args)
    
if __name__ == "__main__":
  args = Args.get_args()
  main(args)