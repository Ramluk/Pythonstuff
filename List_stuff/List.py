pizzas = ['Pep','Mush','Veg']
for pizza in pizzas:
    print(f"{pizza.title()} is my fav")
print("Pep, Mush, Veg, you name it, I'll eat it!")
print("I just love pizza!")

# using multiple lists in an if statement
#pizza parlor
available_toppings = ['Pepperoni','Pineapple','Anchovies','Onion','Sausage']
requested_toppings = []
cust_request = 0
print("Mark's Pizzeria, what toppings can I get for ya?")
print("Whenever you're done entering toppings, just press enter!")
while cust_request != "":
    cust_request = input("Enter a topping here:")
    requested_toppings.append(cust_request)
    for requested_topping in requested_toppings:
        if requested_topping in available_toppings:
            print(f"adding {cust_request} to the list.")
        else:
            print("Sorry, we don't have that topping.")
print("So far I got this on your pizza:")
for i in requested_toppings:
    print(i)
print("Anything else I can get for ya?")
yesorno = input("Yes or No?")
if yesorno == "Yes":
    print("Too bad, thats it.")
else:
    print("Continuing")


