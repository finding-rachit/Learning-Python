def list_plus_one(lst):
  new_lst = []
  
  for item in lst:
    new_lst.append(str(item))

  join_string = ''.join(new_lst)
  join_int = int(join_string) + 1

  return_string = str(join_int)
  return_lst = []
  for x in return_string:
    return_lst.append(int(x))

  return return_lst

print(list_plus_one([1,9,9,9]))