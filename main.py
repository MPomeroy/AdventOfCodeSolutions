# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__ = "Mason"
__date__ = "$17-Dec-2015 7:20:56 PM$"

import sys

if __name__ == "__main__":
    print("Please enter the day of the puzzle to solve(between 4 and 10):")
    command = input('--> ')
    if command == '4':
        import Day4
        
    elif command == '5':
        import Day5
            
    elif command == '6':
        import Day6
        
    elif command == '7':
        import Day7
        
    elif command == '8':
        import Day8
        
    elif command == '9':
        import Day9
        
    elif command == '10':
        import Day10
        
    elif command == '11':
        import Day11
            
print('Exiting script...')
SystemExit.mro()
