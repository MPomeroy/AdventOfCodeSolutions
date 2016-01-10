# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__ = "Mason"
__date__ = "$9-Jan-2016 6:58:02 PM$"

def main():
    def isInt(s):
        try: 
            int(s)
            return True
        except ValueError:
            return False

    print('Reading in from file.')
    #get the puzzle input
    commandSequence = {}
    inputFile = open('Input/Day7.txt', 'r')
    commandList = inputFile.read()
    commandList = commandList.split("\n")
    i = 0
    for command in commandList:
        commandSequence[i] = command
        i = i+1
    inputFile.close()
    print('Finished reading file.')

    print('Beginning the tokenization.')
    print(commandSequence)
    wireList = {}
    #split each line into a list
    for key in commandSequence:
        line = commandSequence[key]
        commandSequence[key] = line.split(' ')
        #make a dictionary of all wires
        for token in commandSequence[key]:
            if token != 'NOT' and token != 'LSHIFT' and token != 'OR' and token != 'RSHIFT' and token != 'AND' and token != '->' and not isInt(token):
                if token not in wireList:
                    wireList[token] = 'unknown'
    wireList['b'] = '3176'
    print('Finished tokenizing the commands and building wirelist.')


    print('Starting main process loop...')
    #now we loop over each command row, when we hit an assignment or an equation 
    #with known values(from wireList) then we calculate the value and save it
    solved  = 0
    todrop = []
    try:
        while solved == 0:

            print('Removing previously processed gates')

            for keyToDrop in todrop:
                del commandSequence[keyToDrop]
            todrop = []#clear the todrop array
            print('Beginning new processing pass. '+ str(len(commandSequence))+' gates left.')
            for key in commandSequence:
                line = commandSequence[key]
                print(line)
                #handle simple assignment cases like:
                #line['1', '->', 'a']
                if len(line) == 3:
                    if isInt(line[0]) == False and wireList[line[0]] != 'unknown':
                        line[0] = wireList[line[0]]
                    if isInt(line[0]) and wireList[line[2]] == 'unknown':
                        wireList[line[2]] = line[0]
                        print('Setting ' + str(line[2])+' to '+str(line[0]))
                        todrop.append(key)
                    elif wireList[line[2]] != 'unknown':
                        todrop.append(key)

                if len(line) == 4 and line[0] == 'NOT':
                    if isInt(line[1]) == False and wireList[line[1]] != 'unknown':
                        line[1] = wireList[line[1]]
                    if isInt(line[1]) and wireList[line[3]] == 'unknown':
                        wireList[line[3]] =  ~int(line[1])
                        todrop.append(key)
                    elif wireList[line[3]] != 'unknown':
                        todrop.append(key)

                if len(line) == 5:
                    if isInt(line[0]) == False and wireList[line[0]] != 'unknown':
                        line[0] = wireList[line[0]]
                    if isInt(line[2]) == False and wireList[line[2]] != 'unknown':
                        line[2] = wireList[line[2]]
                    if isInt(line[0]) and isInt(line[2]) and wireList[line[4]] == 'unknown':
                        if line[1] == 'LSHIFT':
                            wireList[line[4]] = int(line[0])<<int(line[2])
                            print('Setting ' + str(line[4])+' to ' +str(line[0])+'(LSHIFT)'+str(line[2])+'='+str(wireList[line[4]]))
                            todrop.append(key)
                        if line[1] == 'RSHIFT':
                            wireList[line[4]] = int(line[0])>>int(line[2])
                            print('Setting ' + str(line[4])+' to ' +str(line[0])+'(RSHIFT)'+str(line[2])+'='+str(wireList[line[4]]))
                            todrop.append(key)
                        if line[1] == 'AND':
                            wireList[line[4]] = int(line[0])&int(line[2])
                            print('Setting ' + str(line[4])+' to ' +str(line[0])+'(AND)'+str(line[2])+'='+str(wireList[line[4]]))
                            todrop.append(key)
                        if line[1] == 'OR':
                            wireList[line[4]] = int(line[0])|int(line[2])
                            print('Setting ' + str(line[4])+' to ' +str(line[0])+'(OR)'+str(line[2])+'='+str(wireList[line[4]]))
                            todrop.append(key)
                    elif wireList[line[4]] != 'unknown':
                        todrop.append(key)
                if isInt(wireList['a']):
                    solved = 1
                    print(wireList)
                    print('Value of a is:'+str(wireList['a']))
    except Exception as e:
        print('Exception occured:'+e)
main()