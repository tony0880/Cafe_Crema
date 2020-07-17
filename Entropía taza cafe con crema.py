#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-Importaciones de las bibliotecas-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#

import random
import matplotlib.pyplot as plt
import numpy
import math
import pylab 


#-------------------------------------------------------------FORMACIÓN DE MATRICES-------------------------------------------------------------#


#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-Función principal para la formación de las matrices-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#

def mov_particula (posx, posy, mat):
    #El bucle examina la matriz de izquierda a derecha y de arriba hacia abajo.
    while posy < n:        
        while posx < n:            
            if mat[posy][posx] == 1:
                new_mat = donde_mueve (posx, posy, mat)
                posx = posx + 1                    
            #Si en la posición dada hay un cero, el bucle pasa a la siquiente posición.
            else:            
                posx = posx + 1            
        #Una vez examinadas todas las casillas de una fila, se examina la siguiente fila comenzando desde la columna 0.      
        else:               
            posx = 0
            posy = posy + 1      
    #Una vez completada la iteración se iguala la matriz original a la editable y se repite el proceso hasta completar las iteraciones deseadas.        
    else: 
        posx = 0
        posy = 0 
        mat = new_mat
        return (mat)

#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-Función para determinar el movimiento de la partícula-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#       

def donde_mueve (posx, posy, mat):
    xy = random.randint(1, 2) 
    #Caso para cuando el movimiento es horizontal.
    if xy == 1: 
        #Si la partícula se encuentra en el extremo izquierdo, esta solo puede moverse a la derecha  
        if posx == 0:
            #La variable r determina si la partícula se mueve en cierta dirección o si se queda quieta
            r = random.randint(0, 1)       
            if al_lado(posx + r, posy, mat) == True:
                mat[posy][posx] = 1
                return (mat)
            else:
                mat[posy][posx] = 0
                mat[posy][posx + r] = 1
                return (mat)
        #Si la partícula se encuentra en el extremo derecho, esta solo puede moverse a la izquierda        
        elif posx == n - 1: 
            r = random.randint(-1, 0)
            if al_lado(posx + r, posy, mat) == True:
                mat[posy][posx] = 1
                return (mat)
            else:
                mat[posy][posx] = 0
                mat[posy][posx + r] = 1
                return (mat)
        else:
            r = random.randint(-1, 1)
            if al_lado(posx + r, posy, mat) == True:
                mat[posy][posx] = 1
                return (mat)
            else:
                mat[posy][posx] = 0
                mat[posy][posx + r] = 1
                return (mat)
    #Caso para cuando el movimiento es vertical
    else: 
        #Si la partícula se encuentra en el extremo superior, esta solo puede moverse hacia abajo          
        if posy == 0:       
            r = random.randint(0, 1)
            if al_lado(posx, posy + r, mat) == True:
                mat[posy][posx] = 1
                return (mat)
            else:
                mat[posy][posx] = 0
                mat[posy + r][posx] = 1
                return (mat)
        #Si la partícula se encuentra en el extremo inferior, esta solo puede moverse hacia arriba
        elif posy == n - 1:     
            r = random.randint(-1, 0)
            if al_lado(posx, posy + r, mat) == True:
                mat[posy][posx] = 1
                return (mat)
            else:        
                mat[posy][posx] = 0                    
                mat[posy + r][posx] = 1
                return (mat)
        else:
            r = random.randint(-1, 1)
            if al_lado(posx, posy + r, mat) == True:
                mat[posy][posx] = 1
                return (mat)
            else:
                mat[posy][posx] = 0
                mat[posy + r][posx] = 1
                return (mat)


#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
#-#-#-#-#-#-#-#-#-#-#-#-#-#-Función que verifica si en la posición dada se encuentra ya una partícula o no en la matriz-#-#-#-#-#-#-#-#-#-#-#-#-#

def al_lado (posx, posy, mat):
    if mat[posy][posx] == 1:
        return True
    else:
        return False


#--------------------------------------------------------------CALCULO DE ENTROPIA--------------------------------------------------------------#        


#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-Función que determina cuantas partículas hay en una celda-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#

