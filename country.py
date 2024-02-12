
from utils.logger import timer

import utils.args as Args
import utils.file as File
import utils.ds as ds
import utils.vis as Viz

@timer
def main(args):
  years_count = File.read_pickle(f"{Args.get_pickle_dir(args, 'years_count')}")
  
  tags_percent = File.read_pickle(f"{Args.get_pickle_dir(args, 'tags_percent')}")
  top_tags = ds.get_top_n(ds.sort_keys_by_value(tags_percent, desc=True), 5)
  top_tags_percent = ds.value_list_from_key_list(tags_percent, top_tags)
  
  tags_years_percent = File.read_pickle(f"{Args.get_pickle_dir(args, 'tags_years_percent')}")
  top_tags_years = ds.get_top_n(ds.sort_keys_by_value(tags_percent, desc=True), 5)
  top_tags_years_percent = ds.filter_by_key_list(tags_years_percent, top_tags_years)
  
  if args['plot']:
    Viz.plot_years(years_count, args['name'], 'Count')
    Viz.plot_bar(top_tags, top_tags_percent, 'Percent')
    Viz.plot_tags_years_(top_tags_years_percent, 'Percent')

  return
    
if __name__ == "__main__":
  args = Args.get_args()
  main(args)