from constants import year_range

def validate_firms(firms, skip=False):
  valid = True

  if skip:
    return valid
  
  missing_years = []
  for year in year_range:
    year_found = False

    for firm_index, firm in firms.iterrows():
      if year_found == False:
        founded_year = firm['Founded Year']

        if year == founded_year:
          year_found = True
    
    if year_found == False:
      valid = False
      missing_years.append(year)
    
  print(f"years {missing_years} not found")

  return valid