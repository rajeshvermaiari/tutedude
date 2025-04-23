#Task 1: Calculate Factorial Using a Function
#============================================
from math import factorial


def factorial(num):
    final_factorial_result = 1
    if num < 2:
        return 1
    #for i in range(num):
    while 1 < num:
        final_factorial_result = int(final_factorial_result) * int(num)
        num -= 1
    return final_factorial_result

value = input("Enter a number:")
print("Factorial of", value, " is", factorial(int(value)))
