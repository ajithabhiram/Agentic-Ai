"""
==========================================
Day 16 - Python Assert & Nested Loops

Topics:
1. Assert Statement
2. Nested Loops
3. Number Patterns
4. Alphabet Patterns
5. Star Patterns
==========================================
"""

# ==========================================
# 1. Assert Statement
# ==========================================

print("========== Assert Statement ==========")

number = int(input("Enter a Positive Number: "))

assert number > 0, "Please enter only a positive number."

number = number + 2

print("Updated Value:", number)

# ==========================================
# 2. Nested Loop Example
# ==========================================

print("\n========== Nested Loop Example ==========")

for row in range(3):
    for column in range(2):
        print(row, column)

# ==========================================
# 3. Number Pattern
# 1 2 3
# 1 2 3
# 1 2 3
# ==========================================

print("\n========== Number Pattern ==========")

for row in range(3):
    for value in range(1, 4):
        print(value, end=" ")
    print()

# ==========================================
# 4. Row Number Pattern
# 1 1 1
# 2 2 2
# 3 3 3
# ==========================================

print("\n========== Row Number Pattern ==========")

for row in range(1, 4):
    for column in range(3):
        print(row, end=" ")
    print()

# ==========================================
# 5. Alphabet Pattern
# A A A
# B B B
# C C C
# ==========================================

print("\n========== Alphabet Pattern ==========")

for letter in range(ord('A'), ord('D')):
    for repeat in range(3):
        print(chr(letter), end=" ")
    print()

# ==========================================
# 6. Sequential Number Pattern
# 1 2 3
# 4 5 6
# 7 8 9
# ==========================================

print("\n========== Sequential Number Pattern ==========")

count = 1

for row in range(3):
    for column in range(3):
        print(count, end=" ")
        count += 1
    print()

# ==========================================
# 7. Square Star Pattern (3 x 3)
# ==========================================

print("\n========== Square Star Pattern ==========")

for row in range(3):
    for column in range(3):
        print("*", end=" ")
    print()

# ==========================================
# 8. Rectangle Star Pattern (4 x 5)
# ==========================================

print("\n========== Rectangle Star Pattern ==========")

for row in range(4):
    for column in range(5):
        print("*", end=" ")
    print()

# ==========================================
# 9. Right Triangle Star Pattern
# *
# **
# ***
# ****
# ==========================================

print("\n========== Right Triangle Star Pattern ==========")

for row in range(1, 5):
    for star in range(row):
        print("*", end="")
    print()

# ==========================================
# End of Day 16
# ==========================================
