
import csv
from pathlib import Path
import os
import pandas as pd
import pickle

from constants import crunchbase_country_dir, crunchbase_industry_dir, pickle_dir

def get_file_lines(file_path):
  with open(file_path, 'r', encoding='utf-8') as file:
    return sum(1 for line in file)

def get_dir_lines(dir_path):
  
  dir = Path(dir_path)

  line_count = 0
  for file_name in dir.glob('*.csv'):
    df = read_csv(file_name)
    line_count += get_file_lines(file_name)

  return line_count

def read_csv(file_path):
  return pd.read_csv(file_path, on_bad_lines='skip')

def read_dir(dir_path):
  dir = Path(dir_path)

  line_count = 0

  df_list = []
  for file_name in dir.glob('*.csv'):
    df = read_csv(file_name)
    df_list.append(df)

    line_count += get_file_lines(file_name)

  df_dir = pd.concat(df_list, ignore_index=True).drop_duplicates()
  print(f"Bad line count: {line_count - len(df_dir)}")

  return df_dir

def read_dir_dir_names(dir_path):
  return [f for f in os.listdir(dir_path) if os.path.isdir(os.path.join(dir_path, f))]

def write_csv(file_path, data):
  with open(f"output/{file_path}.csv", 'w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    for row in data:
      writer.writerow([row])

# CEIC

def read_ceic_dir(dir_path):
  dir = Path(dir_path)
  line_count = 0

  df_list = []
  for file_name in dir.glob('*.csv'):
    df = read_csv(file_name)
    df_list.append(df)
    line_count += get_file_lines(file_name)

  df_dir = pd.concat(df_list, ignore_index=True)
  
  if 'Year' in df_dir.columns:
    df_dir.set_index('Year', inplace=True)
  if 'Month' in df_dir.columns:
    df_dir['Year'] = pd.to_datetime(df_dir['Month'], format='%m/%Y').dt.year

    year_data = {
      'Year': df_dir['Year'].unique(),
      'Fed Rate': [df_dir[df_dir['Year'] == year]['United States'].mean() for year in df_dir['Year'].unique()]
    }

    year_df = pd.DataFrame(year_data)
    year_df.set_index('Year', inplace=True)
    df_dir = year_df

  print(f"Bad line count: {line_count - len(df_dir)}")

  return df_dir[sorted(df_dir.columns.tolist())]

# Crunchbase

def get_country_dir(name):
  return f"{crunchbase_country_dir}/{name}"
  
def get_tag_dir(name):
  return f"{crunchbase_industry_dir}/{name}"

# Pickle

def get_pickle_dir(args, file_name):
  if args['country']:
    return f"{pickle_dir}/{args['name']}_{file_name}.pkl"

def read_pickle(file_name):
  with open(f"{pickle_dir}/{file_name}.pkl", 'rb') as f:
    return pickle.load(f)

def write_pickle(file_name, data):
  with open(f"{pickle_dir}/{file_name}.pkl", 'wb') as f:
    pickle.dump(data, f)