def greet_user():
    """Display a simple greeting."""
    print("Hello!")

greet_user()

#passing info to a function
def greet_user(username):
    print(f"Hello, {username.title()}!")

greet_user('Mark')

#Arguments and Parameters
#The varialbe username is a parameter, the value passed ('Mark') is an argument. There is a difference.
#Passing Arguments
#Types: Positional Arguments, which need to be in the same order that the parameters were written.
#Keyword Arguments, where each argument consists of a variable name and a value; and lists and dictionaries of values.

#function that displays info about pets
        #says what kind of animal each pet is and the pet's name

def describe_pet(animal_type, pet_name):
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet("Koala","leonardo")
describe_pet("Gorilla","Jimmy")
#Remember, order matters in positional arguments.


#keyword argument is a name value pair you pass to a function.
#example
describe_pet(animal_type = 'hamster', pet_name='harry')
#animal_type is key, 'hamster' is value
#notice order of keyword doesn't matter as shown below
describe_pet(pet_name='John',animal_type='Beaver')

#You can set a default value as well.
def describe_person(name, hair_color, eye_color='Green'):
    print(f"Hi, I'm {name.title()}! My hair color is {hair_color.title()}, and my eye color is {eye_color.title()}")

describe_person(hair_color='yellow',name='Mike')

