import matplotlib.pyplot as plt

import config as Config

def plot_labels(plt, title, ylab, ylim, legend=False, grid=True):
  plt.title(title)
  plt.xlabel('Year')
  plt.ylabel(ylab)

  plt.xlim(Config.start_year - 5, Config.end_year)
  if ylim:
    plt.ylim(ylim)

  if legend:
    plt.legend(loc='lower left')

  if grid:
    plt.grid(True)

def plot(series, title='', ylab='', ylim=None, highlight_vertical=None, highlight_horizontal=None):
  # plt.figure(figsize=(10, 6))
    
  plt.plot(series.index, series.values)

  if highlight_vertical:
    for year in highlight_vertical:
      plt.axvline(x=year, color='r', linestyle='--')

  if highlight_horizontal:
    for value in highlight_horizontal:
      plt.axhline(y=value, color='b', linestyle='--')

  plot_labels(plt, title, ylab, ylim)

  plt.show()