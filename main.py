# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__ = "Mason"
__date__ = "$17-Dec-2015 7:20:56 PM$"

import sys
import importlib

if __name__ == "__main__":
    print("Please enter the day of the puzzle to solve(between 4 and 10):")
    command = input('--> ')
    if int(command) in range(4, 8):
        try:
            importlib.import_module('Day'+command)
        except importError:
                print('You gave a valid day, but no solution was found...')
    else:
        print('No solution found for that day!')
            
print('Exiting script...')
SystemExit.mro()
