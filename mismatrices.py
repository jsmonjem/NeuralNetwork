# -*- coding: utf-8 -*-

def printmatrix(matrix):
    if matrix==None:
        print("[]")
        return
    print("rows",len(matrix))
    print("columns",len(matrix[0]))
    for i in range (len(matrix)):
        for j in range(len(matrix[0])):
            print( matrix[i][j],end=" ")
        print()
    print()

def matrizPorEscalar(A,e):
    rowsA=len(A)
    colA=len(A[0])
    for i in range (rowsA):
        for j in range(colA):
            A[i][j]=A[i][j]*e
    return A

def matrixSubstraction(A,B) : #function to obtain A minus B.
    rowsA=len(A)
    colA=len(A[0])
    rowsB=len(B)
    colB=len(B[0])
    if colA!=colB or rowsA!=rowsB:
        print("matrices incompatibles para resta.")
        print("rowsA: ",rowsA,"rowB:",rowsB,"colA: ",colA,"colB:",colB)
        return None
    else:
        for i in range(rowsA):
            for j in range (colA):
                A[i][j]=A[i][j]-B[i][j]
        return A

def transpose(A):
    rowsA=len(A)
    colA=len(A[0])
    result=[]
    for i in range (colA):
        result.append([])
        for j in range (rowsA):
            result[i].append(0)

    for k in range (colA):
        for l in range(rowsA):
            result[k][l]=A[l][k]
    return result

def hadamard(A,B):
    rowsA=len(A)
    colA=len(A[0])
    rowsB=len(B)
    colB=len(B[0])
    if colA!=colB or rowsA!=rowsB:
        print("matrices incompatibles para producto elemento a elemento.")
        print("rowsA: ",rowsA,"rowB:",rowsB,"colA: ",colA,"colB:",colB)
    else:
        for i in range(rowsA):
            for j in range(colA):
                A[i][j]=A[i][j]*B[i][j]
        return A

def matrixMultp(A,B):   #function to multiply A times B.
    print("hello")
    rowsA=len(A)
    colA=len(A[0])
    rowsB=len(B)
    colB=len(B[0])
    result=[]
    if colA!=rowsB:
        print("matrices incompatibles para multiplicación.")
        print("colA: ",colA,"rowB:",rowsB)
        return None
    else:
        for i in range(rowsA):   ###define a matrix of zeros, size rowsA x colB
            result.append([0])
            for j in range(colB-1):
                result[i].append(0)

        for i in range (rowsA):
            for j in range(colB):
                sum=0.0
                for k in range (rowsB):
                    sum=sum+(A[i][k]*B[k][j])
                result[i][j]=sum
        return result
