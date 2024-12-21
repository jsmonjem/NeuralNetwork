import math

def sigmoid(x):
    if isinstance(x, float) or isinstance(x, int):
        return ((math.exp(x))/(1+math.exp(x)))
    elif isinstance(x, list):
        matrix=[]
        for i in range (len(x)):
            matrix.append([])
            for j in range (len(x[0])):
                matrix[i].append(0)
        for i in range (len(x)):
            for j in range (len(x[0])):
                matrix[i][j]=(math.exp(x[i][j]))/(1+math.exp(x[i][j]))   
        return matrix

#sigmoid.sigmoid(i)
