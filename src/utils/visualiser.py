import matplotlib.pyplot as plt
import pandas as pd
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

def plot(series, title='', ylab='', ylim=None, highlight_vertical=None, highlight_horizontal=None, save=False):
  # plt.figure(figsize=(5, 3))
    
  plt.plot(series.index, series.values)

  if highlight_vertical:
    for year in highlight_vertical:
      plt.axvline(x=year, color='r', linestyle='--')

  if highlight_horizontal:
    for value in highlight_horizontal:
      plt.axhline(y=value, color='b', linestyle='--')

  plot_labels(plt, title, ylab, ylim)

  if save:
    plt.savefig(f'../report/plots/{title}.png')

  plt.show()

def plot_table(results, title='', save=False):
  # summary_table = model.summary().tables[1]
  # fig, ax = plt.subplots(figsize=(12, 8))
  # ax.axis('off')
  # ax.table(cellText=summary_table.data, colLabels=summary_table.columns, loc='center')
  # plt.savefig('../report/plots/{title}.png', bbox_inches='tight')
  coefficients = results.params
  std_errors = results.std_errors

  # Create a table
  table_data = pd.DataFrame({'Coefficient': coefficients, 'Std. Error': std_errors})
  table_data.index.name = 'Variables'

  # Save table as image
  fig, ax = plt.subplots(figsize=(8, 6))
  ax.axis('off')
  ax.table(cellText=table_data.values, colLabels=table_data.columns, rowLabels=table_data.index, loc='center')
  plt.savefig('panel_ols_summary.png', bbox_inches='tight')
  plt.show()