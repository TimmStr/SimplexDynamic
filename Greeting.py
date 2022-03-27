import numpy as np
from matplotlib import pyplot as plt


class Greeting:
    def __init__(self):
        # self.structureVariables = int(input('How many structure variables:'))
        #self.structureVariables = 2  #### später löschen
        # self.equations = int(input('How many equations:'))
        #self.equations = 3  ##### später löschen

        self.structureVariables = 3  #### später löschen
        self.equations = 2  ##### später löschen
        self.targetFunction = 0
        self.arrays = 0
        self.solutions = []
        self.create_array()

    def create_array(self):
        self.arrays
        self.arrays = np.zeros((self.equations + 1, self.structureVariables + self.equations + 1))
        self.fill_array()

    def fill_array(self):
        # fill structure-,slack variables and b variables
        counter = self.structureVariables
        for equa in range(0, self.equations):
            for struc in range(0, self.structureVariables):
                pass
                #### später Auskommentieren weg machen
                # x = float(input(('Insert the '+str(struc+1)+'. structure variable of the '+str(equa+1))+'. equation: '))
                # self.arrays[equa][struc]=x
                # print(self.arrays)
            self.arrays[equa][counter] = 1
            counter = counter + 1
            ### später Auskommentieren weg machen
            # x = float(input(('Insert the b variable for the ' + str(equa + 1)) + '. equation: '))
            # self.arrays[equa][self.structureVariables+self.equations]=x
            # print(self.arrays)
        # ab hier später löschen
        # self.arrays = np.array([[40., 24, 1, 0, 0, 480],
        #                         [24, 48, 0, 1, 0, 480],
        #                         [0, 60, 0, 0, 1, 480],
        #                         [10, 40, 0, 0, 0, 0]], dtype=float)
        # np.set_printoptions(formatter={'float': lambda x: "{0:0.3f}".format(x)})
        # bis hier hin

        # 3d Darstellung:

        print(self.arrays)
        self.arrays = np.array([[1, 2, 7, 1, 0, 4],
                                [1, 3, 1, 0, 1, 5],
                                [1, 0, 3, 0, 0, 0]], dtype=float)
        np.set_printoptions(formatter={'float': lambda x: "{0:0.3f}".format(x)})

        self.add_target_function()

    def add_target_function(self):
        for struc in range(0, self.structureVariables):
            # später auskommentieren
            # x = float(input(('Insert the ' + str(struc + 1) + '. structure variable of the target equation: ')))
            pass
            # self.arrays[self.equations][struc]=x

        x = int(input(('If you want to maximize, type 1: ')))
        if (x == 1):
            for i in range(0, self.structureVariables):
                self.arrays[self.equations][i] = self.arrays[self.equations][i] * -1
        print(self.arrays)
        print()
        self.calc_pivot_column()

    def calc_pivot_column(self):
        min = self.arrays[self.equations][0]
        column_index = 0
        for i in range(1, self.structureVariables + self.equations + 1):
            if self.arrays[self.equations][i] < min:
                min = self.arrays[self.equations][i]
                column_index = i
        # print('Min= '+str(min))
        # print('Index= '+str(column_index))
        if min < 0:
            self.calc_pivot_element(column_index)
        else:
            print('Found perfect solution')
            self.show_graphics()

    def calc_pivot_element(self, column_index):
        row_index = 0
        pivot = self.arrays[0][self.structureVariables + self.equations] / self.arrays[0][column_index]
        for i in range(1, self.equations):
            if (self.arrays[i][column_index] > 0 and
                    self.arrays[i][self.structureVariables + self.equations] / self.arrays[i][column_index] < pivot):
                pivot = self.arrays[i][self.structureVariables + self.equations] / self.arrays[i][column_index]
                row_index = i
        print(self.arrays[row_index][column_index])
        print()
        self.divide_row_by_pivot(row_index, column_index)
        # print(pivot)

    def divide_row_by_pivot(self, row_index, column_index):
        divide_by = self.arrays[row_index][column_index]
        for i in range(0, self.structureVariables + self.equations + 1):
            self.arrays[row_index][i] = self.arrays[row_index][i] / divide_by

        self.arrays[1][3] = self.arrays[1][3] / 10
        print(self.arrays)
        print()
        self.base_change(row_index, column_index)

    def base_change(self, row_index, column_index):
        for i in range(0, self.equations + 1):
            multiply = self.arrays[i][column_index] / self.arrays[row_index][column_index]
            if (i != row_index):
                for j in range(0, self.structureVariables + self.equations + 1):
                    self.arrays[i][j] = self.arrays[i][j] - multiply * (self.arrays[row_index][j])
        print(self.arrays)
        print()

        for i in range(0, self.structureVariables):
            sum = 0
            b = 0
            for j in range(0, self.equations):
                sum = sum + self.arrays[j][i]
                if (self.arrays[j][i] == 1):
                    b = self.arrays[j][self.equations + self.structureVariables]
            if (sum == 1):
                self.solutions.append(b)
            else:
                self.solutions.append(0)

        self.calc_pivot_column()

    def show_graphics(self):
        if self.structureVariables <= 3:
            print(self.solutions)
            x = []
            y = []
            z = []
            # for i in range(0,len(self.solutions)):
            if (self.structureVariables == 1):
                x = self.solutions
                plt.scatter(x)
                plt.xlabel('1st structure variable')
            elif (self.structureVariables == 2):
                for i in range(0, len(self.solutions)):
                    if (i == 0 or i % 2 == 0):
                        x.append(self.solutions[i])
                    else:
                        y.append(self.solutions[i])
                plt.scatter(x, y)
                plt.xlabel('1st structure variable')
                plt.ylabel('2nd structure variable')
            elif (self.structureVariables == 3):
                fig = plt.figure()
                ax = fig.add_subplot(projection='3d')
                test = 0
                for i in range(0, len(self.solutions)):
                    written = False
                    if (test == 0):
                        x.append(self.solutions[i])
                        test = 1
                        written = True
                    elif (test == 1 and written == False):
                        y.append(self.solutions[i])
                        test = 2
                        written = True
                    elif (test == 2 and written == False):
                        z.append(self.solutions[i])
                        test = 0
                        written = True
                print('1st structure variable'+str(x))
                if(len(y)>=1):
                    print('2nd structure variable'+str(y))
                if(len(z)>=1):
                    print('3rd structure variable'+str(z))
                ax.scatter(x, y, z)
                ax.set_xlabel('1st structure variable')
                ax.set_ylabel('2nd structure variable')
                ax.set_zlabel('3rd structure variable')
        plt.show()

g = Greeting()
