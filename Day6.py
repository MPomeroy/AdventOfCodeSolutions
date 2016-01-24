# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__ = "Mason"
__date__ = "$9-Jan-2016 6:57:17 PM$"

def main():
    import FileLoadWrapper
    import re
    # Set up a map of the christmas lights
    numOfLights = list(range(1000))
    lightArray = {}
    for x in numOfLights:
        lightArray[x] = {}
        for y in numOfLights:
            lightArray[x][y] = 0
    
    loader = FileLoadWrapper.FileLoader('Input', '6')
    inputString = loader.read()
    inputCommands = inputString.split('\n')
    
    puzzleNumber6 = input('Enter the puzzle Number:')
    
    for commandString in inputCommands:
        command = re.search("([a-z]*.[a-z]*)", commandString)
        beginningCoor = re.search("([0-9]*,[0-9]*)", commandString)
        endCoor = re.search("through ([0-9]*,[0-9]*)", commandString)
        begCoorArray = beginningCoor.group(0).split(',');
        endCoorArray = endCoor.group(1).split(',');

        XRange = list(range(int(begCoorArray[0]), int(endCoorArray[0])+1))
        YRange = list(range(int(begCoorArray[1]), int(endCoorArray[1])+1))
        for x in XRange:
            for y in YRange:

                if command.group(0) == 'turn on':
                    if puzzleNumber6 == '1':
                        lightArray[x][y] = 1
                    if puzzleNumber6 == '2':
                        lightArray[x][y] = lightArray[x][y]+1
                if command.group(0) == 'turn off':
                    if puzzleNumber6 == '1':
                        lightArray[x][y] = 0
                    if puzzleNumber6 == '2':
                        lightArray[x][y] = lightArray[x][y]-1
                        if(lightArray[x][y] < 0):
                            lightArray[x][y] = 0
                if command.group(0) == 'toggle ':
                    if puzzleNumber6 == '1':
                        if lightArray[x][y] == 1:
                            lightArray[x][y] = 0
                        else:
                            lightArray[x][y] = 1
                    if puzzleNumber6 == '2':
                        lightArray[x][y] = lightArray[x][y]+2


    TurnedOnLights = 0;
    TotalBrightness = 0
    for x in lightArray:
        for y in lightArray[x]:
            if puzzleNumber6 == '1' and lightArray[x][y] == 1:
                TurnedOnLights = TurnedOnLights+1
            elif puzzleNumber6 == '2':
                TotalBrightness = TotalBrightness+lightArray[x][y]
    print('Number of Turned on Lights:'+str(TurnedOnLights))
    print('Total birghtness:'+str(TotalBrightness))
main()
