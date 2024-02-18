from functools import partial
from multiprocessing import Pool

import utils.firm as Firms

def process_chunk(chunk, old_map):
  new_map_chunk = {}

  for url in chunk:
    if url not in old_map:
      domain_created_year = Firms.get_domain_created_year(url)
      new_map_chunk[url] = domain_created_year

  return new_map_chunk

def merge_results(results):
  result_map = {}
  for result in results:
      result_map.update(result)
  return result_map

def get_domain_created_year_map(urls, domain_created_year_map, p=4, c=10):
  chunks = [urls[i:i+c] for i in range(0, len(urls), c)]

  partial_process_chunk = partial(process_chunk, old_map=domain_created_year_map)

  with Pool(p) as pool:
    results = pool.map(partial_process_chunk, chunks)

  # Merge results from all processes
  result_map = merge_results(results)

  domain_created_year_map.update(result_map)
  # print(domain_created_year_map)

  return domain_created_year_map