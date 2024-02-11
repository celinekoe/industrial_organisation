from constants import tags_path, year_range
from utils.ds import filter_by_key_list, get_top, sort_keys_by_value
from utils.file import read_pickle, read_csv_as_list
from utils.viz import plot_tags, plot_tag

import time

start_time = time.time()

tags = read_csv_as_list(tags_path)
firms = read_pickle("firms")
tags_years_count = read_pickle("tags_years_count")
years_count = read_pickle("years_count")
tags_count = read_pickle("tags_count")

def get_tags_years_percent(tags, tags_year_count, fill_blanks=True):
  tags_years_percent = {tag: {} for tag in tags}
  for tag in tags_year_count:
    for year in year_range:
      if tags_year_count[tag][year] > 0:
        tags_years_percent[tag][year] = tags_year_count[tag][year] / years_count[year] * 100
      elif fill_blanks:
        tags_years_percent[tag][year] = 0
  return tags_years_percent

def get_tags_max_min_diff_percent(tags, tags_years_percent):
  tags_max_percent = {}
  tags_min_percent = {}
  tags_diff_percent = {}

  for tag in tags:
    tag_percent = tags_years_percent[tag]

    max_percent = 0
    min_percent = 100
    for year, percent in tag_percent.items():
      if percent > 0:
        if percent > max_percent:
          max_percent = percent
          tags_max_percent[tag] = max_percent
        if percent < min_percent:
          min_percent = percent
          tags_min_percent[tag] = min_percent

    tags_diff_percent[tag] = (max_percent - min_percent) / max_percent * 100
  
  return tags_max_percent, tags_min_percent, tags_diff_percent

def get_top_tags_by_(tags_years_percent, tags_):
  top_tags = get_top(sort_keys_by_value(tags_, desc=True))
  return filter_by_key_list(tags_years_percent, top_tags)

tags_years_percent = get_tags_years_percent(tags, tags_years_count)
tags_max_percent, tags_min_percent, tags_diff_percent = get_tags_max_min_diff_percent(tags, tags_years_percent)

top_tags_max_percent = get_top_tags_by_(tags_years_percent, tags_max_percent)
# plot_tags(top_tags_max_percent, 'Percent of Founded Startups By Category')

top_tags_diff_percent = get_top_tags_by_(tags_years_percent, tags_diff_percent)
# plot_tags(top_tags_diff_percent, 'Percent of Founded Startups By Category')

single_tag = 'Genetics'
plot_tag(single_tag, tags_years_percent[single_tag])

end_time = time.time()
elapsed_time = end_time - start_time
print(f"Script execution time: {elapsed_time} seconds")
