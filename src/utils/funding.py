import pandas as pd

def enrich(investors):
  investors['Announced Year'] = investors['Announced Date'].astype(str).str[:4] # use this instead of datetime as there are pre-epoch date
  investors['Announced Year'] = pd.to_numeric(investors['Announced Year'], errors='coerce')

  return investors