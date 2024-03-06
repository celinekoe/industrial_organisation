import pandas as pd

import config as Config

def _get_year(df, date_col):
  year = df[date_col].astype(str).str[:4] # use this instead of datetime as there are invalid dates
  year = pd.to_numeric(year, errors='coerce').fillna(0)

  return year

def _get_month(df, date_col):
  month = df[date_col].astype(str).str[5:7]  # use this instead of datetime as there are invalid dates
  month = pd.to_numeric(month, errors='coerce').fillna(0)

  return month

def set_year(df, date_col, year_col):
  df[year_col] = _get_year(df, date_col)

  return df

def set_month(df, date_col, month_col):
  year = _get_year(df, date_col)
  year_index = year - Config.start_year

  month = _get_month(df, date_col)
  df[month_col] = year_index * 12 + month
  
  return df
