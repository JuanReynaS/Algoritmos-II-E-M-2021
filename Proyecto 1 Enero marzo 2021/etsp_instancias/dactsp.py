# Descripción: En este módulo se ejecuta las diversas pruebas de exigidas por
#
#
# Ejecución del programa: >./dactsp.py archivo_entrada archivo_salida


# Creado por: Juan Reyna
# email: 10-10883@usb.ve
# version: 1.0

import math as mt
import random as rd
import sys


import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

sys.setrecursionlimit(999999)

def obtener_rectangulo(P): 
    """ Dado un conjunto de puntos se obtine el rectangulo de menor área que con tiene 
		a todos esos puntos
    """
    lista_x = []
    lista_y = []
    for x in P:
        lista_x.append(x[0])
        lista_y.append(x[1])

    if len(lista_x) > 0  and len(lista_y) > 0:
        x_min = min(lista_x)
        y_min = min(lista_y)  
        x_max = max(lista_x)
        y_max = max(lista_y)  
        rectangulo = [(x_min, y_min), (x_max, y_min), (x_max, y_max) 
                                                    , (x_min, y_max)]
    
    elif len(lista_x) == 0  and len(lista_y) == 0:
        rectangulo = []

    return rectangulo


def dim_rect(rectangulo):
    """ Recibe un rectángulo y calcula las longitudes de sus lados""" 
    X_dim = abs(rectangulo[1][0] - rectangulo[0][0])
    Y_dim = abs(rectangulo[3][1] - rectangulo[0][1])    
 
    return X_dim, Y_dim

