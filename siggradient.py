import sigmoid

def siggradient(x):
    if isinstance(x, float) or isinstance(x, int):
        return (sigmoid.sigmoid(x)*(1-sigmoid.sigmoid(x)))
    elif isinstance(x, list):
        matrix=[]
        for i in range (len(x)):  #creo una matriz en ceros...
            matrix.append([])
            for j in range (len(x[0])):
                matrix[i].append(0)
        for i in range (len(x)):  #lleno la matriz.
            for j in range (len(x[0])):
                matrix[i][j]=(sigmoid.sigmoid(x[i][j])*(1-sigmoid.sigmoid(x[i][j])))
        return matrix


#siggradient.siggradient(i)
