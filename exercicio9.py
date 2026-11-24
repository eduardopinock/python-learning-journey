
# Read the file name from the user
file_name = input("Enter the file name: ")

# Read the contents of the file
with open(file_name, "r", encoding="utf-8") as file:
    content = file.read()

# a. Count characters, words and lines
characters = len(content)
words = content.split()
lines = content.splitlines()

print("\n--- File Information ---")
print("Total characters:", characters)
print("Total words:", len(words))
print("Total lines:", len(lines))

# b. Calculate the frequency of each character
frequency = {}

for character in content:
    frequency[character] = frequency.get(character, 0) + 1

print("\n--- Character Frequency ---")
print(frequency)

# c. Print words in reverse order
print("\n--- Words in Reverse Order ---")
print(" ".join(words[::-1]))

# d. Copy even lines to File1 and odd lines to File2
with open("File1", "w", encoding="utf-8") as file1:
    with open("File2", "w", encoding="utf-8") as file2:

        for line_number, line in enumerate(lines, start=1):
            if line_number % 2 == 0:
                file1.write(line + "\n")
            else:
                file2.write(line + "\n")

print("\nFile1: Even lines copied successfully.")
print("File2: Odd lines copied successfully.")
