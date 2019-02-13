first_name = "Reiko"
last_name = "Matsuki"

def password_generator(first_name,last_name):
  last_first = first_name[-3:]
  last_last = last_name[-3:]
  together = last_first + last_last
  return together

temp_password = password_generator(first_name,last_name)
print(temp_password)