def obtenerPuntoDeCorte(P, ejeDeCorte): 
    """Esta función recibe un conjunto de puntos y un eje del plano cartesiano y
	   devuelve el punto ubicado en el medio de el conjunto
    """
    n = len(P)
    pos = (n // 2) - 1
    if ejeDeCorte == "X":      
        P.sort()
    elif ejeDeCorte == "Y":
        P.sort(key=lambda comp2: comp2[1])
    return P[pos]

def aplicarParticion(P, ejeDeCorte, pc, rectangulo):
	"""Esta función recibe un rectangulo con sus puntos interiores y
		devuelve dos rectangulos mas pequeños que se origina la dividir el rectángulo
		recibido con una  recta perpendicular al eje dado por el pon de corte pc
		}
	"""
    v1, v2, v3, v4 = rectangulo
    P.sort()
    
    if ejeDeCorte == "X":
        P.sort()
        indice_pc = P.index(pc)
        rectanguloIzq = obtener_rectangulo(P[:indice_pc + 1])
        rectanguloDer = obtener_rectangulo(P[indice_pc + 1:])
        
    elif ejeDeCorte == "Y":
        
        P.sort(key=lambda comp2: comp2[1])
        indice_pc = P.index(pc)
        rectanguloIzq = obtener_rectangulo(P[:indice_pc + 1])
        rectanguloDer = obtener_rectangulo(P[indice_pc + 1:])


    return (rectanguloIzq, rectanguloDer)


def obtenerPuntosRectangulo(P, rectangulo):
	"""Esta función obtiene los puntos interioes de un rectángulo dado"""
    particion = []
    if len(rectangulo) == 0:
        pass
    else:
        for x in P:   
            if x in rectangulo:
                particion.append(x)
            elif  ((rectangulo[0][0] <= x[0] <= rectangulo[1][0])  and
                    (rectangulo[0][1] <= x[1] <= rectangulo[3][1])):
                    particion.append(x)   

    return (particion)


def divideAndConquerTSP(P): 
    n = len(P)
    if n == 0:
        return []
    elif n == 1:
        return [(P[0], P[0])] #cicloUnaCiudad(P)
    elif n == 2:
        return [(P[0], P[1]), (P[0], P[1])] #cicloUnaCiudad(P)
    elif n == 3:
        return [(P[0], P[1]), (P[0], P[2]), (P[1], P[2])]#cicloTresCiudad(P)
    else:
        pderecha, pizquierda = obtenerParticiones(P)
        c1 = divideAndConquerTSP(pderecha)
        c2 = divideAndConquerTSP(pizquierda)
        return combinarCiclos(c1, c2)


def obtenerParticiones(P):
    rectangulo = obtener_rectangulo(P) 
    Xdim, Ydim = dim_rect(rectangulo) 
    if Xdim >  Ydim:
        ejeDeCorte = "X"
    else:
        ejeDeCorte = "Y"
    p_c = obtenerPuntoDeCorte(P, ejeDeCorte)

    (rectanguloIzq, rectanguloDer) = aplicarParticion(P, ejeDeCorte, p_c, rectangulo)
    particionIzq = obtenerPuntosRectangulo(P, rectanguloIzq) 
    
    
    particionDer = obtenerPuntosRectangulo(P, rectanguloDer) 

    if ((len(particionIzq) == 0 and len(particionDer) > 3) or
           (len(particionIzq) > 3 and len(particionDer) == 0)): 

        if ejeDeCorte == "X": 
            ejeDeCorte = "Y" 
        else:
            ejeDeCorte = "X" 
        
        p_c = obtenerPuntoDeCorte(P, ejeDeCorte)
        (rectanguloIzq, rectanguloDer) = aplicarParticion(P, ejeDeCorte, p_c, rectangulo)
        particionIzq = obtenerPuntosRectangulo(P, rectanguloIzq) 
        
        particionDer = obtenerPuntosRectangulo(P, rectanguloDer) 
        
        if ((len(particionIzq) == 0 and len(particionDer) > 3) or
           (len(particionIzq) > 3 and len(particionDer) == 0)):

            p_c = rd.choice(P)
            (rectanguloIzq, rectanguloDer) = aplicarParticion(P, ejeDeCorte, p_c, rectangulo)
            particionIzq = obtenerPuntosRectangulo(P, rectanguloIzq) 
            
            particionDer = obtenerPuntosRectangulo(P, rectanguloDer) 
        particionIzq, particionDer = ([], [])
    
    return (particionIzq, particionDer)

def combinarCiclos(ciclo1, ciclo2):
    n = len(ciclo1)
    m = len(ciclo2)

    if n == 0:
        return ciclo2
    if m == 0:
        return ciclo1

    minG = float("inf")
    for ladoC1 in ciclo1:     
        dold1 = distancia(ladoC1[0], ladoC1[1])

        for ladoC2 in ciclo2:

            dold2 = distancia(ladoC2[0],ladoC2[1])#
            dnew1 = distancia(ladoC1[0], ladoC2[0])#
            dnew2 = distancia(ladoC1[1], ladoC2[1])#
            dnew3 = distancia(ladoC1[0], ladoC2[1])#
            dnew4 = distancia(ladoC1[1], ladoC2[0])#
            g1 = distanciaGanada(dold1, dold2, dnew1, dnew2)
            g2 = distanciaGanada(dold1, dold2, dnew3, dnew4)

            ganancia = max(g1, g2)
            if ganancia < minG:
                minG = ganancia
                if g1 < g2:
                    ladosAgregarC1 = (ladoC1[0], ladoC2[0]) #
                    ladosAgregarC2 = (ladoC1[1], ladoC2[1]) #
                else:
                    ladosAgregarC1 = (ladoC1[0], ladoC2[1]) #
                    ladosAgregarC2 = (ladoC1[1], ladoC2[0]) #
                
                ladosEliminarC1 = (ladoC1[0], ladoC1[1]) #
                ladosEliminarC2 = (ladoC2[0], ladoC2[1]) #


    ciclo1.remove(ladosEliminarC1)
    ciclo2.remove(ladosEliminarC2) 
    ciclo3 = []
    ciclo3.append(ladosAgregarC1)
    ciclo3.append(ladosAgregarC2)
    
    if len(ciclo1):
        ciclo3 = ciclo3 + list(ciclo1)
    if len(ciclo2):
        ciclo3 = ciclo3 + list(ciclo2)  
    return sorted(ciclo3) 

def distancia(tupla1, tupla2):

    x_d = tupla1[0] - tupla2[0]
    y_d = tupla1[1] - tupla2[1]
    d_ij = abs(mt.sqrt((x_d * x_d)+ (y_d * y_d)))
    return int(d_ij+0.5)

def distanciaGanada(dOLD1, dOLD2, dNEW1, dNEW2):
    return (dNEW1 + dNEW2) - (dOLD1+dOLD2)

ciudades = []
f=open(sys.argv[1],"r")
f.seek(0)
it=(linea for i,linea in enumerate(f) if  6 <= i)
for linea in it:
    linea = linea.split()
    if len(linea) == 3:
        linea.pop(0)

        ciudades.append((float(linea[0]), float(linea[1])))
f.close()
ciudadesB = ciudades[:]

TS = divideAndConquerTSP(ciudades)
print(len(TS))
ditstancia_recorrida = 0
for lados in TS:
    ditstancia_recorrida = ditstancia_recorrida + distancia(lados[0], lados[1])


nombre_instancia = sys.argv[1].split(sep='.')[0]
print("El nombre de la instancia es: {}".format(nombre_instancia))
print("La distancia del Tour solución es: {}".format(ditstancia_recorrida))

# El coódigo comentado a continuación solo describe el tour para el ejemplo 

"""listada = []
for i in TS:
    if type(i) == tuple:
        listada.extend(i) 

lista = []
for i in listada:
    if not i in lista:
        lista.append(i)    
v = ciudadesB[0]


ciudades_tour = [v] 
for j in range(0,len(lista)):
        for par in TS:

            if v == par[0] and not(par[1] in ciudades_tour):
                ciudades_tour.append(par[1])
                v = par[1]
            elif v == par[1] and not(par[0] in ciudades_tour): 
                ciudades_tour.append(par[0])

lista_tour = []
for i in range(len(ciudadesB)):
    lista_tour.append(ciudadesB.index(ciudades_tour[i]) + 1)

print( len(lista_tour))

lista_tour.append(-1)"""


name = "NAME: " + nombre_instancia + ".out"
comment = "COMMENT: Length " + str(ditstancia_recorrida)
type1 = "TYPE : TOUR"
dimension = "DIMENSION : " + str(len(ciudades))
tour_section = "TOUR_SECTION"

archivo_salida = open(sys.argv[2],"w")

archivo_salida.write(name + "\n")
archivo_salida.write(comment + "\n")
archivo_salida.write(type1 + "\n")
archivo_salida.write(dimension + "\n")
archivo_salida.write(tour_section + "\n")
# El código comentado funciona solo con el ejemplo
# for i in lista_tour:
#    archivo_salida.write(str(i) + "\n")
for i in TS:
	archivo_salida.write(str(i) + "\n")
archivo_salida.write(str(TS) + "\n")
archivo_salida.write("EOF")
archivo_salida.close()


