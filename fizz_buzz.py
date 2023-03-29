def fizz_buzz(number):
    if number % 5 == 0 and number % 3 == 0:
        return "fizzbuzz"
    if number % 3 == 0:
        return "fizz"
    if number % 5 == 0:
        return "Buzz"
    return number

test_digit = fizz_buzz(int(input("enter number to check:")))
print(test_digit)

