import copy

from models.country import Country
from constants import asean

import utils.args as Args
import utils.ds as ds
import utils.file as File
import utils.logger as Logger
import utils.visualiser as visualiser

def run_tag(args):
  tag = args['name'].capitalize()
  countries_count = {}
  countries_years_count = {}

  for country_name in args['countries']:
    country = Country(country_name)
    country.unpickle()
    country_data = vars(country)

    countries_count[country_name] = country_data['tags_count'][tag]
    countries_years_count[country_name] = country_data['tags_years_count'][tag]

  visualiser.plot_pie(countries_count)
  visualiser.plot_labels_years_(countries_years_count, 'Count')
  visualiser.show()

  return

@Logger.timer
def main(args):
  if args['country']:
    if args['region'] == 'asean':
      new_args = copy.deepcopy(args)
      new_args.pop('countries', None)
      new_args['countries'] = asean
      run_tag(new_args)
    else:
      run_tag(args)
    
if __name__ == "__main__":
  args = Args.get_args()
  main(args)