import utils.location as LocationUtils
import utils.string as StringUtils

from constants.investors import public_investor_types, public_investors

def get_public(investor_type):
  investor_types = StringUtils.string_to_list(investor_type)
  for investor_type in investor_types:
    if investor_type in public_investor_types :
      return True

  return False

def enrich(investors):
  investors['Country'] =  investors['Location'].apply(LocationUtils.get_country)
  investors['Public'] = investors['Investor Type'].apply(get_public)

  return investors

def get_public_investors(investors):
  public_investors = investors.loc[investors['Public'], 'Organization/Person Name']
  return public_investors