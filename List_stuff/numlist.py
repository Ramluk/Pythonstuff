for value in range(1,5): #this prints 1-4, off by one. It stops at second value you give
    print(value)

#you can also just pass one value, and it'll print from 0
range(6)
#use range to make a list of #'s
numbers = list(range(1,6))
print(numbers) #prints list 1-5 [1,2,3,4,5]
#For range, you can also tell python to skip numbers
#in a given range. If you pass a 3rd argument it'll 
#use it as a step size.
even_numbers = list(range(2,12,2))
print(even_numbers)
squares = []
for value in range(1,11):
    square = value ** 2
    squares.append(square)
print(squares)
#different way to do it.
square_easier = []
for value in range(1,11):
    square_easier.append(value**2)
print(square_easier)

digits = list(range(0,240))
print(digits)
print(min(digits))
print(max(digits))
print(sum(digits))

