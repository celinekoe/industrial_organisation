import utils.location as LocationUtils
import utils.common as StringUtils

from constants.investor import public_investor_types, public_investors

def get_public_funded(investor_types, public_investor_types):
  for investor_type in investor_types:
    if investor_type in public_investor_types:
      return True

  return False

def enrich(investors):
  investors['Country'] =  investors['Location'].apply(LocationUtils.get_country)
  investors['Investor Type'] = investors['Investor Type'].apply(StringUtils.string_to_list)
  investors['Investment Stage'] = investors['Investment Stage'].apply(StringUtils.string_to_list)
  investors['Public Funded'] = investors['Investor Type'].apply(get_public_funded, args=(public_investor_types,))

  return investors

def get_public_funded_investors(investors):
  public_investors = investors.loc[investors['Public Funded'], 'Organization/Person Name']
  return public_investors.tolist()