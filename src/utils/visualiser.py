import matplotlib.colors as mcolors
import matplotlib.pyplot as plt
import pandas as pd

def plot(series, title='', ylab=''):
  plt.figure(figsize=(10, 6))
  
  plt.plot(series.index, series.values)
    
  plt.title(title)
  plt.xlabel('Year')
  plt.ylabel(ylab)
  plt.grid(True)

  plt.show()

def plot_dict(dict, title='', ylab='', colors=None):
  plt.figure(figsize=(10, 6))

  for i, (key, series) in enumerate(dict.items()):
    color = colors[i] if colors and i < len(colors) else None
    plt.plot(series, label=key, color=color)

  plt.yscale('log')

  plt.title(title)
  plt.xlabel('Year')
  plt.ylabel(ylab)
  plt.legend()
  plt.grid(True)

  plt.show()

def stack(df, title='', labels=None, colors=None):
  years = df.index
  values = df.values.T

  if isinstance(years, pd.MultiIndex):
    years = years.levels[0]

  if not labels:
    labels = df.columns

  plt.stackplot(years, values, labels=labels, colors=colors)

  plt.title(title)
  plt.legend(loc='lower left')
  plt.xlabel('Categories')
  plt.ylabel('Cumulative Percentage')

  plt.show()

def mid_color(color1, color2, alpha=0.5):
  color1_rgb = mcolors.to_rgb(color1)
  color2_rgb = mcolors.to_rgb(color2)
  mid_color = tuple((1 - alpha) * c1 + alpha * c2 for c1, c2 in zip(color1_rgb, color2_rgb))
  
  return mid_color