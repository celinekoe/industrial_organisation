import matplotlib.pyplot as plt

def plot_tags(tags_, title):
  plt.figure(figsize=(10, 6))
  
  for tag, years_ in tags_.items():
    years = list(years_.keys())
    percents = list(years_.values())
    plt.plot(years, percents, marker='o', label=tag)

  if title:
    plt.title(title)
    
  plt.xlabel('Year')
  plt.ylabel('Percent')
  plt.legend()
  plt.grid(True)
  plt.show()

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
  plt.show()