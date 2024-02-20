# String

def string_to_list(string):
  items = []
  if isinstance(string, str):
    items = [item.strip() for item in string.split(',')]

  return items

def prepend_string(string, prepend):
  if prepend:
    string = f'{prepend}: {string}'
  return string

# Dict

def sort_dict(dict_):  
  return dict(sorted(dict_.items(), key=lambda item: item[1], reverse=True))

def sum_dict(dict_):
  new_dict = {}
  for key, value in dict_.items():
    new_dict[key] = value.sum()

  return new_dict

def top_n(dict, n):
  return first_n(sort_dict(dict), n)

def first_n(dict, n):
  new_dict = {}
  for key, value in list(dict.items())[:n]:
    new_dict[key] = value
  return new_dict

def flip_list_dict(dict):
  flipped_dict = {}
  for key, list in dict.items():
    for inner_key in list:
      if inner_key in flipped_dict:
        flipped_dict[inner_key].append(key)
      else:
        flipped_dict[inner_key] = [key]
  return flipped_dict
