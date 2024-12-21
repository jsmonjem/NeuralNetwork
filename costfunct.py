import math

def costfunct(y, hypo, lambda1,t1,t2):
    #la funcion de costo es -1/m de la sumatoria de:       donde m es el numero de ejemplos: se tiene en cuenta en el retorno. en mi caso, el numero de ejemplos es 1 siempre.
    # (y * log de la hypoteisis) + (1-y) por logaritmo de( 1 - la hypotesis)
    #a eso se le suma lambda/(2m) de la sumatoria de theta cuadrado. #esto es la regularizacion: 
    #se penalizan valores de theta grandes. se busca evitar el overfitting.
    #necesito y, (la salida esperada (para conocer el error))
    #theta

    suma=0.0
    lsum=0.0
    for i in range(len(t1)):  ##en esta primera parte hallo el costo de la regularizacion.(incluyendo a theta 1 y 2)
        for j in range (1,len(t1[0])):
            lsum=lsum+t1[i][j]*t1[i][j]
    for i in range(len(t2)):
        for j in range (1,len(t2[0])):
            lsum=lsum+t2[i][j]*t2[i][j]  
    lsum=lsum*(lambda1/2*len(y[0]))        
                                                        
    for i in range(len(y[0])): ##en esta parte, hallo el costo asociado al error entre la hipotesis y la salida real.
        suma=suma+((y[i][0]*math.log(hypo[i][0],math.exp(1)))+  ( (1-y[i][0]) * (math.log(1-hypo[i][0],math.exp(1) )  )  ) )
    return (-suma/len(y[0])+lsum)
