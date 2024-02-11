import numpy as np
import time

from constants import tags_path, firms_path, year_range
from utils.file import read_csv_as_list, read_csv_as_df, write_pickle

start_time = time.time()

tags = read_csv_as_list(tags_path)
num_tags = len(tags)
tags_years_count = {tag: {year: 0 for year in year_range} for tag in tags}
years_count = {year: 0 for year in year_range}
tags_count = {tag: 0 for tag in tags}

firms = read_csv_as_df(firms_path)

for firm_index, firm in firms.iterrows():
  industries = [industry.strip() for industry in firm['Industries'].split(',')]

  founded_year = firm['Founded Year']
  years_count[founded_year] = years_count[founded_year] + 1 

  firm_tags = np.zeros(num_tags)
  for index, tag in enumerate(tags):
    if tag in industries:
      firm_tags[index] = 1

      tags_years_count[tag][founded_year] = tags_years_count[tag][founded_year] + 1 
      tags_count[tag] = tags_count[tag] + 1

  firm['Tags'] = firm_tags

write_pickle("firms", firms)
write_pickle("tags_years_count", tags_years_count)
write_pickle("years_count", years_count)
write_pickle("tags_count", tags_count)

end_time = time.time()
elapsed_time = end_time - start_time
print(f"preprocess execution time: {elapsed_time:.2f} seconds")