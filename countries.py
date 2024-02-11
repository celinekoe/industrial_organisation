from utils.file import read_pickle
from utils.log import timer
from utils.ds import filter_by_key_list, get_top_n, sort_keys_by_value
from utils.viz import plot_tags_years_, plot_years, plot_pie

@timer
def main():
  years_count = read_pickle("years_count")
  # plot_years(years_count, 'Singapore', 'Count')

  tags_count = read_pickle("tags_count")
  plot_pie(tags_count)

  tags_percent = read_pickle("tags_percent")
  tags_years_percent = read_pickle("tags_years_percent")
  top_tags = get_top_n(sort_keys_by_value(tags_percent, desc=True), 10)
  top_tags_years_percent = filter_by_key_list(tags_years_percent, top_tags)
  # plot_tags_years_(top_tags_years_percent, 'Percent')

  return
    
if __name__ == "__main__":
  main()