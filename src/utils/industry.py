import constants.industry as Constants

def get_industry_groups():
  return list(Constants.industry_group_industry_map.keys())

def get_industries():
  industries = [industry for industry_group_industries in Constants.industry_group_industry_map.values() for industry in industry_group_industries]
  industries = list(set(industries))
  return sorted(industries)