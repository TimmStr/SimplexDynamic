import numpy as np



class Greeting:
    def __init__(self):
        #self.structureVariables = int(input('How many structure variables:'))
        self.structureVariables=2#### später löschen
        #self.equations = int(input('How many equations:'))
        self.equations=3 ##### später löschen
        self.targetFunction = 0
        self.arrays = 0
        self.create_array()

    def create_array(self):

        self.arrays
        self.arrays = np.zeros((self.equations + 1, self.structureVariables + self.equations + 1))
        self.fill_array()

    def fill_array(self):
        #fill structure-,slack variables and b variables
        counter=self.structureVariables
        for equa in range(0, self.equations):
            for struc in range(0, self.structureVariables):
                pass
                #### später Auskommentieren weg machen
                #x = float(input(('Type the '+str(struc+1)+'. strucure variable of the '+str(equa+1))+'. equation: '))
                #self.arrays[equa][struc]=x
                #print(self.arrays)
            self.arrays[equa][counter]=1
            counter = counter + 1


            ### später Auskommentieren weg machen
            #x = float(input(('Type the b variable for the ' + str(equa + 1)) + '. equation: '))
            #self.arrays[equa][self.structureVariables+self.equations]=x
            #print(self.arrays)
        #ab hier später löschen
        self.arrays=np.array([[40.,24,1,0,0,480],
                     [24,48,0,1,0,480],
                     [0,60,0,0,1,480],
                     [10,40,0,0,0,0]],dtype=float)
        np.set_printoptions(formatter={'float': lambda x: "{0:0.3f}".format(x)})

        #bis hier hin
        print(self.arrays)

        self.add_target_function()

    def add_target_function(self):
        for struc in range(0,self.structureVariables):
            # später auskommentieren
            #x = float(input(('Type the ' + str(struc + 1) + '. structure variable of the target equation: ')))
            pass
            #self.arrays[self.equations][struc]=x

        x = int(input(('If you want to maximize, type 1: ')))
        if (x == 1):
            for i in range(0,self.structureVariables):
                self.arrays[self.equations][i]=self.arrays[self.equations][i]*-1
        print(self.arrays)
        self.calc_pivot_column()

    def calc_pivot_column(self):
        min=self.arrays[self.equations][0]
        column_index=0
        for i in range (1, self.structureVariables+self.equations+1):
            if self.arrays[self.equations][i]<min:
                min=self.arrays[self.equations][i]
                column_index=i
        print('Min= '+str(min))
        print('Index= '+str(column_index))
        self.calc_pivot_element(column_index)

    def calc_pivot_element(self, column_index):
        row_index=0
        pivot=self.arrays[0][self.structureVariables+self.equations]/self.arrays[0][column_index]
        for i in range(1,self.equations):
            if(self.arrays[i][column_index]>0 and
                    self.arrays[i][self.structureVariables+self.equations]/self.arrays[i][column_index]<pivot):
                pivot=self.arrays[i][self.structureVariables+self.equations]/self.arrays[i][column_index]
                row_index=i
        print(self.arrays[row_index][column_index])
        self.divide_row_by_pivot(row_index,column_index)
        #print(pivot)

    def divide_row_by_pivot(self,row_index,column_index):
        divide_by=self.arrays[row_index][column_index]
        for i in range(0,self.structureVariables+self.equations+1):
            self.arrays[row_index][i]=self.arrays[row_index][i]/divide_by

        self.arrays[1][3]=self.arrays[1][3]/10
        #np.set_printoptions(precision=3)
        print(self.arrays)
        print(self.arrays[row_index][4])

    def base_change(self):





g = Greeting()
