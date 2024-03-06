import numpy as np

import config as Config
import utils.dataframe as dfUtils

class Scouter():
  def __init__():
    pass

  # def _scout_one(self, df, year_col):
  #   year_count, year_count_growth = \
  #     dfUtils.get_year_count(
  #       df, year_col,
  #       Config.start_year, Config.end_year
  #     )
    
  #   return year_count, year_count_growth

  def scout(self, df):
    self.year_count, self.year_count_growth = dfUtils.get_year_count(df, self.year_col)
    self.year_volatility = self.year_count_growth.rolling(window=Config.window_size).mean()

    for idx, i in enumerate(self.targets):
      if self.return_after and idx > self.return_after:
        break

      i_df = dfUtils.filter(df, i, self.target_col)
      self.i_map[i] = i_df

      i_year_count, i_year_count_growth = dfUtils.get_year_count(i_df, self.year_col)
      self.year_count_map[i], self.year_count_growth_map[i] = i_year_count, i_year_count_growth

      i_year_count_growth_rolling = i_year_count_growth.rolling(window=Config.window_size).mean()

      # i_year_count_growth_lagged = i_year_count_growth.shift(1)
      # i_year_count_growth_lagged_rolling = i_year_count_growth_lagged.rolling(window=Config.window_size).mean()
      
      # i_year_count_growth_beta = i_year_count_growth_rolling - i_year_count_growth_lagged_rolling
      # i_year_count_growth_beta = i_year_count_growth_beta.replace([np.inf, -np.inf], None)
      # i_year_count_growth_beta_abs = i_year_count_growth_beta.copy()
      # i_year_count_growth_beta_abs[~i_year_count_growth_beta.isna()] = i_year_count_growth_beta_abs[~i_year_count_growth_beta.isna()].abs()

      # i_year_volatility = i_year_count_growth.rolling(window=Config.window_size).std()
      # self.year_volatility[i] = i_year_volatility
      i_year_count_growth_beta = i_year_count_growth.rolling(window=Config.window_size).std()

      self.year_count_growth_rolling_map[i] = i_year_count_growth_rolling
      self.year_count_growth_beta_map[i] = i_year_count_growth_beta
      # self.year_count_growth_beta_abs_map[i] = i_year_count_growth_beta_abs

