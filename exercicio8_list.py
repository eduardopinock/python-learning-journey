
# Exercise 8: Cubes of even integers
# Using for loop and list comprehension

# Get input from the user
import ast

input_list = ast.literal_eval(input("Enter a list: "))

# METHOD 1: Using for loop

cubes_for_loop = []

for item in input_list:

    if type(item) == int and item % 2 == 0:
        cubes_for_loop.append(item ** 3)

print("Cubes using for loop:", cubes_for_loop)


# METHOD 2: Using list comprehension

cubes_comprehension = [
    item ** 3
    for item in input_list
    if type(item) == int and item % 2 == 0
]

print("Cubes using list comprehension:", cubes_comprehension)
