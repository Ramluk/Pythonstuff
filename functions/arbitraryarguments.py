"""Example: Consider a function that builds a pizza. It has to accept
a number of toppings, but you can't know ahead of time how many toppings
people might want."""
"""def make_pizza(*toppings):
    #print list of toppings that have been requested
    print(toppings)

make_pizza('pepperoni','extra cheese', 'mushrooms')
make_pizza('black olives', 'hyena meat')"""

"""def make_pizza(*toppings):
    print("Making a pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")
make_pizza('pepperoni','extra cheese', 'mushrooms')
make_pizza('black olives', 'hyena meat')"""

#Mixing positional and arbitrary arguments
"""If you want a function to accept several different kinds of arguments,
the parameter that accepts an arbitrary # of arguments has to come last in the function definition"""
#If the above function also needs a pizza size
def make_pizza(size, *toppings):
    print(f"Making a {size} pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")
make_pizza('large', 'Onion', 'Pepperoni', 'Black Olive', 'Spinach')
make_pizza('small', 'Anchovies')
#You'll often see *args, a generic parameter name that collects arbitrary positional arguments.
