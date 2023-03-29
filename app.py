course = "Python Programming"
print(len(course))
print(course[-1])

import math
print(ord('b'))

# age = input("x:")
age = 22
message = "Eligible" if int(age) >= 18 else "Not Eligible"
print(message)

high_income = True
good_credit = True
student = False

if high_income and good_credit:
    print("candidate is eligible")
else:
    print("Not eligible")

if not student:
    print("not a student, so Eligible")

if (high_income or good_credit) and not student:
    print("or condition met")

if 18 <= age < 65:
    print("labour able")

for number in range(0, 20, 2):
    print("try to login", number, number * ".")

successful = False
for login in range(1, 4):
    print("enter passwd")
    if successful:
        print("authenticated")
        break
else:
    print("bad passwd, failed")

for x in range(5):
    for y in range(3):
        print(f"({x} {y})")

command = ""
while command.lower() != "quit":
    command = input(">")
    print("ECHO", command)

while True:
    command = input(">")
    print("ECHO", command)
    if command.lower() == "quit":
        break

def multi_user(*user):
    print(user)

multi_user("dan", "happy", "chi chi")


def save_user(**user):
    return user

save_user(id=1, wife = "happy", daughter = "chi chi")
user_1 = save_user(identity = 1, first_name = "Daniel", last_name = "Okoro")
print(user_1)

def multiply(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total


multiply(2,3,4)