import numpy as np

import constants.config as Config

import hangar.Navigation as Navigation
import hangar.Optics as Optics

import utils.common as CommonUtils
import utils.dataframe as dfUtils

import visual.visualiser as Visualiser

class Bomber:
  def __init__(self, macro):
    self.factory_type = ''
    self.macro = macro

    self.industry_groups = Navigation.get_industry_groups()
    self.industries = Navigation.get_industries()

    self.ig_map = {}
    self.i_map = {}
    self.year_count = None
    self.year_count_growth = None

    self.year_count_map = {}
    self.year_count_growth_map = {}
    self.year_count_share_map = {}
    self.year_count_share_growth_map = {}

    self._reset_identify()
  
  def _reset_identify(self):
    self.walks = []
    self.climb = None

    self.rolling_coef_map = {}

  def _refurbish(self, refurb):
    props = [attr for attr in dir(refurb) if not attr.startswith('__') and not callable(getattr(refurb, attr))]
    for prop in props:
      setattr(self, prop, getattr(refurb, prop))

  def _scout_one(self, df, year_col):
    year_count, year_count_growth = \
      dfUtils.get_year_count(
        df, year_col,
        Config.start_year, Config.end_year
      )
    
    return year_count, year_count_growth

  def _identify_rolling(self, series, i):
    rolling_year = []
    rolling_coef = []

    rolling_subsets = Optics.get_rolling_subsets(series)
    
    for idx, subset in enumerate(rolling_subsets):
      ar_coef, ar_coef_p = Optics.ar(subset, i)
      rolling_year.append(subset.index[0])
      rolling_coef.append(ar_coef)

    self.rolling_coef_map[i] = dfUtils.list_to_series(rolling_year, rolling_coef)

  def _identify_one(self, i):
    max_count = self.year_count_map[i].max()
    count_threshold = Config.count_threshold

    try:
      if max_count > count_threshold:
        explosion = Optics.explosion(self.year_count_share_growth_map[i])
        if explosion:
          self.explosions.append(i)

        share_adf_p, lag = Optics.adf(self.year_count_share_map[i])
        if Optics.accept_null(share_adf_p):
          self.walks.append(i)

        self._identify_rolling(self.year_count_share_map[i], i)
      
    except Exception as e:
      print(f'identify failed for {i} with error: ', e)

  def _identify_climb(self):
    year_coefs = []
    for year in Config.year_range:
      coefs = []
      for i, rolling_coef in self.rolling_coef_map.items():
        coef = rolling_coef[year]
        if not np.isnan(coef):
          coefs.append(coef)

      if len(coefs) > Config.min_industries:
        mean_coef = sum(coefs) / len(coefs)
        year_coefs.append(mean_coef)
      else:
        year_coefs.append(None)

    self.climb = dfUtils.list_to_series(Config.year_range, year_coefs)

  def _plot(self, series, series_lab, y_lab='', i=''):
    Visualiser.plot(series,
                    CommonUtils.prepend_string(f'{self.factory_type}: {series_lab}', i), y_lab,
                    highlight=self.macro.recessions)

  def scout(self, df, year_col, return_after):
    self.year_count, self.year_count_growth = dfUtils.get_year_count(df, year_col)

    for idx, i in enumerate(self.industries):
      if return_after and idx > return_after:
        break

      i_df = dfUtils.filter_industry(df, i)
      i_year_count, i_year_count_growth = self._scout_one(i_df, year_col)
      i_year_count_share, i_year_count_share_growth = dfUtils.get_year_share(i_year_count, self.year_count)

      self.i_map[i] = i_df
      self.year_count_map[i] = i_year_count
      self.year_count_growth_map[i] = i_year_count_growth
      self.year_count_share_map[i] = i_year_count_share
      self.year_count_share_growth_map[i] = i_year_count_share_growth

  def identify(self, return_after):
    self._reset_identify()

    for idx, i in enumerate(self.industries):
      if return_after and idx > return_after:
        break

      self._identify_one(i)

    self._identify_climb()

  def report(self):
    self._plot(self.climb, 'Trend')