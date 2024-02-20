def string_to_list(string):
  items = []
  if isinstance(string, str):
    items = [item.strip() for item in string.split(',')]

  return items

def list_in_list(list1, list2):
  return any(item in list2 for item in list1)

def flip_list_dict(dict):
  flipped_dict = {}
  for key, list in dict.items():
    for inner_key in list:
      if inner_key in flipped_dict:
        flipped_dict[inner_key].append(key)
      else:
        flipped_dict[inner_key] = [key]
  return flipped_dict
