def string_to_list(string):
  items = []
  if isinstance(string, str):
    items = [item.strip() for item in string.split(',')]

  return items
