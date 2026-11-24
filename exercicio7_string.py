
# Exercise 7: Find all occurrences of a substring

def find_occurrences(string1, string2):

    # Create an empty list to store the indexes
    indices = []

    # Check if the second string is empty
    if string2 == "":
        return -1

    # Initialize the starting position
    start = 0

    # Search for all occurrences
    while True:

        # Find the next occurrence
        index = string1.find(string2, start)

        # Stop if the substring is not found
        if index == -1:
            break

        # Store the index in the list
        indices.append(index)

        # Move to the next position
        start = index + 1

    # Return the result
    if len(indices) > 0:
        return indices
    else:
        return -1


# Get input from the user
string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")

# Call the function
result = find_occurrences(string1, string2)

# Display the result
print("Occurrences found at indexes:", result)
