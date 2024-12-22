import sigmoid
import siggradient
import costfunct

pixeles=20
canvas=600

matrix=[]
for i in range (pixeles):
    matrix.append([])
    for j in range (pixeles):
        matrix[i].append(0)


#Done bias a1=[[int]] es una lista dentro de una lista, porque hace parte de una matriz columna.
#Done a1=[]        #Input layer. Matriz de (400x1):  (pixeles^2 x 1).  matriz vertical:  [[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],...,[0],[0],[0],[0],[0],[0],[0],[0],[0],[0]]
#Done theta1=[]    #tetha para obtener a2 (25x401) incluyendo al bias
#Done bias a2=int
#Done a2=[]       #hidden layer: theta1*a1:  (25x1)  a2[1]=sigmoide(a1*t1+a2*t2+t3*a3...)    a2[2]=sigmoide(a1*t1+a2*t2+t3*a3...)
#Done theta2=[]   #tetha para obtener a3 (10x26)
#Done a3=[]       #Output layer: theta2*a2:  (10x1)

###########################################################################################
#Inicializacion de matrices Theta:



def printmatrix(matrix):
    if matrix==None:
        print("[]")
        return
    print("rows",len(matrix)),
    print("columns",len(matrix[0]))
    for i in range (len(matrix)):
        for j in range(len(matrix[0])):
            print( matrix[i][j]),
        print("")
    print("")

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



def epsilon_init(prevLay,nextLay):  ### el epsilon es usado para llenar las matrices theta con valores dentro del rango [-epsilon, epsilon].  esto depende de la formula siguiente.
    return (sqrt(6)/sqrt(prevLay+nextLay))


theta1=[]  #matriz de 25x401 inicializado con los valores de epsilon_init.
epsilon=epsilon_init(401,25)
for i in range (25):
    theta1.append([])
    for j in range (401):
        theta1[i].append(random(-epsilon,epsilon))

theta2=[]  #matriz de 10x26 inicializado con los valores de epsilon_init.
epsilon2=epsilon_init(26,10)
for i in range (10):
    theta2.append([])
    for j in range (26):
        theta2[i].append(random(-epsilon2,epsilon2))

b1=random(0,0.1)
b2=random(0,0.1)
biasa1=[[b1]]
biasa2=[[b2]]


a1=[]          ###se inicializa el vector de entrada a1.
for i in range (pixeles**2):
    a1.append([0])


  
backpropagationInProgress = False
      
def dibujarCanvas():
    #Cuando el mouse se presiona, se actualiza la matriz, el canvas, y el vector de entrada.
    if mousePressed and (mouseButton == LEFT): 
        if 0 <= mouseX < width/2 and 0 <= mouseY < height:
            fill(0)
            square((mouseX/(width/2/pixeles))*(width/2/pixeles),(mouseY/(height/pixeles))*(height/pixeles),width/pixeles/2)
            matrix[(mouseY/(height/pixeles))][(mouseX/(width/pixeles/2))]=1
            a1[(mouseX/(width/pixeles/2))+(pixeles*(mouseY/(height/pixeles)))][0]=1


def capturarEntrada():
    global backpropagationInProgress, A3,A2
    #Se borra la matriz, el canvas y a1 con, right clic.

    if mousePressed and (mouseButton == RIGHT):  
        for i in range (pixeles):    #para la matriz y a1
            for j in range (pixeles):
                matrix[i][j]=0
                a1[i+(pixeles*j)][0]=0                
        for x in range(pixeles):    #para el canvas
            for y in range(pixeles):
                stroke(100,100,100)
                fill(255)
                square(x*int(width/pixeles/2),y*int(height/pixeles),width/pixeles/2) 
                
    if keyPressed  and not backpropagationInProgress: ## Solo ejecuta backpropagation si no está en progreso
        if key == '1':  # Tecla 1
            uno=[[1],[0],[0],[0],[0],[0],[0],[0],[0],[0]]
            backpropagationInProgress = True
            ejecutarBackpropagation(uno)
    if keyPressed  and not backpropagationInProgress: ## Solo ejecuta backpropagation si no está en progreso
        if key == '2':  # Tecla 1
            dos=[[0],[1],[0],[0],[0],[0],[0],[0],[0],[0]]
            backpropagationInProgress = True
            ejecutarBackpropagation(dos)
    if keyPressed  and not backpropagationInProgress: ## Solo ejecuta backpropagation si no está en progreso
        if key == '3':  # Tecla 1
            tres=[[0],[0],[1],[0],[0],[0],[0],[0],[0],[0]]
            backpropagationInProgress = True
            ejecutarBackpropagation(tres)
    if keyPressed  and not backpropagationInProgress: ## Solo ejecuta backpropagation si no está en progreso
        if key == '4':  # Tecla 1
            cuatro=[[0],[0],[0],[1],[0],[0],[0],[0],[0],[0]]
            backpropagationInProgress = True
            ejecutarBackpropagation(cuatro)
    if keyPressed  and not backpropagationInProgress: ## Solo ejecuta backpropagation si no está en progreso
        if key == '5':  # Tecla 1
            cinco=[[0],[0],[0],[0],[1],[0],[0],[0],[0],[0]]
            backpropagationInProgress = True
            ejecutarBackpropagation(cinco)
    if keyPressed  and not backpropagationInProgress: ## Solo ejecuta backpropagation si no está en progreso
        if key == '6':  # Tecla 1
            seis=[[0],[0],[0],[0],[0],[1],[0],[0],[0],[0]]
            backpropagationInProgress = True
            ejecutarBackpropagation(seis)
    if keyPressed  and not backpropagationInProgress: ## Solo ejecuta backpropagation si no está en progreso
        if key == '7':  # Tecla 1
            siete=[[0],[0],[0],[0],[0],[0],[1],[0],[0],[0]]
            backpropagationInProgress = True
            ejecutarBackpropagation(siete)
    if keyPressed  and not backpropagationInProgress: ## Solo ejecuta backpropagation si no está en progreso
        if key == '8':  # Tecla 1
            ocho=[[0],[0],[0],[0],[0],[0],[0],[1],[0],[0]]
            backpropagationInProgress = True
            ejecutarBackpropagation(ocho)
    if keyPressed  and not backpropagationInProgress: ## Solo ejecuta backpropagation si no está en progreso
        if key == '9':  # Tecla 1
            nueve=[[0],[0],[0],[0],[0],[0],[0],[0],[1],[0]]
            backpropagationInProgress = True
            ejecutarBackpropagation(nueve)
    if keyPressed  and not backpropagationInProgress: ## Solo ejecuta backpropagation si no está en progreso
        if key == '0':  # Tecla 1
            cero=[[0],[0],[0],[0],[0],[0],[0],[0],[0],[1]]
            backpropagationInProgress = True
            ejecutarBackpropagation(cero)
    if mousePressed and (mouseButton == CENTER): 
        ejecutarForwardPropagation()
    if keyPressed : ## Solo ejecuta backpropagation si no está en progreso
        if key == 's':  # Tecla 1
            print(theta1)
            print(theta2)


        
