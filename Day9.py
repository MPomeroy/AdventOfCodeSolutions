# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__ = "Mason"
__date__ = "$9-Jan-2016 7:07:15 PM$"

def main():
    import itertools
        
    print('This Day 9 solution solves both puzzle 1 and 2 simultaneously.')

    file = open('Input/Day9.txt', 'r')
    inputText = file.read()

    lines = inputText.split('\n')
    cachedDistance = {}
    for line in lines:
        words = line.split(' ')
        #build the cached distance dictionary
        for i in [0, 2]:
            if words[i] not in cachedDistance.keys():
                for locKey, locDict in cachedDistance.items():
                    if words[i] not in locDict:
                        locDict[words[i]] = 0
                cachedDistance[words[i]] = {el:0 for el in cachedDistance.keys()}
    for line in lines: #populate the cachedDistance table
        words = line.split(' ')
        cachedDistance[words[0]][words[2]] = words[4]
        cachedDistance[words[2]][words[0]] = words[4]
    print(cachedDistance)

    locList = cachedDistance.keys()

    permutationList = itertools.permutations(locList, 8)
    permutationList = [x for x in permutationList]
    currLowestDist = 1000
    currHighestDist = 0
    for permut in permutationList:
        currDist = 0
        i = 0
        for stop in permut:
            if i == 0:
                i += 1
                continue
            currDist = currDist+int(cachedDistance[stop][permut[i-1]])
            i += 1
        if currDist < currLowestDist:
            currLowestDist = currDist
        if currDist > currHighestDist:
            currHighestDist = currDist
    print('Lowest possible distance is:'+str(currLowestDist))
    print('Highest possible distance is:'+str(currHighestDist))
main()
