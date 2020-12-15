#A function doesn't always have to display its output directly.
#It can process and return a value or a set of values. This is called a return value.

#Let's look at a function that takes a first name, last name and returns a neatly formatted full name.
def get_formatted_name(first_name,last_name):
    full_name = f"{first_name} {last_name}"
    return full_name.title()

get_formatted_name('Mark','Ralph')

Musician = get_formatted_name('Jimi','Hendrix')
print(Musician)

#sometimes you'll want to make an argument optional. For instance if we wanted to take middle names, but not everyone has one.
def get_formatted_name2(first_name, last_name, middle_name=''):
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
        return full_name.title()
User = get_formatted_name2('John', 'Coltrane')
print(User)

#returning a dictionary
def build_person(first_name, last_name):
    """Return a dictionary of information about a person"""
    person = {'first': first_name, 'last': last_name}
    return person

musician = build_person('jimi','hendrix')
print(musician)

def build_person(first_name, last_name, age=None):
    person = {'first': first_name, 'last': last_name}
    
    if age:
        person['age'] = age
    return person
musicianed= build_person('jimi', 'hendrix', age=27)
print(musicianed)

while True:
    print("\nPlease tell me your name:")
    print("(enter 'q' at any time to quit.)")
    f_name = input("First name: ")
    if f_name == 'q':
        break
    l_name = input("Last Name: ")

    formatted_name = get_formatted_name(f_name,l_name)
    print(f"\nHello, {formatted_name}!")

def greet_users(names):
    for name in names:
        msg = f"Hello, {name.title()}!"
        print(msg)

usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)

unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

while unprinted_designs:
    current_design = unprinted_designs.pop()
    print(f"Printing model: {current_design}")
    completed_models.append(current_design)

print("\nThe following models have been printed:")
for completed_model in completed_models:
    print(completed_model)

"""Good way to reorganize this code is by writing two functions: each of which does one specific job.
Most of the code won't change; we're just making it more carefully structured. First function will
handle printing the designs, the second will summarize the prints that have been made."""

def print_models(unprinted_designs, completed_models):
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)

def show_completed_models(completed_models):
    print("\n The following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)

unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []
print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)

