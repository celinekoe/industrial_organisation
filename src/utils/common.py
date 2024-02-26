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

def flip_list_dict(dict):
  flipped_dict = {}
  for key, list in dict.items():
    for inner_key in list:
      if inner_key in flipped_dict:
        flipped_dict[inner_key].append(key)
      else:
        flipped_dict[inner_key] = [key]
  return flipped_dict
