Alien_color = 'Green'
player = input("Enter your name: ")
print(f"Welcome to the Alien Manifesto, {player}!")
print("\n \t It was a cold day in December,")
print("\t We had just finished a tour in Vietnam")
print("\t and my first day back to the states,")
print("\t I get abducted by aliens!")
print("\t Gee, what a trip it has been.")
print("Narrator: \t\n You wake up in a cell inside the ship you were abducted on...")
print("Narrator: \t\n You look around, no one seems to be nearby.")
print(f"{player}: \t\n \"Damn my ass is sore... What happened?\"")
print("Narrator: \t\n You have no recollection of anything since you were sucked up in a UFO beam. \n You begin to look around the room.")
print("Narrator: \t\n An alien appears from some sort of cosmic beam in front of your cell.")
print("Now's your chance, what do you want to do?")
choices = ['1. Run at the cell door and punch into that mushy sack in the aliens chest cavity area.','2. Continue sitting in the dark corner','3. Make gorilla noises']
for i in choices:
    print(i)
decision = input()
if decision == 1:
    print("You were shot by the alien.")
elif decision == 2:
    print("The alien says something incomprehensible, and then spits on you.")
else:
    print("You were moved to the cages with the gorillas, and dismembered by them.")






