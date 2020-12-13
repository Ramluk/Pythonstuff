#Allows you to generate a list with for loop and creation of new elements into one line, and automatically appends each new element.

#old way we did it.
squares = []
for value in range(1,11):
    square = value ** 2
    squares.append(square)
print(squares)

#new way
newSquare =[value**2 for value in range(1,11)]
print(newSquare)

twentyCount = [value for value in range(1,21)]
print(twentyCount)
onemilli = [value for value in range(1,1000001)]
#print(onemilli)
print(min(onemilli))
print(max(onemilli))
print(sum(onemilli))
odd_numbers = [value for value in range(1,20,2)]
print(odd_numbers)
threes = [i for i in range (3,31) if i % 3 == 0]
print(threes)

cubes = [i**3 for i in range(1,11)]
print(cubes)