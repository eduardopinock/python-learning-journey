
# Program to swap the first n characters of two strings

# Taking input from the user
string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")

n = int(input("Enter the number of characters to swap: "))

# Checking whether n is valid
if n < 0 or n > min(len(string1), len(string2)):
    print("Invalid number of characters")

else:
    # Swapping the first n characters
    new_string1 = string2[:n] + string1[n:]
    new_string2 = string1[:n] + string2[n:]

    # Displaying the results
    print("String 1 after swapping:", new_string1)
    print("String 2 after swapping:", new_string2)
