"""
    # Problem
    ----------------------------
    # Create a random list filled with characters H and T for Heads and Tails
    # Output the number of Hs and Ts
    ----------------------------
    # Example Output : 
    # Heads : 54
    # Tails : 46
"""

#  Import this for Randomizing
import random

# Create an empty list
my_list = []

for i in range(1, 101):
  my_list.append(random.choice(["H", "T"]))

print("Heads : ", my_list.count("H"))
print("Tails : ", my_list.count("T"))
