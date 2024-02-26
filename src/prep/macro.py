import constants.dirs as DirConstants
import utils.file as FileUtils

def prep_real_gdp():
  real_gdp = FileUtils.read_real_gdp(DirConstants.real_gdp_dir)

  FileUtils.write_pickle(f"real_gdp", real_gdp)

def prep_real_gdp_growth():
  real_gdp_growth = FileUtils.read_real_gdp(DirConstants.real_gdp_growth_dir)

  FileUtils.write_pickle(f"real_gdp_growth", real_gdp_growth)

def prep_fed_rate():
  fed_rate = FileUtils.read_fed_rate(DirConstants.fed_rate_dir)
  FileUtils.write_pickle(f"fed_rate", fed_rate)
