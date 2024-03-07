country = 'united_states'

start_year = 1960
# start_year = 1994
end_year = 2024 # Exclusive
# end_year = 2019
year_range = range(start_year, end_year)
fudge_factor = 100
window_size = 3
min_count = 500 + fudge_factor

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