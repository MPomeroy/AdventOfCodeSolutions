# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__ = "Mason"
__date__ = "$23-Jan-2016 2:03:50 PM$"

def main():
    import os.path
    import itertools
    
    puzzleNumber = input('Enter the puzzle number:')
    
    if not os.path.isfile('Input/Day13.txt'):
        print('Input file is required for Day 13! Please place your input in Day13.txt in the Input subfolder and try again.')
        os._exit(1)
    file = open('Input/Day13.txt', 'r')
    inputFile = file.read();
    
    lines = inputFile.split('\n')
    
    happinessMap = {}    
    for line in lines:
        words = line.split(' ')
        if words[0] not in happinessMap.keys():
            happinessMap[words[0]] = {}
        if words[10] not in happinessMap[words[0]].keys():
            happinessMap[words[0]][words[10][:-1]] = int(words[3])
            if words[2] == 'lose':
                happinessMap[words[0]][words[10][:-1]] = int(happinessMap[words[0]][words[10][:-1]])*-1
    
    if puzzleNumber == '2':
        happinessMap['you'] = {}
        for person in happinessMap.keys():
            happinessMap['you'][person] = 0
            happinessMap[person]['you'] = 0
    
    seatingPermuts = itertools.permutations(happinessMap.keys())
    
    highestHappiness = 0;
    for permut in seatingPermuts:
        permutHappiness = 0;
        enumPerm = enumerate(permut)
        for idl, person in enumPerm:
            if idl+1 <= len(permut)-1:
                greaterPerson = permut[idl+1]
            else:
                greaterPerson = permut[0]
            permutHappiness = permutHappiness + happinessMap[person][greaterPerson]
            if idl-1 >= 0:
                lesserPerson = permut[idl-1]
            else:
                lesserPerson = permut[len(permut)-1]
            permutHappiness = permutHappiness + happinessMap[person][lesserPerson]
        if permutHappiness > highestHappiness:
            highestHappiness = permutHappiness
    
    print('The highest possible happiness is:'+str(highestHappiness))
    
main()