#Task 1: Check if a Number is Even or Odd
#====================================
number = input("Enter a number:")
try:
    int(number)
    if int(number) % 2 == 0:
        print(number,' is an even number')
    else:
        print(number,' is an Odd number')
except ValueError:
    print("Entered value is not a number")








