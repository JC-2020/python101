# Ask the user for their cat's age

cat_age = input('How old is your cat? ')

# Covert to an integer
cat_age = int(cat_age)

# Print one message if it's a kitten, otherwise do nothing
if cat_age < 2:
    print('What a cute kitten!')
elif cat_age < 9:
    print('What a big cat!')
else:
    print('What an old cat!')
