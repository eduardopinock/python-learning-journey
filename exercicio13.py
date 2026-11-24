
try:
    name = input("Enter your name: ")

    if not name.replace(" ", "").isalpha():
        raise ValueError("Name must contain only letters.")

    print("Valid name:", name)

except ValueError as error:
    print("Invalid input:", error)