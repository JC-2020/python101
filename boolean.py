num = input('Give me a number? ')
num = int(num)

is_odd = num % 2 != 0
if is_odd:
    print(f'{num} is odd')
else:
    print(f'{num} is even')