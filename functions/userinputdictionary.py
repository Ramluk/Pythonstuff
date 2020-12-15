responses = {}

polling_active = True

name = input("\nWhat is your name? ")
response = input("Which mountain would you like to climb someday? ")

responses[name] = response

repeat = input("Would you like to let another person respond? (Yes/No) ")

if repeat == 'no':
    polling_active = False



print("\n--- Poll Results ---")
for name, response in responses.items():
    print(f"{name} would like to climb {response}.")

def greet_user():
    """Display a simple greeting."""
    print("Hello!")

greet_user()

