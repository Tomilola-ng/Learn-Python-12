"""
      Problem
      --------------
      # Create a function that receives a list and a function.
      # This function passed will return True or False if a list value is Odd.
      # The surrounding function will return a list of odd numbers.
"""

def is_odd(num: int):
  # Using Modulus to check if the number is Odd
  if num % 2 == 1:
    return True
  return False


def list_odd(func_is_odd, arg_list: []):
  odd_num_list = [] # List for Odd number

  for item in arg_list:
    if func_is_odd(item):
      odd_num_list.append(item)

  return odd_num_list

# Creating My List
my_list = [2,3,4,5,6,7,19,40,57,68] # Total of 5 Odd numbers, 10 Total numbers

# Calling the function now
print(list_odd(is_odd, my_list))
