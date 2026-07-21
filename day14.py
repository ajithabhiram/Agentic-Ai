'''
Day 14 Practice
Topics Covered:
1. Type Conversions
2. Input Formatting using eval()
3. For Loop
4. Sum and Average
5. Sum of Numeric Values in a Mixed List
6. Dictionary Iteration
7. Range Function
8. Daily Workout Log
'''
print("========== Type Conversions ==========")
age = [23, 21, 43]
print("Original List:", age)
print("String:", str(age))
print("Tuple:", tuple(age))
print("Set:", set(age))
print("Dictionary:", dict.fromkeys(age))
name = "codegnan"
print("\nOriginal String:", name)
print("List:", list(name))
print("Tuple:", tuple(name))
print("Set:", set(name))
print("Dictionary:", dict.fromkeys(name))
print("\n========== Input Formatting ==========")
data = eval(input("Enter a list: "))
print(data)
print(type(data))
data1 = eval(input("Enter a tuple: "))
print(data1)
print(type(data1))

details = eval(input("Enter student details (dictionary): "))
print(details)
print(type(details))

print("\n========== Sum and Average ==========")

marks = list(map(int, input("Enter the marks separated by commas: ").split(',')))

total = 0

for mark in marks:
    total = total + mark

average = total / len(marks)

print("Sum of marks:", total)
print("Average of marks:", average)


print("\n========== Sum of Numeric Values ==========")

mixed_list = eval(input("Enter a mixed list: "))

sum_values = 0

for item in mixed_list:
    if type(item) == int or type(item) == float:
        sum_values = sum_values + item

print("Sum of numeric values:", sum_values)


print("\n========== Dictionary Iteration ==========")

student = {
    "Names": ["Sai", "Abhi", "Ram"],
    "Marks": [24, 20, 28]
}

print("\nKeys:")
for key in student:
    print(key)

print("\nValues:")
for value in student.values():
    print(value)

print("\nKeys and Values:")
for key, value in student.items():
    print(key, ":", value)


print("\n========== Range Function ==========")

print("Range(5)")
for i in range(5):
    print(i, end=" ")

print("\n")

print("Range(1,11)")
for i in range(1, 11):
    print(i, end=" ")

print("\n")

print("Range(1,11,2)")
for i in range(1, 11, 2):
    print(i, end=" ")

print("\n")

print("Reverse Order")
for i in range(10, -1, -2):
    print(i, end=" ")


print("\n\n========== Daily Workout Log ==========")

work_log = [1, 1, 1, 0, 1, 1, 0]

longest_streak = 0
count = 0

for day in work_log:
    if day == 1:
        count = count + 1
        if count > longest_streak:
            longest_streak = count
    else:
        count = 0

print("Longest Workout Streak:", longest_streak)
