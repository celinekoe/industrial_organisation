import numpy as np
import pandas as pd

import config as Config

# Data Frame
def df(map):
  return pd.DataFrame(map) 

# Fill

def list_to_series(index_list, value_list):
  series = pd.Series(value_list, index=index_list)
  filled_series = fill_range(series)

  return filled_series

def fill_range(series):
  filled_index = pd.Index(range(Config.start_year, Config.end_year))
  series = series.reindex(filled_index, fill_value=None)

  return series

# Growth

def get_growth(series):
  growth = series.pct_change()
  growth.replace([np.inf, -np.inf], None, inplace=True)
  
  return growth

# Count

def _get_grouped_count(df, group_col):
  return df.groupby(group_col).size()

def get_year_count(df, year_col, start_year=None, end_year=None):
  year_count = _get_grouped_count(df, [year_col]) + Config.fudge_factor

  if start_year and end_year:
    year_count = fill_range(year_count)
  
  year_count_growth = get_growth(year_count)

  return year_count, year_count_growth

# Sum

def get_grouped_sum(df, group_col, sum_col):
  return df.groupby(group_col)[sum_col].sum()

def get_year_sum(df, year_col, sum_col, start_year=None, end_year=None):
  year_sum = get_grouped_sum(df, [year_col], sum_col)
  if start_year and end_year:
    year_sum = fill_range(year_sum)

  year_sum_growth = get_growth(year_sum)

  return year_sum, year_sum_growth

# Share

def get_year_share(year_count, year_total):
  year_count_share = year_count / year_total
  year_count_share_growth = get_growth(year_count_share)

  return year_count_share, year_count_share_growth

# Filter

def filter(df, filter, filter_col):
  filtered_df = df[df[filter_col].apply(lambda filter_list: filter in filter_list)]
  return filtered_df

# Rolling Average

def rolling(series):
  rolling_avg = series.rolling(window=Config.window_size).mean()
  return rolling_avg
