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
print(pokemon1.name + pokemon1.number)
