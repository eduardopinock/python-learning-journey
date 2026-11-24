
# Original tuple
t1 = (1, 2, 5, 7, 9, 2, 4, 6, 8, 10)

# a. Print half the values in two lines
middle = len(t1) // 2

print("First half:", t1[:middle])
print("Second half:", t1[middle:])

# b. Create another tuple with even numbers
even_numbers = tuple(num for num in t1 if num % 2 == 0)

print("Even numbers:", even_numbers)

# c. Concatenate t2 with t1
t2 = (11, 13, 15)

t3 = t1 + t2

print("Concatenated tuple:", t3)

# d. Find maximum and minimum values
print("Maximum value:", max(t3))
print("Minimum value:", min(t3))
