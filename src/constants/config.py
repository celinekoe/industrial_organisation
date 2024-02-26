start_year = 1960
end_year = 2020 # Exclusive
year_range = range(start_year, end_year)

count_threshold = 200
growth_threshold = 3

p_accept_threshold = 0.9
p_reject_threshold = 0.05

min_industries = 5
window_size = 14 # window_size = r_0 * T, r_0 = 0.01 + 1.8/sqrt(T)
window_overlap = int(window_size / 2)