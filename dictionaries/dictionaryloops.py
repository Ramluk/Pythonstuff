user_0 = {
    'username': 'jumanji',
    'first_name': 'Daniel',
    'last_name': 'Creed',
}
#can also just use k,v instead of key,value
for key, value in user_0.items():
    print(f"\nKey: {key}")
    print(f"Value: {value}")
#items() returns a list of key-value pairs
#looping through keys
for i in user_0.keys():
    print(i.title())
#this is actually default behavior as seen below
for i in user_0:
    print(i)
favorite_languages = {
    'jen': 'Python',
    'Derrick': 'Javascript',
    'Jamal': 'C#',
    'Tamisha': 'Ruby',
    'Tim': 'oCaml',
    'Joshua': 'Python',
}
friends = ['jen', 'Jamal']
for name in favorite_languages:
    print(f"What's up, {name.title()}!")
    if name in friends:
        language = favorite_languages[name].title() #pulls value from name
        print(f"\t{name.title()}, I see you love {language}!")

if 'erin' not in favorite_languages.keys(): #.keys() is optional
    print("Erin, please take our poll!")


#looping through in a particular order
for name in sorted(favorite_languages):
    print(f"\n{name}, thank you for taking the poll!")

#if you're interested more in looping through values than keys...
#you can use the values() method
print("\n\tNow that the poll is over, the following values have been mentioned:")
for language in favorite_languages.values():
    print(language.title())
print("\n\nUsing set & sorted")
#to avoid data redundancy, we can use a set. A set is a collection in which each item must be unique.
for language in set(sorted(favorite_languages.values())):
    print(language.title()) 

#you can automatically generate a set similar to a dictionary, but notice no :
languages = {'python', 'ruby', 'javascript', 'ruby'}
print(languages)
