# Asks user for name
name = input ("Please enter first and last name? ").strip().title()

# removes whitspace from the variable so only text is there using a function but only removes the left of and right of the inputed text
#name = name.strip()

# capitalize first letter
#name = name.capitalize()

# will captalize the first letter of each word
#name = name.title()

# chain the functions on the string
#name = name.strip().title()

# split usersname using the split function will split into variables in order in string first word into first variable and so on
first, last = name.split()

# Says hello to user
print ("Hello,",name)

# Use end paramter for print change default end="\n" which would create new line end of each pring
print ("Hello,",end=" ")
print (name)

# use sep parameter for print change the default of sep=" " which creates a space between objects 
print ("Hello,",name, sep="Test")

# tells python speical string and formats differently so pulls out the variable between {}
print (f"Hello, {name}")

# print what there first name is and there last
print (f"Your first name is, {first}")
print (f"Your last name is, {last}")