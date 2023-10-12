#Import random
import random


#Create the function below:
def matrixBuilder(num):
    matrix = []
    
    for i in range(num):
        innermatrix = [1] * num
        matrix.append(innermatrix)
    
    return matrix
        
print(matrixBuilder(3))