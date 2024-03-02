country = 'united_states'

start_year = 1960
end_year = 2020 # Exclusive
year_range = range(start_year, end_year)

min_count = 200
min_industries = 5

# Rolling AR
lag = 1
# window_size = 14 # window_size = r_0 * T, r_0 = 0.01 + 1.8/sqrt(T)
window_size = 3

ylim = (0, 1)
ylim_detailed = (-1, 2.5)