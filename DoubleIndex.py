def double_index(lst,index):
  try:
    value = lst[index]
    print(value)
    lst[index] = value*2
  except IndexError:
    return lst
  return lst

print(double_index([3, 8, -10, 12], 2))