from list import access


try:
    age = int(input("enter Age:"))
    print(f"you are {age} years old")
except (ValueError, ZeroDivisionError):
    print("you didn't enter a valid age ")
else:
    print("no exceptions caught")

from timeit import timeit

code1 = """
def classify_age(age):
    if age <= 0:
        raise ValueError("Age can not be less than or equal to zero")
    return age/10


try:
    classify_age(-1)
except ValueError as err:
    pass
"""


code2 = """
def classify_age(age):
    if age <= 0:
        return None
    return age/10


xfactor = classify_age(-1)
if xfactor == None:
    pass
"""

print("first code", timeit(code1, number=10000), timeit(code2, number=10000))
