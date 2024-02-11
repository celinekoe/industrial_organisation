from constants import tags_path, year_range  

def init_tags_(tags):
  return {tag: 0 for tag in tags}

def init_tags_rel_tags_(tags):
  return {tag: {tag: 0 for tag in tags} for tag in tags}

def init_tags_years_(tags):
  return {tag: {year: 0 for year in year_range} for tag in tags}

def init_years_tags_(tags):
  return {year: {tag: 0 for tag in tags} for year in year_range}

def get_tags_percent(tags, tags_count, firms):    
  tags_percent = init_tags_(tags)

  for tag in tags_count:
    for year in year_range:
      if tags_count[tag] > 0:
        tags_percent[tag] = tags_count[tag] / len(firms) * 100

  return tags_percent

def get_tags_years_percent(tags, tags_years_count, years_count):    
  tags_years_percent = init_tags_years_(tags)

  for tag in tags_years_count:
    for year in year_range:
      if tags_years_count[tag][year] > 0:
        tags_years_percent[tag][year] = tags_years_count[tag][year] / years_count[year] * 100

  return tags_years_percent

def get_tags_rel_tags_percent(tags, tags_rel_tags_count):
  tags_rel_tags_percent = init_tags_rel_tags_(tags)

  for tag in tags_rel_tags_count:
    tags_rel_tags_total = sum(tags_rel_tags_count[tag].values())

    for rel_tag in tags_rel_tags_count[tag]:
      if tags_rel_tags_count[tag][rel_tag] > 0:
        tags_rel_tags_percent[tag][rel_tag] = tags_rel_tags_count[tag][rel_tag] / tags_rel_tags_total * 100

  return tags_rel_tags_percent

def get_years_tags_percent(tags, years_tags_count, years_count):
  years_tags_percent = init_years_tags_(tags)
  
  for year in year_range:
    for tag in tags:
      if years_tags_count[year][tag] > 0:
        years_tags_percent[year][tag] = years_tags_count[year][tag] / years_count[year] * 100

  return years_tags_percent
