num = 0
while True:
    try:
        num = int(input('Give me a number: '))
        break
    except ValueError:
        print('Please try again')
print(f'You entered {num}')            