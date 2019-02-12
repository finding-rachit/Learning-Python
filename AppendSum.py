def append_sum(lst):
  for x in range(0,3):
    last = lst[-1]
    s_last = lst[-2]
    add = last + s_last
    lst.append(add)
  return lst

print(append_sum([1, 1, 2]))