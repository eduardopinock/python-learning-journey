# Accept a number n and compute the sum 1 + 2 + ... + n

n = int(input("Enter a number n: "))

total = 0
for i in range(1, n + 1):
    total += i

print("Sum =", total)