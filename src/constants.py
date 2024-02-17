start_year = 1950
end_year = 2024 # 2024 is excluded
year_range = range(start_year, end_year)

top_count = 10
exclude_top_count = 11

asean = ['indonesia', 'malaysia', 'philippines', 'singapore', 'thailand', 'vietnam']

data_dir = '../data'
crunchbase_dir = f"{data_dir}/crunchbase"
crunchbase_country_dir = f"{crunchbase_dir}/country"
crunchbase_industry_dir = f"{crunchbase_dir}/industry"
ceic_dir = f"{data_dir}/ceic"
real_gdp_dir = f"{ceic_dir}/real_gdp"
fed_rate_dir = f"{ceic_dir}/fed_rate"
ceic_pop_dir = f"{ceic_dir}/population"

pickle_dir = '../pickle'

tag_groups = [
  'Administrative Services',
  'Advertising',
  'Agriculture and Farming',
  'Apps',
  'Artificial Intelligence (AI)',
  'Biotechnology',
  'Blockchain and Cryptocurrency',
  'Clothing and Apparel',
  'Commerce and Shopping',
  'Community and Lifestyle',
  'Consumer Electronics',
  'Consumer Goods',
  'Content and Publishing',
  'Data and Analytics',
  'Design',
  'Education',
  'Energy',
  'Events',
  'Financial Services',
  'Food and Beverage',
  'Gaming',
  'Government and Military',
  'Hardware',
  'Health Care',
  'Information Technology',
  'Internet Services',
  'Lending and Investments',
  'Manufacturing',
  'Media and Entertainment',
  'Messaging and Telecommunications',
  'Mobile',
  'Music and Audio',
  'Natural Resources',
  'Navigation and Mapping',
  'Other',
  'Payments',
  'Platforms',
  'Privacy and Security',
  'Professional Services',
  'Real Estate',
  'Sales and Marketing',
  'Science and Engineering',
  'Social Impact',
  'Software',
  'Sports',
  'Sustainability',
  'Transportation',
  'Travel and Tourism',
  'Video'
]

tag_group_science_map = {
  'Administrative Services': False,
  'Advertising': False,
  # 'Agriculture and Farming': True,
  'Agriculture and Farming': False,
  'Apps': False,
  'Artificial Intelligence (AI)': True,
  'Biotechnology': True,
  # 'Blockchain and Cryptocurrency': True,
  'Blockchain and Cryptocurrency': False,
  'Clothing and Apparel': False,
  'Commerce and Shopping': False,
  'Community and Lifestyle': False,
  # 'Consumer Electronics': True,
  'Consumer Electronics': False,
  'Consumer Goods': False,
  'Content and Publishing': False,
  # 'Data and Analytics': True,
  'Data and Analytics': False,
  'Design': False,
  'Education': False,
  'Energy': True,
  'Events': False,
  'Financial Services': False,
  'Food and Beverage': False,
  'Gaming': False,
  'Government and Military': False,
  'Hardware': True,
  # 'Health Care': True,
  'Health Care': False,
  # 'Information Technology': True,
  'Information Technology': False,
  'Internet Services': False,
  'Lending and Investments': False,
  # 'Manufacturing': True,
  'Manufacturing': False,
  'Media and Entertainment': False,
  # 'Messaging and Telecommunications': True,
  'Messaging and Telecommunications': False,
  'Mobile': False,
  'Music and Audio': False,
  # 'Natural Resources': True,
  'Natural Resources': False,
  # 'Navigation and Mapping': True,
  'Navigation and Mapping': False,
  'Other': False,
  'Payments': False,
  'Platforms': False,
  'Privacy and Security': False,
  'Professional Services': False,
  'Real Estate': False,
  'Sales and Marketing': False,
  'Science and Engineering': True,
  'Social Impact': False,
  'Software': False,
  'Sports': False,
  'Sustainability': True,
  'Transportation': False,
  'Travel and Tourism': False,
  'Video': False,
}