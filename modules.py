# HAndy list of modules at
# https://docs.python.org/3/py-modindex.html
# pip package manager should be within 3
# cmd prompt pip --verions == version 20 something
# python_docx installed just to check

import tools
import docx

print(tools.roll_dice(6))
# docx. to call a docx fnct/var
# could also pip uninstall pythongfdjkfajbkfa

# importing from main memory test to trial

from memorytest import pokemon

pokemon1 = pokemon("Bulbasaur", 1, 150, 100) # object instance of class pokemon
pokemon2 = pokemon("Squirtle", 4, 150, 100)
print(pokemon1.name + str(pokemon1.number))

print(pokemon1.hard_hitter()) # calling function defined in class
pokemon1.attack()

class swimming_pokemon(pokemon):
    # class inheritance example
    def surf(self):
        print("The pokemon surfs!")
    # can override inherited functions
    def attack(self):
        print("The pokemon uses a water attack!")