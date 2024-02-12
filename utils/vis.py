import matplotlib.pyplot as plt

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

def plot_bar(keys, values, title="", ylabel=""):
  plt.bar(keys, values)

  plt.title(title)
  plt.xlabel('Categories')
  plt.ylabel(ylabel)

def plot_pie(key_values, title=""):
  keys = list(key_values.keys())
  values = list(key_values.values())

  plt.pie(values, labels=keys, autopct='%1.1f%%')
  plt.axis('equal')
  plt.title(title)

def show():
  plt.show()