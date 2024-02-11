
from utils.file import read_pickle
from utils.log import timer

import utils.viz as viz

@timer
def main():
  part_tags_percent = read_pickle("part_tags_percent")
  print(part_tags_percent['Biotechnology'])
  viz.plot_pie(part_tags_percent)
    
if __name__ == "__main__":
  main()