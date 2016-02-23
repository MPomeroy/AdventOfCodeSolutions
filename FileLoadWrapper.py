# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__ = "Mason"
__date__ = "$24-Jan-2016 11:58:28 AM$"

class FileLoader:
    
    def __init__(self, TCorI, dayNum):
        import os.path
        if not os.path.isfile(TCorI+'/Day'+dayNum+'.txt'):
            print('Input file is required for Day '+dayNum+'! Please place your input in Day'+dayNum+'.txt in the Input subfolder and try again.')
            os._exit(1)
        self.file = open(TCorI+'/Day'+dayNum+'.txt', 'r')
        
    def read(self):
        return(self.file.read());