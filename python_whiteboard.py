# set user number input
number = int(input("Select a number to count" ))

# print out all numbers from 1 to that number
for test in range(1, number):
    if test % 3 == 0 :
        print("fizz")
    elif test % 5 == 0:
        print("buzz")
    elif test % 3 == 0 and test % 5 == 0:
        print("fizzbuzz")
    else:
        print(test)