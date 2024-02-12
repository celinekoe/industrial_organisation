start_year = 1950
end_year = 2024 # 2024 is excluded
year_range = range(start_year, end_year)

top_count = 10
exclude_top_count = 11

asean = ['indonesia', 'malaysia', 'philippines', 'singapore', 'thailand', 'vietnam']

data_dir = 'data'
crunchbase_dir = f"{data_dir}/crunchbase"
crunchbase_country_dir = f"{crunchbase_dir}/country"
crunchbase_industry_dir = f"{crunchbase_dir}/industry"
ceic_dir = f"{data_dir}/ceic"
ceic_gdp_dir = f"{ceic_dir}/real_gdp"
ceic_fed_rate_dir = f"{ceic_dir}/fed_rate"
ceic_pop_dir = f"{ceic_dir}/population"

pickle_dir = 'pickle'
