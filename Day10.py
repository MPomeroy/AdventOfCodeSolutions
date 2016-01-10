# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__ = "Mason"
__date__ = "$9-Jan-2016 7:08:39 PM$"

def main():
    string = input('Enter your starting number:')
        
    recursions = 50
    while recursions > 0:
        print('On recursion:'+str(recursions))
        currentChar = ''
        currCharCount = 1
        newString = ''
        for i in list(range(len(string))):
            if i == 0:
                currentChar = string[i]
                continue
            if string[i] == currentChar:
                currCharCount += 1
            else:
                newString = newString+str(currCharCount)+string[i-1]
                currentChar = string[i]
                currCharCount = 1
            if i == len(string)-1:
                newString = newString+str(currCharCount)+string[i]
        print('old string:'+string)
        print('new string:'+newString)
        string = newString
        recursions -= 1
    print('Length of string after 40 iterations is:'+str(len(string)))
    
main()