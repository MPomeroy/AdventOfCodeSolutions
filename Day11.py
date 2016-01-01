# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__ = "Mason Pomeroy"
__date__ = "$24-Dec-2015 1:30:58 PM$"
__name__ = 'Day11'


def main():
    password = input('Enter the starting password:')
    
    alphList = list('abcdefghjkmnpqrstuvwxyz')
    alphDict = {}
    alphRevDict = {}
    i = 0
    for letter in alphList:
        alphDict[letter] = i
        i += 1
    i = 0
    for letter in alphList:
        alphRevDict[i] = letter
        i += 1
    
        
    def get_new_pass(password):
        lastChar = password[len(password)-1]
        password = password[0:len(password)-1]
        if(lastChar == 'z'):
            password = get_new_pass(password)
            newChar = 'a'
        else:
            lastCharNum = alphDict[lastChar]
            newChar = alphRevDict[lastCharNum+1]
        password = password+newChar
        return password
    
    solved = 0
    while solved == 0:
        password = get_new_pass(password)
        print('Got new password:'+password)
        doubleLetterCount = 0
        runCount = 0
        for i in list(range(len(password))):
            if i == 0:
                continue
            if password[i] == password[i-1]:
                if i > 1 and password[i-1] != password[i-2]:
                    doubleLetterCount += 1
                elif i <= 1:
                    doubleLetterCount += 1
            if i > 1 and password[i] not in list('abjkmn'):
                if password[i-1] == alphRevDict[alphDict[password[i]]-1] and password[i-2] == alphRevDict[alphDict[password[i-1]]-1]:#because we can't have i,l or o these can't be in a run anyway
                    runCount = 2
            if(doubleLetterCount == 2 and runCount == 2):
                solved = 1
                break
        print('Verification results:doubleLetter:'+str(doubleLetterCount)+'runCount:'+str(runCount))
    print('First valid pass is:'+password)
    
main()
