# ask user what would you like to do? Add, Print, Remove items
item_list = []

def add():
    while True:
        add_item = input("What would you like to add? ")
        item_list.append(add_item)
        feedback = input("Would you like to add more? ")
        if feedback.upper() == "NO" :
            break

def remove():
    while True :
        remove_item = input("What would you like to remove? ")
        item_list.remove(remove_item)
        feedback = input("Would you like to remove more? ")
        if feedback.upper() == "NO" :
            break

while True:
    user_input = input("What would you like to do? Add, Print, remove items? ")
#print(user_input.upper() == "ADD")
    if user_input.upper() == "ADD" :
        add() 
    elif user_input.upper() == "PRINT" :
        print(item_list)
    elif user_input.upper() == "REMOVE" :
        remove()