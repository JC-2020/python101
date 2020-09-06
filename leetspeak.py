user_input = input('Enter phase: ')
user_input = user_input.upper()
translation = ''
for phase in user_input:
    if phase == 'A':
        translation += '4'
    elif phase == 'E':
        translation += '3'
    elif phase == 'G':
        translation += '6'
    elif phase == 'I':
        translation += '1'
    elif phase == 'O':
        translation += '0'
    elif phase == 'S':
        translation += '5'
    elif phase == 'T':
        translation += '7'
    else:
        translation += phase
print(translation)