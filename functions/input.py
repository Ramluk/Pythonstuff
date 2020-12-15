#when using input() python takes it as a string
#you can change this input to int
age = input("How old are you? ")
age = int(age)
if age >= 18:
    print("test over or = 18")

#while loops
#for loop takes a collectio nof itemss and executes a block of code once for each item in the collection
#A while loop runs as long as a condition is true, or while it's true
#while loop to count 1-5
current_number = 1
while current_number <=5:
    print(current_number)
    current_number += 1

prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "Enter 'quit' to end the program. "

message = ""
while message != 'quit':
    message = input(prompt)
    print(message)
#if you're wanting to run a program to continue running, but there are multiple conditions that can stop the program you can use a variable
active = True
while active:
    message = input(prompt)

    if message == 'quit':
        active = False
    else:
        print(message)

prompt = "\nPlease enter the name of a city you have visited."
prompt += "\n(Enter 'quit' when you are finished.) "
#using break to exit loop
while True:
    city = input(prompt)

    if city == 'quit':
        break
    else:
        print(f"I'd love to go to {city.title()}!")

#while loop to print odd numbers
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue

    print(current_number)