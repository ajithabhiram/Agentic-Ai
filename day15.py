'''
Day 15 Practice
Topics Covered:
1. While Loop
2. Password Validation
3. Limited Login Attempts
4. For-Else
5. Break
6. Continue
7. Pass
'''
print("========== While Loop Example ==========")
count = 1
while count <= 5:
    print("You can access the portal")
    names = []
    names.append("Codegnan")
    print(names)
    count += 1
print("\n========== Countdown ==========")
count = 5
while count >= 1:
    print("Count =", count)
    count -= 1
print("\n========== Password Validation ==========")
password = input("Enter Password: ")
while password != "admin":
    print("Incorrect Password")
    password = input("Enter Password Again: ")
print("Access Granted")
print("\n========== Login with 3 Attempts ==========")
attempt = 0
while attempt < 3:
    password = input("Enter Password: ")

    if password == "admin":
        print("Login Successful")
        break

    print("Incorrect Password")
    attempt += 1
else:
    print("Account Locked")

print("\n========== Product Search (For-Else) ==========")
store = ["mobile", "laptop", "powerbank", "charger"]
search = input("Enter Product Name: ").lower()
for item in store:
    if search == item:
        print("Product Found")
        break
else:
    print("Product Not Found")

print("\n========== Break Statement ==========")
for i in range(1, 11):
    if i == 6:
        break
    print(i)
print("\n========== Continue Statement ==========")

for ch in "codegnan":
    if ch == "g":
        continue
    print(ch)


print("\n========== Pass Statement ==========")

for i in range(5):
    pass

print("Pass statement executed successfully.")


print("\n========== Even Numbers using While ==========")

num = 2

while num <= 20:
    print(num, end=" ")
    num += 2


print("\n\n========== Sum of First 10 Numbers ==========")

i = 1
total = 0

while i <= 10:
    total += i
    i += 1

print("Sum =", total)
