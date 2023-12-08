"""
    # Problem
    ----------------------
    # Find the multiples of 9 from a random 100 value list with values between 1 and 1000
"""

# Import module for randomizing
import random

# Generate random 100 value list
random_list = []

for i in range(100):
  random_list.append(random.randint(1, 1001))

def is_multiple_of_9(num: int):
  if num % 9 == 0:
    return True
  return False

result_list = []

for item in random_list:
    if is_multiple_of_9(item):
        result_list.append(item)
    
print(result_list)
