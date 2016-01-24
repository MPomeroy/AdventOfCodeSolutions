# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__ = "Mason"
__date__ = "$24-Dec-2015 6:16:30 PM$"
__name__ = 'Day12'

def main():
    import FileLoadWrapper
    import json
    
    puzzleNumber = input('Puzzle Number:')
    
    runTestCase = input('Run test case?(y/n) ->')
    if runTestCase == 'y':
        if puzzleNumber == '1':
            loader = FileLoadWrapper.FileLoader('TestCase', '12')
        else:
            loader = FileLoadWrapper.FileLoader('TestCase', '12-2')
    else:
        loader = FileLoadWrapper.FileLoader('Input', '12')
    file = loader.read();
    rawJSON = file.read()
    
    jsonArray = json.loads(rawJSON)
    
    def is_int(s):
        try: 
            int(s)
            return True
        except ValueError:
            return False
        except TypeError:
            return False
        
    def add_slot_to_total(slot, intTotal):
#        print('Add slot to total called with slot:' +str(slot))
        if is_int(slot):
#            print('Adding '+str(slot)+' to total '+str(intTotal)+'  new total:'+ str(intTotal+slot))
            intTotal = intTotal+slot
        elif isinstance(slot, list) or isinstance(slot, dict):
            intTotal = num_array_search(slot, intTotal)
#        print('returning: '+str(intTotal))
        return intTotal
            
    def num_array_search(array, intTotal):
       
        if isinstance(array, dict):
            #Filter out anything with "red" in it for puzzle number 2
            if puzzleNumber == '2' and "red" not in array.values() and "red" not in array.keys():
                for key, slot in array.items():
                    intTotal = add_slot_to_total(slot, intTotal)
                    
        elif isinstance(array, list):
            for slot in array:
                intTotal = add_slot_to_total(slot, intTotal)
                    
        return intTotal
    
    print('Integer total is:'+str(num_array_search(jsonArray, 0)))
    
    
main()