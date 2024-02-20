
import constants.funding as FundingConstants
import constants.visual as VisualConstants

import utils.dataframe as DataUtils
import visual.visualiser as Visualiser

def stack_STEM_public_funded(funding):
  funding_STEM_year_sum_percent = DataUtils.get_STEM_year_percent(funding, FundingConstants.year_label, FundingConstants.raised_label)
  funding_public_year_sum_percent = DataUtils.get_public_funded_year_percent(funding, FundingConstants.year_label, FundingConstants.raised_label)
  funding_STEM_public_funded_year_sum_percent = DataUtils.get_STEM_public_year_percent(funding, FundingConstants.year_label, FundingConstants.raised_label)

  Visualiser.stack(funding_STEM_year_sum_percent,
                   'STEM Funding: Sum: Percent', '%',
                   VisualConstants.STEM_stack_labels,
                   colors=VisualConstants.STEM_colors,
                   year_start=1990)
  Visualiser.stack(funding_public_year_sum_percent,
                   'Public Funding: Sum: Percent', '%',
                   VisualConstants.public_funded_stack_labels,
                   colors=VisualConstants.public_funded_colors,
                   year_start=1990)
  Visualiser.stack(funding_STEM_public_funded_year_sum_percent,
                   'STEM Public Funding: Sum: Percent', '%',
                   ['Not STEM Private Funding', 'STEM Private Funding', 'Not STEM Public Funding', 'STEM Public Funding'],
                   colors=VisualConstants.STEM_public_year_percent_colors,
                   year_start=1990)