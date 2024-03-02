import pandas as pd

def set_year(df, date_col, year_col):
  df[year_col] = df[date_col].astype(str).str[:4] # use this instead of datetime as there are pre-epoch date
  # df[year_col] = pd.to_numeric(df[year_col], errors='coerce').fillna(0).astype('int32')
  df[year_col] = pd.to_numeric(df[year_col], errors='coerce').fillna(0)
  
  return df
