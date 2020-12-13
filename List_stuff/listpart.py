#To work with a specific part of a list, you slice
#Slicing a list
#specify the index of the first and last element you want to work with, but as with the range function, it'll stop one before the 2nd index you specify.
players = ['charles','cindy','mike','kyla','florence','eli']
print(players[0:3]) #prints 0,1,2
#you can also do different sections
print(players[1:4]) #prints 1-3
#if you omit first index, it'll start at beginning of list
print(players[:5]) #prints first 5
#if you omit the last index, it'll print from the 1st index to the end of list
print(players[1:]) #prints from 2nd to end as first is 0
#remember a negative index returns elements from end of list
print(players[-3:]) #will print 3 in to end of list
#if you include a third value it'll speciifcy how many items to skip in that range
print(players[0::2])

print("The first 3 players are:")
for player in players[:3]:
    print(player.title())

#COPYING A LIST
my_foods = ['pizza','lamb','porkchops','guacamole']
friend_foods = my_foods[:]
print("My favorite foods are:")
print(my_foods)
my_foods.append("cannoli")
friend_foods.append("tuna")
print(friend_foods)
print(my_foods)


print("The first 3 items in the list are:")
print(my_foods[:3])
print("Three items from the middle of the list are:")
print(my_foods[1:4])
print("The last 3 items in the list are:")
print(my_foods[-3:])
for i in my_foods:
    print(i)
    
