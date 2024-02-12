
from utils.file import read_pickle
from utils.logger import timer

import utils.vis as vis

@timer
def main():
  part_tags_percent = read_pickle("part_tags_percent")
  print(part_tags_percent['Biotechnology'])
  vis.plot_pie(part_tags_percent)
    
if __name__ == "__main__":
  main()