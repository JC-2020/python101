# create a list of number, print the largest of the numbers

import random

def is_it_an_integer():
    # while loop that goes until the user inputs an integer correctly
    while True:
        try:
            return int(input('> '))
        except ValueError:
            print('Invalid input, please enter an integer')
# prompt the user to get our upper bounds for a random num
# i.e. if the user inputs 5, then we could get a random number from 0 to 5
print('Input a number you want for the upper bounds of a random int')
user_input = is_it_an_integer()

# create our empty list
list_of_numbers = []

# for loop for our list
for index in range(0, list_length):
    # create a new random number
    # random_randint(a,b) returns a random integer that is between a and b
    random_number = random.randint(0, user_input)

    # append our random number
    list_of_numbers.append(random_number)

# initiate a variable that keeps track of the highest number is greatest
for numbers in list_of_numbers:
    # if the current number in the list is higher than highest_numb, then we assign that number to highest number
    if numbers > highest_numb:
        highest_numb = numbers

# print the variable highest_numb
print(f'Our list is:')
print(list_of_numbers)
print(f'The highest number in the list is: {highest_numb}')
