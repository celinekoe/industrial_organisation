import matplotlib.colors as mcolors

import constants.industry as IndustryConstants
import constants.investor as InvestorConstants

def mid_color(color1, color2, alpha=0.5):
  color1_rgb = mcolors.to_rgb(color1)
  color2_rgb = mcolors.to_rgb(color2)
  mid_color = tuple((1 - alpha) * c1 + alpha * c2 for c1, c2 in zip(color1_rgb, color2_rgb))
  
  return mid_color

start_year = 1960
end_year = 2019
STEM_stack_labels = [IndustryConstants.not_STEM_label, IndustryConstants.STEM_label]
STEM_colors = ['lightgreen', 'green']
public_funded_stack_labels = [InvestorConstants.private_funded_label, InvestorConstants.public_funded_label]
public_funded_colors = ['lightblue', 'blue']
STEM_public_year_percent_colors = [mid_color('green','blue', 0.8), mid_color('lightgreen', 'blue', 0.8), 
                                   mid_color('green', 'lightblue', 0.8),  mid_color('lightgreen', 'lightblue', 0.8)]