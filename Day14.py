# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__ = "Mason"
__date__ = "$24-Jan-2016 11:52:37 AM$"

def main():
    import FileLoadWrapper
    import re
    import math
    
    puzzleNumber = input('Enter the puzzle number:')
    testCase = input('Run test case? y/n:')
    print(testCase)
    if(testCase == 'y' or testCase == 'Y'):
        loader = FileLoadWrapper.FileLoader('TestCase', '14')
        inputFile = loader.read();
        numberOfSeconds = 1000
    else:
        loader = FileLoadWrapper.FileLoader('Input', '14')
        inputFile = loader.read();
        numberOfSeconds = 2503
    
    
    reindeers = inputFile.split('\n')
    
    
    
    if(puzzleNumber == '1'):
        highestDistance = 0
    else:
        reindeerDistances = {}
        reindeerIt = 0
    combinedSearch = re.compile('([0-9]{1,}) .* ([0-9]{1,}) .* ([0-9]{1,})')
    for reindeerRec in reindeers:
        combined = combinedSearch.search(reindeerRec)
        kmps = int(combined.group(1))
        flytime = int(combined.group(2))
        resttime = int(combined.group(3))
        
        if(puzzleNumber == '1'):
            modulus = numberOfSeconds%(flytime+resttime)
            if(modulus < flytime):
                appendedFlytime = modulus
            else:
                appendedFlytime = flytime
            distance = (((math.floor(numberOfSeconds/(flytime+resttime)))*flytime)+appendedFlytime)*kmps
        
            if distance > highestDistance:
                highestDistance = distance
        else:
            numberOfSecondsIt = 1
            reindeerState = 1
            reindeerDistances[reindeerIt] = {}
            reindeerDistances[reindeerIt][0] = 0
            while(numberOfSecondsIt < numberOfSeconds):
                if(reindeerState == 1):
                    #don't overblow the racetimer
                    if(numberOfSecondsIt < flytime):
                        tempLimit = numberOfSeconds
                    else:
                        tempLimit = numberOfSecondsIt+flytime
                    temp = numberOfSecondsIt
                    #store the distance the reindeer is at at each second
                    while(temp < tempLimit):
                        reindeerDistances[reindeerIt][temp] = reindeerDistances[reindeerIt][temp-1]+kmps
                        temp += 1
                    reindeerState = 0
                    numberOfSecondsIt += flytime
                else:
                    
                    if(numberOfSecondsIt < resttime):
                        tempLimit = numberOfSeconds
                    else:
                        tempLimit = numberOfSecondsIt+resttime
                    temp = numberOfSecondsIt
                    #store the distance the reindeer is at at each second
                    while(temp < tempLimit):
                        reindeerDistances[reindeerIt][temp] = reindeerDistances[reindeerIt][temp-1]
                        temp += 1
                    reindeerState = 1
                    numberOfSecondsIt += resttime
            reindeerIt += 1
    
    
    if(puzzleNumber == '1'):
        print('Highest distance is:'+str(highestDistance))
    else:
        reindeerScores = {}
        for number, dist in reindeerDistances.items():
            reindeerScores[number] = 0
            
        numberOfSeconds = numberOfSeconds-1
        while(numberOfSeconds >= 0):
            highestDistance = 0
            farthestReindeer = 0
            #need to handle farthest reindeer being tied
            for reindeerNum, distances in reindeerDistances.items():
                if(distances[numberOfSeconds] > highestDistance):
                    highestDistance = distances[numberOfSeconds]
                    farthestReindeer = reindeerNum
            reindeerScores[farthestReindeer] += 1
            numberOfSeconds = numberOfSeconds-1
        highestScore = 0
        for key, score in reindeerScores.items():
            if(score > highestScore):
                highestScore = score
        print('Highest score:' + str(highestScore))
        
main()