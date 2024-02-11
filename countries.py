from utils.file import read_pickle
from utils.log import timer
import utils.ds as ds
import utils.viz as viz

@timer
def main():
  years_count = read_pickle("years_count")
  # plot_years(years_count, 'Singapore', 'Count')

  tags_percent = read_pickle("tags_percent")
  top_tags = ds.get_top_n(ds.sort_keys_by_value(tags_percent, desc=True), 5)
  top_tags_percent = ds.value_list_from_key_list(tags_percent, top_tags)
  # viz.plot_bar(top_tags, top_tags_percent, "Percent")

  tags_years_percent = read_pickle("tags_years_percent")
  top_tags_yaers = ds.get_top_n(ds.sort_keys_by_value(tags_percent, desc=True), 5)
  top_tags_years_percent = ds.filter_by_key_list(tags_years_percent, top_tags_yaers)
  viz.plot_tags_years_(top_tags_years_percent, 'Percent')

  return
    
if __name__ == "__main__":
  main()