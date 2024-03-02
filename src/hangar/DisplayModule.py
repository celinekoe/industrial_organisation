import config as Config
import utils.visualiser as Visualiser

class Display():
  def __init__():
    pass

  def report(self, macro):
    Visualiser.plot(self.trend, f'{self.frame} by {self.target_col}: Rolling AR({Config.lag}) Coef',
                    'ar coef', ylim=Config.ylim,
                    highlight_vertical=macro.recessions)      
 
  def detailed_report(self, macro):
    # for i, series in self.rolling_coef_map.items():
    #   mean = series.mean()
    #   Visualiser.plot(series, f'{self.frame}: {i}: Rolling AR({Config.lag}) Coef',
    #                   'ar coef', ylim=Config.ylim_detailed,
    #                   highlight_vertical=macro.recessions, highlight_horizontal=[mean])
    for i, series in self.year_count_growth_growth_map.items():
      mean = series.mean()
      Visualiser.plot(series, f'{self.frame}: {i}: Rolling AR({Config.lag}) Coef',
                      'ar coef', ylim=Config.ylim_detailed,
                      highlight_vertical=macro.recessions, highlight_horizontal=[mean])

            
  def sample(self, i, macro, detailed):
    Visualiser.plot(self.rolling_coef_map[i], f'{self.frame} by {self.target_col}: Rolling AR({Config.lag}) Coef', 'ar coef',
                    highlight_vertical=macro.recessions)

    if detailed:
      mean = self.year_count_share_map[i].mean()
      Visualiser.plot(self.year_count_share_map[i], f'{self.frame}: {i}: Count: Share', '%',
                      highlight_vertical=macro.recessions,  highlight_horizontal=[mean])
