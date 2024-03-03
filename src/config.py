country = 'united_states'

window_size = 3

start_year = 1960
# start_year = 1990
start_year = start_year - window_size + 1 # Include window
end_year = 2020 # Exclusive
year_range = range(start_year, end_year)

# Panel
const_exog_label = 'const'
entity_label = 'entity'
entity_exog_label = 'industry'
time_label = 'time'
time_exog_label = 'year'
time_exog_norm_label = 'year_norm'
p_value = 0.05

ylim = (0, 1)
ylim_detailed = (-1, 2.5)