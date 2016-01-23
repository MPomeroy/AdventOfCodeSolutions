# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__ = "Mason"
__date__ = "$9-Jan-2016 6:59:33 PM$"

def main():
    import os.path
    import binascii
        
    puzzleNumber = input('Which Puzzle number?')

    runTestCase = input("Run the test case?(y/n):")
    if(runTestCase == 'y' or runTestCase == 'Y'):
        if not os.path.isfile('TestCase/Day7.txt'):
            print('Input file is required for Day 7! Please place your input in Day7.txt in the TestCase subfolder and try again.')
            os._exit(1)
        file = open('TestCase/Day8.txt', 'r')
    if(runTestCase == 'n' or runTestCase == 'N'):
        if not os.path.isfile('Input/Day8.txt'):
            print('Input file is required for Day 8! Please place your input in Day8.txt in the Input subfolder and try again.')
            os._exit(1)
        file = open('Input/Day8.txt', 'r')
    firstReading = file.read()

    strForReading = firstReading
    strForReading = strForReading.replace("\n", '')
    fileLength = len(strForReading)
    lines = firstReading.split("\n")
    condensedLine = ''

    if(puzzleNumber == '1'):
        for line in lines:
            line = line[1:len(line)-1]
            condensedString = ''
            interpretSlash = False
            interpretHex = False
            hexBuffer = ''
            for i in list(range(len(line))):
                char = line[i]
                if interpretHex != False:
                    hexBuffer = str(hexBuffer)+str(char)
                    interpretHex = interpretHex-1
                    if interpretHex == 0:
                        char =  'a'#it doesn't matter what the hex character is just stick something in
                        condensedString = condensedString+str(char)
                        interpretHex = False
                elif interpretSlash == True:
                    if(char == 'x'):
                        interpretHex = 2
                    else:
                        condensedString = condensedString+char
                    interpretSlash = False
                elif(char == "\\"):
                    interpretSlash = True
                    continue
                else:
                    condensedString = condensedString+char
            condensedLine = condensedLine+condensedString
        print(fileLength)
        print(len(condensedLine))
        print('The difference between the file and string is:'+str(fileLength-len(condensedLine)))
    else:
        for line in lines:
            line = line[1:len(line)-1]
            condensedString = '"\\"'
            for i in list(range(len(line))):
                char = line[i]
                if(char == "\\"):
                    condensedString = condensedString+'\\'+'\\'
                    continue
                elif(char == '"'):
                    condensedString = condensedString+'\\'+char
                    continue
                else:
                    condensedString = condensedString+char
            print(condensedString+'\\""')
            condensedLine = condensedLine+condensedString+'\\""'
        print(fileLength)
        print('The condensedLine has '+str(len(condensedLine))+' chars(in this puzzle this is actually an expanded string.)')
        print('The difference between the file and string is:'+str(len(condensedLine)-fileLength))

    file.close()
    
main()
