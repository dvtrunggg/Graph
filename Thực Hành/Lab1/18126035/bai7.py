import numpy as np
def sortAscendingRow(matrix):
    sortedM = matrix[np.argsort(matrix.sum(axis=1))]
    print(sortedM)
'''    
def sum0(a, b):
    for i in range(len(a)):
        for j in range(len(a[0])):
            c[i][j] = a[i][j] + b[i][j]
    return c

def multiply0(a, b):
    for i in range(len(a)): 
        for j in range(len(b[0])): 
            for k in range(len(b)):
                c[i][j] += a[i][k] * b[k][j]    
'''    
    
    
# test thử:)))    
def Sum(a,b):
    c = a + b
    return c
def Multiply(a,b):
    c = a*b
    return c
    
def isMagicSquare(matrix):
    row = len(matrix)
    column = len(matrix[0])

    if (row == column):
        s1 = 0
        for i in range(row): 
            s1 += matrix[i][i]

        s2 = 0
        for i in range(row): 
            s2 += matrix[i][row - i - 1]

        if (s1 != s2): 
            return False
        
        for i in range(row): 
            rowSum = 0
            for j in range(column): 
                rowSum += matrix[i][j]

            if (rowSum != s1): 
                return False

        for i in range(row): 
            columnSum = 0
            for j in range(column): 
                columnSum += matrix[j][i]
            
            if (columnSum != s1): 
                return False

        return True
    else: 
        return False
        
        
a = np.array([[5, 12, 6, 7], [3, 5, 2, 1], [5, 2, 6, 1]])

b = np.array([[7, 3, 10, 10], [9, 5, 8, 4], [11, 5, 4, 7]])


print(Sum(a,b))
print(Multiply(a,b))
sortAscendingRow(a)
print(a)
print(isMagicSquare(a))