def ejecutarForwardPropagation():
    A1=biasa1+a1             #a la entrada(columna) le añado el bias.
    a2=matrixMultp(theta1,A1)  #forward propagation, etapa 1, entrada x theta1 = hidden layer.
    A2=biasa2+a2  
    A2=sigmoid.sigmoid(A2)            #obtengo la hidden layer real (con bias).
    A3=sigmoid.sigmoid(matrixMultp(theta2,A2))  #obtengo la output layer. (la pongo en mayuscula, esta no necesita bias.)       
    
    print('Prediccion: ',0 if (A3.index(max(A3))+1)==10 else (A3.index(max(A3))+1))
    #printmatrix(A3)
    dibujoCapa(800,70,A2)
    dibujoCapa(1000,70,A3)

           
def dibujoCapa(xpos, ypos,capa):
    for indice in range(len(capa)):
        fill(map(capa[indice][0],0,1,0,255))
        square(xpos,ypos+indice*15,15)
        
def ejecutarBackpropagation(Y):
    global theta1, theta2, backpropagationInProgress
    #Forward propagation:
    #Primera capa oculta:
    A1=biasa1+a1             #a la entrada(columna) le añado el bias.
    a2=matrixMultp(theta1,A1)  #forward propagation, etapa 1, entrada x theta1.
    A2=biasa2+a2  
    A2=sigmoid.sigmoid(A2)            #obtengo la hidden layer (con bias).
    
    #Capa de salida.
    A3=sigmoid.sigmoid(matrixMultp(theta2,A2))  #obtengo la output layer. (la pongo en mayuscula, esta no necesita bias.)
    
    
    print("Costo:",costfunct.costfunct(Y,A3,0,theta1,theta2))
    print('Prediccion: ',0 if (A3.index(max(A3))+1)==10 else (A3.index(max(A3))+1))
    #printmatrix(A3)

    #Backwards propagation:
        
    delta3=matrixSubstraction(A3,Y)  ##error de la capa de salida (lo que me dio vs lo que debe ser)
    delta2=hadamard( matrixMultp(transpose(theta2),delta3) , siggradient.siggradient(A2) ) ##error de la capa oculta (lo que me dio vs lo que debe ser(backpropagation))
        
    Delta2=[]
    for i in range (1,len(delta2)):
        Delta2.append(delta2[i])
    
    t2grad= matrixMultp(delta3, transpose(A2)) ### no estoy teniendo en cuenta regularizacion. pero es util para evitar sobreajuste
    t1grad= matrixMultp(Delta2, transpose(A1)) ### no estoy teniendo en cuenta regularizacion. pero es util para evitar sobreajuste
    
    tasa=0.05
    
    theta1=matrixSubstraction(theta1,matrizPorEscalar(t1grad,tasa)) 
    theta2=matrixSubstraction(theta2,matrizPorEscalar(t2grad,tasa))
        
    backpropagationInProgress = False
    
    
def setup(): 
    size(canvas*2,canvas)
    background(200,200,200)
    for x in range(pixeles):
        for y in range(pixeles):
            stroke(100,100,100)
            fill(255)
            square(x*int(width/2/pixeles),y*int(height/pixeles),width/pixeles/2)
 
def draw():  
    dibujarCanvas()
    capturarEntrada()


    
    
