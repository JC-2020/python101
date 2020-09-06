ramit = {
  'name': 'Ramit',
  'email': 'ramit@gmail.com',
  'interests': ['movies', 'tennis'],
  'friends': [
    {
      'name': 'Jasmine',
      'email': 'jasmine@yahoo.com',
      'interests': ['photography', 'tennis']
    },
    {
      'name': 'Jan',
      'email': 'jan@hotmail.com',
      'interests': ['movies', 'tv']
    }
  ]
}
# gets the email address of Ramit
name = ramit['email'] 
print(name)

# gets the first of Ramit's interests
interest = ramit['interests'][0]
print(interest)

# gets the email address of Jasmine
email_of_jasmine = ramit['friends'][0]['email']
print(email_of_jasmine)

# gets the second of Jan's two interests
two_interests_of_jan = ramit['friends'][1]['interests'][1]
print(two_interests_of_jan)