def cafe_leche (posx, posy, mat, lista_particulas, iteracion, lista_entropia):
    while iteracion <= iteraciones:
        if iteracion == 11 or iteracion == 101 or iteracion == 1001 or iteracion == 10001:
            grafica_matriz (mat, iteracion)
            grafica_entropia (lista_entropia, iteracion)
        #Se utiliza la función para generar matrices, elaborada con anterioridad.
        mat = mov_particula (0, 0, mat)
        while posy < n:
            while posx < n:
                #Se generan celdas, donde cada una es un estado para la partícula.
                celda = mat[posy : posy + tamano_subcelda, posx : posx + tamano_subcelda]
                posx = posx + tamano_subcelda
                #Se crea una lista con la cantidad de partículas que hay por cada celda.
                lista_particulas = lista_particulas + [cant_part (celda, 0, 0, tamano_subcelda)]
            else:
                posx = 0
                posy = posy + tamano_subcelda
        else:
            #Una vez analizada toda la matriz se crea una lista con los valores de entropía para cada matriz.
            lista_entropia = lista_entropia + [calc_entropia (lista_particulas, 0, 0, 0)]
            posy = 0
            posx = 0
            lista_particulas = []
            iteracion = iteracion + 1
    else:
        #Finalmente se retorna una lista con todos los valores de entropía para cada iteración.
        grafica_matriz (mat, iteracion)
        grafica_entropia (lista_entropia, iteracion)   
           


        
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-Función que determina cuantas partículas hay en una celda-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#

def calc_entropia (lista_particulas, cant_celdas, prob, entropia):
    #Toma la catidad de partículas por cada celda y calcula su probabilidad, 
    #la cual es la cantidad de partículas de la celda divido entre el total de partícula en la matriz.
    while cant_celdas < (n**2/tamano_subcelda**2): 
        prob = lista_particulas [cant_celdas]/(tamano_subcelda**2)
        if prob == 0:
            cant_celdas = cant_celdas + 1
        #Se calcula la entropía con la formulación de Gibbs.
        else:
            logaritmo = math.log(prob)
            entropia = entropia - prob * logaritmo
            prob = 0
            cant_celdas = cant_celdas + 1
    else:
        return entropia
        
        

#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-Función que determina cuantas partículas hay en una celda-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#

def cant_part (celda, x_celda, y_celda, tamano_subcelda):
    #Toma una celda dada y cuenta cuantas partículas hay en ella
    part_celda = 0
    while y_celda < tamano_subcelda:
        while x_celda < tamano_subcelda:
            if celda [y_celda][x_celda] == 0:
                x_celda = x_celda + 1
            else:
                x_celda = x_celda + 1
                part_celda = part_celda + 1
        else:
            y_celda = y_celda + 1
            x_celda = 0
    else:
        y_celda = 0
        x_celda = 0
        return part_celda


#--------------------------------------------------------------GRAFICACIÓN DE DATOS-------------------------------------------------------------#        


#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-Función que grafica los datos generados-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#

def grafica_entropia (lista_entropia, iteracion):
    pylab.title("Evolucion de entropía a " + str(iteracion - 1) + " pasos") 
    pylab.xlabel ("Pasos")
    pylab.ylabel ("Entropía") 
    pylab.plot(list(range(1, iteracion)), lista_entropia)
    pylab.savefig("cafe con leche a " + str(iteracion - 1) + " pasos.png",bbox_inches="tight",dpi=600)
    pylab.show()

#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-Función que grafica la matriz-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#

def grafica_matriz (mat, iteracion):
    pylab.title('matriz a ' + str(iteracion - 1) + ' pasos') 
    y =  numpy.where (mat ==1) [0]
    x =  numpy.where (mat ==1) [1]
    plt.plot (x, y, 'bs')
    plt.xlim (0, n)
    plt.ylim (0, n)
    pylab.savefig("matriz a " + str(iteracion - 1) + " pasos.png",bbox_inches="tight",dpi=600)
    plt.show ()


#-----------------------------------------------------------------DATOS INCIALES----------------------------------------------------------------#


#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-Valores editables-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#

n = 100
iteraciones = 200
tamano_subcelda = 10

#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-Valores no editables-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#

lista_iteraciones = []
lista_entropia = [] 
lista_particulas = []
iteracion = 1
posx = 0
posy = 0

#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-Definición de la matriz principal y la editable-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#

mat = numpy.arange(n**2).reshape(n, n)
mat[0:, ::1] = 0
mat[(n//2)-tamano_subcelda//2:(n//2)+tamano_subcelda//2, (n//2)-tamano_subcelda//2:(n//2)+tamano_subcelda//2] = 1
#Se guarda para tener el valor original de la matriz
grafica_matriz (mat, iteracion)         

new_mat = numpy.arange(n**2).reshape(n, n)
new_mat[0:, ::1] = 0

#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-Ejecución del programa-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#

cafe_leche (posx, posy, mat, lista_particulas, iteracion, lista_entropia)