
import utils.file as File

class Country:
  def __init__(self, name):
    self.name = name
    self.firms = None
    self.tags = None
    self.tags_count = None
    self.tags_percent = None
    self.years_count = None
    self.tags_years_count = None
    self.tags_years_percent = None

  def set_firms(data, name):
    self.name = data

  def pickle(self):
    for name, value in vars(self).items():
      print(f"Attribute name: {attr_name}, value: {attr_value}")
      
      File.write_pickle(f"{name}", tags_years_percent)


