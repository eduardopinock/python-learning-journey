text = input("Enter a string: ")
ch = input("Enter a character: ")

if len(ch) != 1:
    print("Please enter exactly one character")
else:
    # a. Frequency of a character
    print("a. Frequency of", ch, ":", text.count(ch))

    # b. Replace a character by another character
    new_ch = input("Enter the replacement character: ")
    print("b. After replacing:", text.replace(ch, new_ch))

    # c. Remove the first occurrence
    print("c. Without the first", ch, ":", text.replace(ch, "", 1))

    # d. Remove all occurrences
    print("d. Without any", ch, ":", text.replace(ch, ""))