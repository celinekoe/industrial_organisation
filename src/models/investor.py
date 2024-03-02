import constants.investor as Constants
import constants.labels as Labels

import utils.datatype as dtUtils
import utils.location as LocUtils

def _get_public_funded(investor_types, public_investor_types):
  for investor_type in investor_types:
    if investor_type in public_investor_types:
      return True

  return False

def enrich(investors):
  investors[Labels.country] =  investors[Labels.investor_location].apply(LocUtils.get_country)
  investors[Labels.investment_stage] = investors[Labels.investment_stage].apply(dtUtils.string_to_list)
  investors[Labels.investor_type] = investors[Labels.investor_type].apply(dtUtils.string_to_list)
  investors[Labels.public_funded] = investors[Labels.investor_type].apply(_get_public_funded, args=(Constants.public_investor_types,))

  return investors

def get_public_funded_investors(investors):
  public_investors = investors.loc[investors[Labels.public_funded], Labels.investor_name]
  return public_investors.tolist()