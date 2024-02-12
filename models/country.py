
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

  def set_firms(self, firms):
    self.firms = firms

  def set_tags(self, tags):
    self.tags = tags

  def set_tags_(self, tags_count, tags_percent):
    self.tags_count = tags_count
    self.tags_percent = tags_percent

  def set_years_(self, years_count):
    self.years_count = years_count

  def set_tags_years_(self, tags_years_count, tags_years_percent):
    self.tags_years_count = tags_years_count
    self.tags_years_percent = tags_years_percent
  
  def pickle(self):
    for name, value in vars(self).items():
      if name != 'name':
        File.write_pickle(f"{self.name}_{name}", value)

  def unpickle(self):
    for name, value in vars(self).items():
      if name != 'name':
        new_value = File.read_pickle(f"{self.name}_{name}")
        setattr(self, name, new_value)


