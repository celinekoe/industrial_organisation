import constants.tags as IndustryConstants

# Constants

def get_industry_group_industries(industry_group):
  return IndustryConstants.industry_group_industry_map[industry_group]

def get_industries():
  industries = [industry for industry_group_industries in IndustryConstants.industry_group_industry_map.values() for industry in industry_group_industries]
  industries = list(set(industries))
  return sorted(industries)

# Group

def get_grouped_count(firms, group):
  return firms.groupby(group).size()

def get_grouped_percent(firms, group):
  grouped_percent = firms.groupby(group).size() \
    .groupby(level=0).apply(lambda x: x / float(x.sum()) * 100) \
    .reset_index(level=0, drop=True) \
    .unstack()
  return grouped_percent

def get_year_count(firms):
  return get_grouped_count(firms, ['Founded Year'])

def get_public_year_count(firms):
  public_year_count = get_grouped_count(firms, ['Founded Year', 'Public Funded']) \
    .unstack() \
    .reset_index() \
    .set_index('Founded Year') \
    .rename(columns={False: 'Private Funded', True: 'Public Funded'})
  return public_year_count

def get_STEM_year_percent(firms):
  return get_grouped_percent(firms, ['Founded Year', 'Science'])

def get_public_year_percent(firms):
  return get_grouped_percent(firms, ['Founded Year', 'Public Funded'])

# Filter

def filter_industry_group(firms, industry_group):
  industry_group_firms = firms[firms['Tag Groups'].apply(lambda firm_industry_group: industry_group in firm_industry_group)]
  return industry_group_firms

def filter_industry(firms, industry):
  industry_firms = firms[firms['Tags'].apply(lambda firm_industry: industry in firm_industry)]
  return industry_firms

def filter_STEM(firms, STEM=True):
  return firms[firms['Science'].fillna(False) == STEM]

def filter_public_funded(firms, public=True):
  return firms[firms['Public Funded'].fillna(False) == public]