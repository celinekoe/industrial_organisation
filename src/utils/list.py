def get_top_p(dict, p):
  total = sum(dict.values())

  run_list = []
  run_total = 0
  for key, value in dict.items():
    run_list.append(key)

    run_total += value
    run_p = run_total / total * 100
    if run_p > p:
      break

  return run_list
