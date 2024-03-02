import numpy as np

import config as Config
import utils.dataframe as dfUtils

class Scouter():
  def __init__():
    pass

  def _scout_one(self, df, year_col):
    year_count, year_count_growth = \
      dfUtils.get_year_count(
        df, year_col,
        Config.start_year, Config.end_year
      )
    
    return year_count, year_count_growth

  def scout(self, df):
    self.year_count, self.year_count_growth = dfUtils.get_year_count(df, self.year_col)

    for idx, i in enumerate(self.targets):
      if self.return_after and idx > self.return_after:
        break

      i_df = dfUtils.filter(df, i, self.target_col)

      i_year_count, i_year_count_growth = self._scout_one(i_df, self.year_col)

      i_year_count_lagged = i_year_count.shift(1)
      i_year_count_beta = i_year_count / i_year_count_lagged
      i_year_count_beta = i_year_count_beta.replace([np.inf, -np.inf], None)

      i_year_count_growth_lagged = i_year_count_growth.shift(1)
      i_year_count_growth_beta = i_year_count_growth / i_year_count_growth_lagged
      i_year_count_growth_beta = i_year_count_growth_beta.replace([np.inf, -np.inf], None)

      i_year_count_share, i_year_count_share_growth = dfUtils.get_year_share(i_year_count, self.year_count)

      i_year_count_share_lagged = i_year_count_share.shift(1)
      i_year_count_share_beta = i_year_count_share / i_year_count_share_lagged
      i_year_count_share_beta = i_year_count_share_beta.replace([np.inf, -np.inf], None)

      i_year_count_share_growth_lagged = i_year_count_share_growth.shift(1)
      i_year_count_share_growth_beta = i_year_count_share_growth / i_year_count_share_growth_lagged
      i_year_count_share_growth_beta = i_year_count_share_growth_beta.replace([np.inf, -np.inf], None)

      self.i_map[i] = i_df

      self.year_count_map[i] = i_year_count
      self.year_count_beta_map[i] = i_year_count_beta

      self.year_count_growth_map[i] = i_year_count_growth
      self.year_count_growth_lagged_map[i] = i_year_count_lagged
      self.year_count_growth_beta_map[i] = i_year_count_growth_beta

      self.year_count_share_map[i] = i_year_count_share
      self.year_count_share_beta_map[i] = i_year_count_share_beta

      self.year_count_share_growth_map[i] = i_year_count_share_growth
      self.year_count_share_growth_beta_map[i] = i_year_count_share_growth_beta

