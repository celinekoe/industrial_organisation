
from pathlib import Path
import os
import pandas as pd
import pickle

from constants import pickle_dir

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
    print(file_name)
    df = read_csv(file_name)
    df_list.append(df)

    line_count += get_file_lines(file_name)

  df_dir = pd.concat(df_list, ignore_index=True)
  print(f"Bad line count: {line_count - len(df_dir)}")

  return df_dir

def read_dir_dir_names(dir_path):
  return [f for f in os.listdir(dir_path) if os.path.isdir(os.path.join(dir_path, f))]

# Pickle

def get_pickle_path(args, file_name):
  if args['country']:
    return f"{pickle_dir}/{args['name']}_{file_name}.pkl"

def read_pickle(file_name):
  with open(f"{file_name}", 'rb') as f:
    return pickle.load(f)

def write_pickle(args, file_name, data):
  file_path = get_pickle_path(args, file_name)
  with open(f"{file_path}", 'wb') as f:
    pickle.dump(data, f)