hotel = {
     '101': {
        'guest': {
            'name': 'Elliot Alderson',
            'phone': 8675309
        }
    },
    '102': {},
    '103': {},
    '104': {
        'guest': {
            'name': 'Darlene Alderson',
            'phone': 4567890
         }
    },
    '105': {},
}
# check if a room is occupied
def is_vacant(which_hotel, rooms):
    if 'guest' in which_hotel[rooms]:
        return True
    else:
        return False

new_guest = {
    'guest': {
        'name':'derek',
        'phone':8923
    }
}

def check_in(rooms, guest_dictionary):
    if is_vacant(hotel, rooms):
        print('pick a different room')
    else:
        hotel[rooms] = guest_dictionary
        print(hotel[rooms],rooms)

print(is_vacant(hotel, '102'))

check_in('102','derek')
print(hotel)

# create a function for check out

def check_out(rooms):
    if is_vacant:
        hotel[rooms]=''
        return hotel
    else:
        print('blah') 
        
check_out ('102')