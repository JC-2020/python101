def is_odd(number):
    if (number %1 == 0):
        return True
    else:
        return False

is_number_odd = is_odd (inp(input("Enter a number" )))
    if is_number_odd:
        print("number is odd!")
    else:
        print("number is even")

