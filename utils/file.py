
from pathlib import Path
import os
import pandas as pd
import pickle

import constants as Constants

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

def read_pickle(file_name):
  with open(f"data/{file_name}.pickle", 'rb') as f:
    return pickle.load(f)

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

  df_dir = pd.concat(df_list, ignore_index=True)
  print(f"Bad line count: {line_count - len(df_dir)}")

  return df_dir

def read_csv_as_list(file_path):
  return pd.read_csv(file_path, header=None).values.flatten().tolist()

def write_pickle(file_name, data):
  with open(f"{Constants.data_dir}/{file_name}.pickle", 'wb') as f:
    pickle.dump(data, f)