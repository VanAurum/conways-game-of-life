#Standard python library imports
import random


'''
Rules to Conway's game of life:
    1. Cells next to exactly 3 alive cells will become alive in the next iteration.
    2. Each cell with 1 or fewer alive neighbours will die in the next iteration.
    3. Each cell with 4 or more live neighbours will die in the next iteration.
    4. Survival: if alive, a cell with 2 or 3 neighbours will persist.
    
Algorithm:
    1. initialize a random matrix.
    2. initialize a random matrix representing state T+1.
    3. iterate through each cell in initial matrix applying conway's rules to matrix T+1.
    4. set next matrix to initial matrix.
    5. repeat for all iterations of the game.    
'''

def create_matrix(n):
    '''
    Creates an n x n matrix of random binary digits
    '''
    return [[random.randint(0,1) for _ in range(n)] for _ in range(n)]

def get_top(matrix,x,y):
    '''
    Returns the value of the cell directly above coordinate x,y
    '''
    if x==0:
        return 0
    return matrix[x-1][y]

def get_right(matrix,x,y):
    '''
    Returns the value of the cell directly to the right of coordinate x,y
    '''    
    if y==len(matrix)-1:
        return 0
    return matrix[x][y+1]

def get_bottom(matrix,x,y):
    '''
    Returns the value of the cell directly below coordinate x,y
    '''
    if x==len(matrix)-1:
        return 0
    return matrix[x+1][y]

def get_left(matrix,x,y):
    '''
    Returns the value of the cell directly to the left of coordinate x,y
    '''
    if y==0:
        return 0
    return matrix[x][y-1]

def sum_neighbours(matrix,x,y):
    '''
    Sums the value of the four neighbours at coordinate x,y
    '''
    m=matrix
    return  sum([ get_top(m,x,y),get_right(m,x,y),get_left(m,x,y),get_bottom(m,x,y),])

def apply_conway(matrix,x,y):
    '''
    Applies the logic of Conway's rules to the matrix cell at x,y.
    '''    
    n_sum=sum_neighbours(matrix,x,y)
    cell_value=matrix[x][y]
    if n_sum==3:
        return 1
    if n_sum<=1:
        return 0
    if n_sum==4:
        return 0
    if (cell_value==1 and (n_sum==2 or n_sum==3)):
        return 1
    if (cell_value==0 and (n_sum==2)):
        return 0
       
def run_iteration(matrix):
    '''
    Runs one iteration of the game.  Loops through each cell on the board, applying 
    Conway's rules to each cell and loading the resulting value into the matrix at T+1
    '''
    new_matrix=[[0]*len(matrix) for _ in range(len(matrix))]
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            t_plus=apply_conway(matrix,i,j)
            new_matrix[i][j]=t_plus
    return new_matrix        

def print_game(matrix):
    '''
    Prints the existing game matrix
    '''
    print('\n')
    for x in matrix:
        print(*x, sep=" ")
    print('\n')  



if __name__=='__main__':
    
    iterations=3    
    matrix=create_matrix(8)
    print_game(matrix)
    for _ in range(iterations):
        new=run_iteration(matrix)
        print_game(new)
        matrix=new

        
        