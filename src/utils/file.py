
import csv
from pathlib import Path
import os
import pandas as pd
import pickle

import constants.dirs as DirConstants

# CSV
def read_csv(file_path):
  return pd.read_csv(file_path, on_bad_lines='skip')

def get_csv_rows(file_path):
  with open(file_path, 'r', encoding='utf-8') as file:
    return sum(1 for row in file) - 1

def print_bad_row_count(df, row_count):
  print(f"Bad row count: {row_count - len(df)}")

# Crunchbase
def get_country_dir(name):
  return f"{DirConstants.country_dir}/{name}"
  
def get_industry_dir(name):
  return f"{DirConstants.industry_dir}/{name}"

def get_investors_dir():
  return f"{DirConstants.investors_dir}"

def get_funding_dir():
  return f"{DirConstants.funding_dir}"

def read_dir(dir_path):
  dir = Path(dir_path)

  row_count = 0

  df_list = []
  for file_name in dir.glob('*.csv'):
    df = read_csv(file_name)
    df_list.append(df)

    row_count += get_csv_rows(file_name)

  return pd.concat(df_list, ignore_index=True), row_count

def read_companies_dir(dir_path):
  df, row_count = read_dir(dir_path)
  df = df.drop_duplicates(subset=['Organization Name', 'Description']).reset_index(drop=True)
  
  print_bad_row_count(df, row_count)

  return df

def read_investors_dir(dir_path):
  df, row_count = read_dir(dir_path)
  df = df.drop_duplicates(subset=['Organization/Person Name', 'Description']).reset_index(drop=True)

  print_bad_row_count(df, row_count)

  return df

def read_funding_dir(dir_path):
  df, row_count = read_dir(dir_path)
  df = df.reset_index(drop=True)

  print_bad_row_count(df, row_count)

  return df

def read_companies_dir_dir_names(dir_path):
  return [f for f in os.listdir(dir_path) if os.path.isdir(os.path.join(dir_path, f))]

# CEIC

def read_real_gdp(dir_path):
  dir = Path(dir_path)
  line_count = 0

  df_list = []
  for file_name in dir.glob('*.csv'):
    df = read_csv(file_name)
    df.set_index('Year', inplace=True)
    df_list.append(df)

    line_count += get_csv_rows(file_name) - 1
  
  df_dir = pd.concat(df_list, axis=1, join='outer')
  print_bad_row_count(df_dir, line_count)

  df_dir.reset_index(inplace=True)
  df_dir.sort_values(by='Year', inplace=True)
  df_dir.set_index('Year', inplace=True)
  df_dir = df_dir.reindex(sorted(df_dir.columns), axis=1)

  return df_dir

def read_fed_rate(dir_path):
  dir = Path(dir_path)
  line_count = 0

  df_list = []
  for file_name in dir.glob('*.csv'):
    df = read_csv(file_name)
    df_list.append(df)

    line_count += get_csv_rows(file_name) - 1

  df_dir = pd.concat(df_list)
  print_bad_row_count(df_dir, line_count)

  df_dir['Year'] = pd.to_datetime(df_dir['Month'], format='%m/%Y').dt.year

  year_data = {
    'Year': df_dir['Year'].unique(),
    'Fed Rate': [df_dir[df_dir['Year'] == year]['United States'].mean() for year in df_dir['Year'].unique()]
  }

  year_df = pd.DataFrame(year_data)
  year_df.set_index('Year', inplace=True)

  return year_df

# Pickle

def get_pickle_dir(args, file_name):
  if args['country']:
    return f"{DirConstants.pickle_dir}/{args['name']}_{file_name}.pkl"

def read_pickle(file_name):
  try:
    with open(f"{DirConstants.pickle_dir}/{file_name}.pkl", 'rb') as f:
      return pickle.load(f)
  except FileNotFoundError:
    print(f"{DirConstants.pickle_dir}/{file_name}.pkl not found")
    return None

def write_pickle(file_name, data):
  with open(f"{DirConstants.pickle_dir}/{file_name}.pkl", 'wb') as f:
    pickle.dump(data, f)