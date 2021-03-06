import numpy as np
import csv
import random
import time
from board import board

class Solve:
    def __init__(self, board):
        #self.board = board
        self.rows = len(board)
        self.cols = len(board[0])
        self.factor = int(self.rows ** 0.5) #The board can only be made up of perfect squares (just how it be) so this variable is the square root of that value

    #Determines whether the number at the inputted posistion is valid
    def validate(self, board, pos, num):
        
        T = np.array(board) #numpy makes matrices easier :)

        tempRow = T[pos[0]] #extract row from matrix
        tempCol = T[:,pos[1]] #extract col from matrix

        #------rows/cols------
        #0's represent empty positions on the board
        #Consider only the values that are not 0's
        row = [i for i in tempRow if i != 0] 
        col = [j for j in tempCol if j != 0]

        #if there are multiple instances of a single number in a row or col, then this will catch the invalid placement
        if len(set(row)) != len(row) or len(set(col)) != len(col):
            return False
        
        #------box------
        #temp values for the row and col of the n^1/2 x n^1/2 positions. In a 9x9 board, these will be the 3x3 box positions the value that
        # is being check resides
        r = int(pos[0] / self.factor)
        c = int(pos[1] / self.factor)

        #iterate through the box
        for x in range(self.factor):
            for y in range(self.factor):
                xSkew = x + r*self.factor
                ySkew = y + c*self.factor
                #print(xSkew, ySkew, board[xSkew][ySkew], pos)
                val = board[xSkew][ySkew] #get the value of each position in the box
                if (xSkew,ySkew) != pos and val != 0 and val == num:
                    return False
                else:
                    continue
        return True

    #Solves the sudoku board
    def solve(self):
        for i in range(self.rows):
            for j in range(self.cols):
                #Empty cell
                if board[i][j] == 0:
                    for num in range(1,self.rows+1):
                        board[i][j] = num
                        if self.validate(board, (i,j), num):
                            if self.solve():
                                return True
                        board[i][j] = 0
                    return False
        return True
    
    #prints a nxn board
    def printBoard(self, board): 
        output = ""
        for i in range(self.rows):
            for j in range(self.cols):
                if (j+1) % self.factor == 0 and j != 0 and j != self.cols-1:
                    output += str(board[i][j]) + "|"
                else:
                    output += str(board[i][j]) + " "
            output += "\n"
            
            if (i+1) % self.factor == 0 and i != 0 and i != self.rows-1:
                output += "- "*self.rows + "\n"
        return output

'''
#Return a 2D matrix
def generateBoard(size):
    with open('board.csv', 'w', newline='') as board:
        yo = csv.writer(board, delimiter = ' ', quotechar = '|', quoting=csv.QUOTE_MINIMAL)
        
        for row in range(9):
            yo.writerow([0]*9)
    root = size**0.5
    if int(root + 0.5) ** 2 == size:
        board = [[0 for _ in range(size)] for _ in range(size)]
        #return Solve.printBoard(board)
        return board
    return "Size needs to be a perfect square"
'''
if __name__ == '__main__':

    #board = generateBoard(9) #Figure out how to generate a board with random numbers 
    #print(board)
    x = Solve(board)
    print(x.printBoard(board))
    print(x.solve())
    print(x.printBoard(board))