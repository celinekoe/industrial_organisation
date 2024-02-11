
import pandas as pd
from pathlib import Path
import pickle

def read_pickle(file_name):
  with open(f"data/{file_name}.pickle", 'rb') as f:
    return pickle.load(f)

def read_csv_as_df(file_path):
  return pd.read_csv(file_path)

def read_dir_as_df(dir_path):
  dir = Path(dir_path)

  df_list = []

  for file_name in dir.glob('*.csv'):
    df = read_csv_as_df(file_name)
    df_list.append(df)

  return pd.concat(df_list, ignore_index=True)

def read_csv_as_list(file_path):
  return pd.read_csv(file_path, header=None).values.flatten().tolist()

def write_pickle(file_name, data):
  with open(f"data/{file_name}.pickle", 'wb') as f:
    pickle.dump(data, f)