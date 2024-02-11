from constants import top_count, exclude_top_count

from collections import defaultdict

def filter_by_key_list(dict, key_list, incl=True):
  return {key: value for key, value in dict.items() if key in key_list}

def value_list_from_key_list(dict, key_list, incl=True):
  return [dict[key] for key in key_list if key in dict]

def sort_keys_by_value(dict, desc=True):
  sorted_tuples = sorted(dict.items(), key=lambda key_value: key_value[1], reverse=desc)
  return extract_first(sorted_tuples)

def extract_first(list):
  return [t[0] for t in list]

def get_key_count_from_list(list):
  count = defaultdict(int)
  for sub_list in list:
    for key in sub_list:
      count[key] += 1
  return dict(count)

def get_top_n(list, n, start=0):
  return list[start:start + n]

def get_flat_list(parent_list, unique=True):
  flat_list = [item for child_list in parent_list for item in child_list]
  
  if unique:
    flat_list = list(set(flat_list))

  return flat_list
