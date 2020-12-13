cars = ['audi','bmw','volvo','subaru','toyota']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

#conditional tests
#at the heart of every if statement is an expression that can be evaluated to true or false, a conditional test.
#equality is ==... = is assignment car = 'bmw' car  == 'bmw'
#equality is case sensitive
#test for inequality
requested_topping = 'mushrooms'
if requested_topping != 'anchovies':
    print("Hold the anchovies!")


#checking multiple conditions
age_0 = 32
age_1 = 18
age_0 >= 21 and age_1 >21 #evaluates to false
#you can also use or
age_0 >= 21 or age_1 >21
requested_toppings = ['mushrooms','onions','pineapple']
if 'mushrooms' in requested_topping:
    print('Mushrooms selected.')

    #checking if something is NOT in a list
banned_users = ['andrew','carolina','david']
user = 'marie'
if user not in banned_users:
    print(f"{user.title()}, you can post a response if you wish.")
#boolean
game_active = True
can_edit = False
for i in requested_toppings:
    if i == 'mushrooms' and 'pineapple':
        print('mush')

#if else (the else is optional)
age = 21
if age >=18:
    print("You're old enough to vote!")
else:
    print("Sorry kid, maybe next year.")
#else if, but in python it's if-elif-else
if age <4:
    print("your admission is free")
elif age < 18 and age >=4:
    print("Your admission is $25")
else:
    print("Your admission cost is $40.")

#more efficient way
if age < 4:
    price = 0
elif age >=4 and age <=18:
    price = 25
else:
    price = 40

print(f"Your price will be ${price}.")


alien_color = 'purple'
player = 'mark'
if alien_color == 'green':
    print(f"You just got 5 points, {player}!")
else:
    print(f"Sorry, {player.title()}! You'll get it right next time.")
