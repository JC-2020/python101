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

#hotel = [hotel1, hotel2, hotel3]
#def print_status()
#for hotel in hotels:
 #   for key in hotel.keys()
  #  if hotel[key]:
   #     print(f'{key} Guest name: {hotel[key]['guest']['name']}.')
    #    else:
     #       print(f'Room {key} is empty.')

while True:
    user_input = int(input("""\nMain Menu
    \nWhat would you like to do?
    \n[1] Print hotel room status
    \n[2] Check in customer
    \n[3] Check out customer
    \n[4] Quit\n>"""))
    print(user_input)
    if user_input == 1:
        print(status)