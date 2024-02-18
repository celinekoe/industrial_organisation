def get_country(headquarters):
  country = None
  if isinstance(headquarters, str):
    tokens = headquarters.split(',')
    country = tokens[len(tokens) - 1].strip()

  return country