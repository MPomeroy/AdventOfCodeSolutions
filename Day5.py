# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__ = "Mason"
__date__ = "$9-Jan-2016 6:56:07 PM$"

def main():
    import os.path
    import re
    ThreeVowelRe = re.compile("[a,e,i,o,u].*[a,e,i,o,u].*[a,e,i,o,u]")
    TwoInARowRe = re.compile(r'([a-z])\1{1,}')
    DisallowedStrings = re.compile("(ab)|(cd)|(pq)|(xy)")

    #puzzleTwo regex
    MatchWithOneBetween = re.compile(r'([a-z]).\1')
    MatchTwoPairs = re.compile(r'([a-z][a-z]).*\1')

    niceStrings = 0
    #entryString = "uurcxstgmygtbstg"
    if not os.path.isfile('Input/Day5.txt'):
        print('Input file is required for Day 5! Please place your input in Day5.txt in the Input subfolder and try again.')
        os._exit(1)
    inputFile = open('Input/Day5.txt', 'r')
    entryString = inputFile.read()

    stringList = entryString.split('\n')
    puzzleNumber = input('Enter the puzzle Number:')
    if puzzleNumber == '1':
        for string in stringList:
            #check for three vowels
            match = ThreeVowelRe.search(string)
            if match:
                pass
                #print("found three vowels")
            else:
                print('There arent three vowels..')
                continue

            #check for two letters in a row
            match = TwoInARowRe.search(string)
            if match:
                pass
                #print("it's a match")
            else:
                print('There arent two letters in a row...')
                continue

            #check for dissallowed characters
            match = DisallowedStrings.search(string)
            if match:
                print('Found illegal string...')
                continue
            else:
                niceStrings = niceStrings+1
        print('Number of NiceStrings : '+str(niceStrings))
    else:
        for string in stringList:
            print(string)
            match = MatchWithOneBetween.search(string)
            if match:
                print('one between found')
                pass
            else:
                continue

            match = MatchTwoPairs.search(string)
            if match:
                print('pairs found:'+match.group(0));
                niceStrings = niceStrings+1
        print('Number of NiceStrings : '+str(niceStrings))
        
main()