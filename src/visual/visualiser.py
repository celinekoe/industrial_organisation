import os
import sys

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import statsmodels.tsa.stattools as stattools 
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
import scipy.stats as stats

import constants.visual as VisualConstants
import utils.common as CommonUtils


def plot_labels(plt, title, ylab, legend=False, grid=True):
  plt.title(title)
  plt.xlabel('Year')
  plt.ylabel(ylab)

  if legend:
    plt.legend(loc='lower left')
  if grid:
    plt.grid(True)

def plot(series, title='', ylab='', highlight=None, year_start=None):
  # plt.figure(figsize=(10, 6))
  
  if year_start:
    series = series.loc[year_start:]
  
  plt.plot(series.index, series.values)

  if highlight:
    for year in highlight:
      if year_start is None or year >= year_start:
        plt.axvline(x=year, color='r', linestyle='--')
    
  plot_labels(plt, title, ylab)

  plt.show()

def plot_dict(dict, title='', ylab='', log_scale=True, colors=None, highlight=None):
  # plt.figure(figsize=(10, 6))

  if log_scale:
    plt.yscale('log')

  for i, (key, series) in enumerate(dict.items()):
    color = colors[i] if colors and i < len(colors) else None
    plt.plot(series, label=key, color=color)

  if highlight:
    for year in highlight:
      plt.axvline(x=year, color='r', linestyle='--')

  plot_labels(plt, title, ylab, legend=True)

  plt.show()

def stack(df, title='', ylab='', labels=None, colors=None,  year_start=None):
  if year_start:
    df = df.loc[year_start:]

  years = df.index
  values = df.values.T

  if isinstance(years, pd.MultiIndex):
    years = years.levels[0]

  if not labels:
    labels = df.columns

  plt.stackplot(years, values, labels=labels, colors=colors)

  plot_labels(plt, title, ylab, legend=True, grid=False)

  plt.show()

def granger_causality(series, max_lag):
  y_series = series[0]
  x_series = series[1]

  # Suppress printing of granger causality results
  original_stdout = sys.stdout
  
  try:
    sys.stdout = open(os.devnull, 'w')
    granger_result = stattools.grangercausalitytests(pd.concat([y_series, x_series], axis=1), maxlag=max_lag)
  finally:
    sys.stdout = original_stdout
 
  granger_tests = {}

  for lag in range(1, max_lag + 1):
      ssr_ftest = granger_result[lag][0]['ssr_ftest']
      granger_tests[lag] = ssr_ftest

  return granger_tests

def regression(series, series_label, group_label=''):
  y_series = series[0]
  x_series = series[1]

  slope, intercept, r_value, p_value, std_err = stats.linregress(x_series, y_series)

  y_label = series_label[0]
  x_label = series_label[1]
  title = CommonUtils.prepend_string(f"{y_label}, {x_label}", group_label)

  plt.scatter(x_series, y_series, color='blue', label='Data')
  plt.plot(x_series, intercept + slope * x_series, color='red', label='Regression line')

  plt.xlabel(x_label)
  plt.ylabel(y_label)
  plt.title(title)
  plt.legend()

  plt.text(0, -0.2, f'Points: {len(y_series)}', fontsize=10, color='black', transform=plt.gca().transAxes)
  plt.text(0, -0.25, f'Slope: {slope:.2f}', fontsize=10, color='black', transform=plt.gca().transAxes)
  plt.text(0, -0.3, f'r-value: {r_value:.2f}', fontsize=10, color='black', transform=plt.gca().transAxes)
  plt.text(0, -0.35, f'p-value: {p_value:.4f}', fontsize=10, color='black', transform=plt.gca().transAxes)

  left_space = 0.3
  max_lag = 2
  granger_tests = granger_causality([y_series, x_series], max_lag)
  for lag in range(1, max_lag + 1):
    plt.text(left_space * lag, -0.2, f'Lag: {lag}', fontsize=10, color='black', transform=plt.gca().transAxes)
    plt.text(left_space * lag, -0.25, f'f-statistic: {granger_tests[lag][0]:.2f}', fontsize=10, color='black', transform=plt.gca().transAxes)
    plt.text(left_space * lag, -0.3, f'p-value: {granger_tests[lag][1]:.2f}', fontsize=10, color='black', transform=plt.gca().transAxes)

  plt.grid(True)
  plt.show()

def regression_bomb(series):
  y_series = series[0]
  x_series = series[1]

  slope, intercept, r_value, p_value, std_err = stats.linregress(x_series, y_series)
  if p_value < 0.05:
    return True

  max_lag = 2
  granger_tests = granger_causality([y_series, x_series], max_lag)

  for lag in range(1, max_lag + 1):
    if granger_tests[lag][1] < 0.05:
      return True
  
  return False

def cf(series, lags):
  plot_acf(series, lags=lags)
  plt.title('Autocorrelation Function (ACF)')
  plt.xlabel('Lag')
  plt.ylabel('Autocorrelation')
  plt.show()

  # Plot PACF
  plot_pacf(series, lags=lags)
  plt.title('Partial Autocorrelation Function (PACF)')
  plt.xlabel('Lag')
  plt.ylabel('Partial Autocorrelation')
  plt.show()
