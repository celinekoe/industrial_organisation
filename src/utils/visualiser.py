import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import pandas as pd

def plot(series, ylab):
  plt.figure(figsize=(10, 6))
  
  plt.plot(series.index, series.values)
    
  plt.xlabel('Year')
  plt.ylabel(ylab)
  plt.grid(True)

def plot_dict(dict, ylab):
  plt.figure(figsize=(10, 6))

  plt.rcParams['axes.prop_cycle'] = plt.cycler(color=plt.cm.tab20.colors)

  for key, series in dict.items():
    plt.plot(series, label=key)

  plt.xlabel('Year')
  plt.ylabel(ylab)
  plt.yscale('log')
  plt.legend()
  plt.grid(True)

def pie(series, n=10, title=""):
  top_labels = series.nlargest(n-1).index
  others_sum = series.loc[~series.index.isin(top_labels)].sum()

  plot_series = series.loc[top_labels]
  plot_series['others'] = others_sum

  plt.pie(plot_series, labels=plot_series.index, autopct='%1.1f%%')
  plt.axis('equal')

  plt.title(title)

def plot_(series_, ylab='Count'):
  plt.figure(figsize=(10, 6))

  for country in series_.columns:
    plt.plot(series_.index, series_[country], label=country)

  plt.xlabel('Year')
  plt.ylabel(ylab)
  plt.legend()
  plt.grid(True)

def show():
  plt.show()