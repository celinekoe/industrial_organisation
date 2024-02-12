from utils.file import read_dir, write_pickle
from utils.logger import timer
from utils.validator import validate_firms

import utils.ds as ds
import utils.vis as vis
import utils.firms as Firms
import utils.tags as Tags

@timer
def main():
  firms = Firms.enrich_firms(read_dir("data/by_country/singapore"))
  validate_firms(firms, skip=True)

  tags = Firms.get_firms_tags(firms)
  
  tags_percent = None
  ignore_tags = []
  ignore_count = 0

  while ignore_count < len(firms):
    tags_count = Tags.init_tags_(tags)
    ignore_count = 0

    for firm_index, firm in firms.iterrows():
      firm_tags = Firms.get_firm_tags(firm)
      
      ignore = False
      if len(firm_tags) == 0:
        ignore_count += 1
        continue
      
      for ignore_tag in ignore_tags:
        if ignore_tag in firm_tags:
          tags_count[ignore_tag] = tags_count[ignore_tag] + 1
          ignore = True
          break

      if ignore:
        ignore_count += 1
      else:
        for tag in tags:
          if tag in firm_tags:
            tags_count[tag] = tags_count[tag] + 1

    tags_percent = Tags.get_tags_percent(tags, tags_count)
    top_tags_percent = ds.sort_keys_by_value(tags_percent, desc=True)

    for tag in top_tags_percent:
      if tag not in ignore_tags:
        ignore_tags.append(tag)
        break

  write_pickle("part_tags", ignore_tags) 
  write_pickle("part_tags_percent", tags_percent)
    
if __name__ == "__main__":
  main()