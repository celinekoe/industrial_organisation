import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import pandas as pd

def plot(series, ylab):
  plt.figure(figsize=(10, 6))
  
  plt.plot(series.index, series.values)
    
  plt.xlabel('Year')
  plt.ylabel(ylab)
  plt.grid(True)

def plot_stacked():
  return

def plot_labels_years_(labels_years_, val_label):
  plt.figure(figsize=(10, 6))
  
  for label, years_ in labels_years_.items():
    years = list(years_.keys())
    values = list(years_.values())
    plt.plot(years, values, marker='o', label=label)
    
  plt.xlabel('Year')
  plt.ylabel(val_label)
  plt.legend()
  plt.grid(True)

def plot_tag(tag, tag_, title=None):
  plt.figure(figsize=(10, 6))
  
  years = list(tag_.keys())
  percents = list(tag_.values())
  plt.plot(years, percents, marker='o', label=tag)

  if title:
    plt.title(title)
    
  plt.xlabel('Year')
  plt.ylabel('Percent')
  plt.legend()
  plt.grid(True)

def plot_years(years_, label, val_label):
  plt.figure(figsize=(10, 6))
  
  years = list(years_.keys())
  values = list(years_.values())
  plt.plot(years, values, marker='o', label=label)
    
  plt.xlabel('Year')
  plt.ylabel(val_label)
  plt.legend()
  plt.grid(True)

def bar(series, title="", ylabel=""):
  plt.bar(series)

  plt.title(title)
  plt.xlabel('Categories')
  plt.ylabel(ylabel)

def pie(series, n=10, title=""):
  top_labels = series.nlargest(n-1).index
  others_sum = series.loc[~series.index.isin(top_labels)].sum()

  plot_series = series.loc[top_labels]
  plot_series['others'] = others_sum

  plt.pie(plot_series, labels=plot_series.index, autopct='%1.1f%%')
  plt.axis('equal')

  plt.title(title)

def plot_two(series1, series2, ylab='Count'):
  plt.figure(figsize=(10, 6))
  
  plt.plot(series1.index, series1.values)
  plt.plot(series2.index, series2.values)
    
  plt.yscale('log')

  plt.xlabel('Year')
  plt.ylabel(ylab)
  plt.legend()
  plt.grid(True)

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