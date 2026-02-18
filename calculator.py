#x = input("Please enter your first number? ")
#y = input("Please enter your second number? ")

# using int() we convert the the variable provided to an integer only work if enter a number
#z = int(x) + int(y)

x = float(input("Whats the first number? "))
y = float(input("Whats the second number? "))

z = round(x + y)

# by putting that , 2 it will round to the given decimal points so in this instance 2
a = round(x / y, 2)

print("Your exact result is:",x + y)
print("Your closet number is:", z)
print(f"In money money notation: {z:,}")
print("Result of dividing:", a)

# uses the f string and says only use to 2 decimal places
print(f"{z:.2f}")