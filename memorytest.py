# Testing memory of past questions. Initial code only, optimisations/improvements to be made in new file
# No resources used.

# Weight Converter Kg to Lbs;
weight = float(input("How much do you weigh?: "))
units = input("And is that in (L)bs or (K)gs?: ")
if units == "K":
    print("That's "+str(weight * 2.20462)+" in lbs.")
elif units == "L":
    print("That's "+str(weight / 2.20462)+" in kg.")
else:
    print("Please give units in K or L...") # This needs to loop back!

# List 1 to 5 in as little code as possible
for number in range(1,6):
    print(number)

# \n in a string creates a new line!
# \" inside a string would negate the quotation mark from ending string prematurely

# Simple addition calculator
val_one = float(input("Enter the first value: "))
val_two = float(input("Enter the second value: "))
result = val_one + val_two # Could expand this with more input options to encompass different operations
print("Your total is: "+ str(result))

# suggest a word game
food = input("Enter an object: ")
number = input("Enter another, slightly weirder object: ")
father = input("Almost there: ")
son = input("Last one: ")
print("My favourite food is "+food)
print("My lucky number is "+number)
print("Like "+ father +" like "+ son + ".")

# Combine lists
list_1 = [1,1,2,3,5,8,13,21]
list_2 = [13,16,18,21,30,40]
list_1.extend(list_2)
list_1.insert(8,69)
print(list_1)