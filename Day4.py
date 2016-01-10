# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__ = "Mason"
__date__ = "$9-Jan-2016 6:53:14 PM$"

def main():
    import hashlib
    #begin by getting the puzzle number
    checkString = ''
    while checkString == '':
        print('Enter puzzle number(1 or 2):')
        puzzleNum = input('--> ')
        if puzzleNum == '1':
            checkNumber = 5
            checkString = '00000'
        elif puzzleNum == '2':
            checkNumber = 6
            checkString = '000000'


    secretKey = "yzbqklnj"
    hashSuffixNum = 0
    hashResult = ''
    while hashResult[0:checkNumber] != checkString:
        hashSuffixNum = hashSuffixNum+1
        fullKey = secretKey.encode('utf-8')+str(hashSuffixNum).encode('utf-8')
        hashCalc = hashlib.md5()
        hashCalc.update(fullKey)
        hashResult = hashCalc.hexdigest()
    print("Lowest number is: "+str(hashSuffixNum))
    print("Full Key: "+str(fullKey))
    
main()
