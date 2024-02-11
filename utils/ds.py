from constants import top_count, exclude_top_count

def filter_by_key_list(dict, key_list, incl=True):
  return {key: value for key, value in dict.items() if key in key_list}

def sort_keys_by_value(dict, desc=True):
  sorted_tuples = sorted(dict.items(), key=lambda key_value: key_value[1], reverse=desc)
  return extract_first(sorted_tuples)

def extract_first(list):
  return [t[0] for t in list]

def get_top(list):
  return list[exclude_top_count:exclude_top_count + top_count]