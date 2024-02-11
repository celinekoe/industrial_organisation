from constants import year_range

def validate_firms(firms, skip=False):
  valid = True

  if skip:
    return valid
  
  for year in year_range:
    year_found = False

    for firm_index, firm in firms.iterrows():
      if year_found == False:
        founded_year = firm['Founded Year']

        if year == founded_year:
          year_found = True
    
    if year_found == False:
      valid = False
      print(f"year {year} not found")
      
      return valid
    
  return valid