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
list_1 = [1,1,2,3,5,8,13,21] # Tuple would use ()
list_2 = [13,16,18,21,30,40]
list_1.extend(list_2)
list_1.insert(8,69)
print(list_1)

# Functions refresher
def rp1(): # Define
    print("Ready player one")
# Call
rp1()
# Little more;
def rp2(name):
    print("Ready "+name)
rp2("Player Two")
rp2(input("What is your name? "))

def cube(num):
    return (num*num*num)
print(cube(3)) # Consider storing value as variable print(result)

def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        result = num1
    elif num2 >= num1 and num2 >= num3:
        result = num2
    else:
        result = num3
    return result
print(max_num(2,6,7))

# Dictionary basics - KVP example
monthConversions = {
    "Jan":"January",
    "Feb":"February",
    "Mar":"March",
    "Apr":"April",
    "May":"May",
    "Jun":"June",
    "Jul":"July",
    "Aug":"August",
    "Sep":"September",
    "Oct":"Octcber",
    "Nov":"November",
    "Dec":"December"
}
# Could use numbers as keys ie months 0-11
print(monthConversions.get("Jan")) # Returns January

# while loops rev
i = 1
while i <= 10:
    print(i) 
    i+=1
# should return list 1-10

# guessing game
secret_word = "flubber"
answer = ""
answer_counter = 0
answer_limit = 5
out_of_answers = False
print("Welcome! See if you can read our mind.")
while answer != secret_word and not(out_of_answers):
    if answer_counter <= answer_limit:
        answer = input("Can you guess the secret word? ")
        answer_counter += 1
    else:
        out_of_answers = True
if out_of_answers:
    print("Hard luck.")
else:
    print("Hooray! Well done.")

# for loops
list = ["Potats", "Apples", "Meat", "Eggs"]
for items in list:
    print(items) # Loop through, list as list
for items in range(len(list)):
    print(list[items])

for index in range(2,11):
    print(index) #2-10

# 2**3 == 2^3, 4**8 == 4^8
def exponent(base, power):
    result = 1
    for index in range(power):
        result = result * base
    return result
print(exponent(2,3))

number_grid = [ # 2d list / grid - matrices workings??
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [0]
]
print(number_grid[0][1]) #should print 2

# nested for loop:
for row in number_grid:
    for col in row:
        print(col) # prints all items as vals so not too helpful in this instance

# letter replacement in honour of Nathalie Soffe
def oodle(name2):
    oodled = ""
    for letter in name2:
        if letter.lower() in "aeiou":
            if letter.isupper():
                oodled = oodled + "Oodle"
            else:
                oodled = oodled + "oodle"
        else:
            oodled = oodled + letter
    return oodled
print(oodle(input("What is your name? ")))

# Try except // catching errors
try:
    number = int(input("Enter a number: "))
    print(number)
except ValueError as err: #important to have specific except to cover different potential errors
    print("Invalid input.") # Can we combine this with previous stuff?
    print(err)

# Reading from files!!!!!
file_file = open("file.txt", "r") # just to read
# w would be write to the file and/or change existing
# a == append to the end of the file, not change existing
# r+ == read and write
print(file_file.readable) # Checks file is readable
# EG if we had w access open, would return false
print(file_file.read()) # full file print
print(file_file.readline())# Reads first line
print(file_file.readline())#reads second
# print(file_file.readlines()) prints as list
# print(file_file.readline()[1]) accesses specific line
# for item in file_file.readlines():
#   print(item) seperate lines I think?

file_file.close() # Always remember to close, think like bracket

# writing to files
file_file = open("file.txt", "a") # append, w for writing, would override file
file_file.write("\nScoodle - Seventy") #\n new line
# warning - permanent writing, can easily mess up original file
file_file.close()

new_file = open("newfile.txt", "w")
new_file.write("blahblahblah")
new_file.close()
# could try with a .html and write a simple webpage through python

# Modules and Pip
# New file required

# classes can effectively be new data types
# useful for modelling abstracts
# create a 'variable' data class
# pokemon for example

class pokemon:
    def __init__(self, name, number, combat_power, hit_points): #initialise function
        # map out attributes of class as names above after self
        self.name = name
        self.number = number
        self.combat_power = combat_power
        self.hit_points = hit_points
#class defines the template, object is a thing fitting that template
# just defined what a pokemon is in the program



