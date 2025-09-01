#Dictionaries
#A dictionary in Python is a collection of key-value pairs

alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])
print(alien_0['points'])

#Removing Key-Value Pairs
del alien_0['points']
print(alien_0)

#A Dictionary of Similar Objects
favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
}

#Using get() to Access Values
point_value = alien_0.get('points', 'No point value assigned.')
print(point_value)
#Here we used get() as an exception handling

print('\n\n')

#Looping Through a Dictionary
user_0 = {
'username': 'efermi',
'first': 'enrico',
'last': 'fermi',
}
for key, value in user_0.items():
    print(f"\nKey: {key}")
    print(f"Value: {value}")

print('\n\n')

for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}.")

print('\n\n')

#Looping Through All the Keys in a Dictionary
for name in favorite_languages.keys():
    print(name.title())

print('\n\n')

#Looping Through a Dictionary’s Keys in a Particular Order
for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll.")


print('\n\n')

#Looping Through All Values in a Dictionary
print("The following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())
#To see each language chosen without repetition, we can use a set.
#A set is a collection in which each item must be unique:
print('\n\n')
for language in set(favorite_languages.values()):
    print(language.title())