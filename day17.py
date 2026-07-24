# Number Pattern
n = int(input("Enter n for Number Pattern: "))

for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()
print()
# Alphabet Pattern
n = int(input("Enter number of rows for Alphabet Pattern: "))
for i in range(n):
    for j in range(i + 1):
        print(chr(ord('A') + j), end=" ")
    print()
print()
# Right-Aligned Star Pattern
n = int(input("Enter n for Star Pattern: "))
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if j <= n - i:
            print(" ", end="")
        else:
            print("*", end=" ")
    print()
print()
# Diamond Pattern
n = int(input("Enter n for Diamond Pattern (odd number): "))
# Upper half
for i in range(1, n + 1):
    for j in range(n - i):
        print(" ", end="")
    for j in range(i):
        print("*", end=" ")
    print()
# Lower half
for i in range(n - 1, 0, -1):
    for j in range(n - i):
        print(" ", end="")
    for j in range(i):
        print("*", end=" ")
    print()
