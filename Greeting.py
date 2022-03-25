import numpy as np


class Greeting:
    def __init__(self):
        self.structureVariables = int(input('How many structure variables:'))
        self.equations = int(input('How many equations:'))
        self.targetFunction = 0
        self.arrays = 0
        self.createArray()

    def createArray(self):
        self.arrays = np.zeros((self.equations + 1, self.structureVariables + self.equations + 1))
        self.fillArray()

    def fillArray(self):
        #fill structure-,slack variables and b variables
        counter=self.structureVariables
        for equa in range(0, self.equations):
            for struc in range(0, self.structureVariables):
                x = float(input(('Type the '+str(struc+1)+'. strucure variable of the '+str(equa+1))+'. equation: '))
                self.arrays[equa][struc]=x
                print(self.arrays)
            self.arrays[equa][counter]=1
            counter = counter + 1
            x = float(input(('Type the b variable for the ' + str(equa + 1)) + '. equation: '))
            self.arrays[equa][self.structureVariables+self.equations]=x
            print(self.arrays)
        self.addTargetFunction()


    def addTargetFunction(self):
        for struc in range(0,self.structureVariables):
            x = float(input(('Type the ' + str(struc + 1) + '. structure variable of the target equation: ')))
            self.arrays[self.equations][struc]=x
        x = int(input(('If you want to maximize, type 1: ')))
        if (x == 1):
            for i in range(0,self.structureVariables):
                self.arrays[self.equations][i]=self.arrays[self.equations][i]*-1
        print(self.arrays)


g = Greeting()
