def common_letters(string_one,string_two):
  return_list = []
  
  for x in string_one:
    for y in string_two:
      if (x == y):
        if (y not in return_list):
          return_list.append(y)
          
  return return_list

print(common_letters("manhattan pistachio", "sour cream onion"))