import math as mt
import random as rd
import sys


import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
def obtener_rectangulo(P):
    lista_x = []
    lista_y = []
    for x in P:
        lista_x.append(x[0])
        lista_y.append(x[1])

    rectangulo = [(min(lista_x),min(lista_y)), (max(lista_x),min(lista_y)), 
                                               (max(lista_x),max(lista_y)),
                                               (min(lista_x),max(lista_y))]

    
    return rectangulo

def dim_rect(rectangulo):
    X_dim = abs(rectangulo[1][0] - rectangulo[0][0])
    Y_dim = abs(rectangulo[3][1] - rectangulo[0][1])    
    return X_dim, Y_dim

def obtenerPuntoDeCorte(P, ejeDeCorte): # Lista
    n = len(P)
    pos = (n // 2) - 1
    if ejeDeCorte == "X":      
        P.sort()
    elif ejeDeCorte == "Y":
        P.sort(key=lambda comp2: comp2[1])
    return P[pos]

def aplicarParticion(P, ejeDeCorte, pc, rectangulo): #aplicar particion es lo mismo que aplcar corte
    v1, v2, v3, v4 = rectangulo
    if ejeDeCorte == "X":

        rectanguloIzq = obtener_rectangulo([pc, v1, v4])
        rectanguloDer = obtener_rectangulo([pc, v2, v3])

    elif ejeDeCorte == "Y":
        rectanguloIzq = obtener_rectangulo([pc, v3, v4])
        rectanguloDer = obtener_rectangulo([pc, v1, v2])
        

    return (rectanguloIzq, rectanguloDer)


def obtenerPuntosRectangulo(P, rectangulo, ejeDeCorte):
    particion = []
    for x in P:   
        if ejeDeCorte == "X":
            if x in rectangulo:
                particion.append(x)
            elif  ((rectangulo[0][0] <= x[0] <= rectangulo[1][0])  and
                   (rectangulo[0][1] <= x[1] <= rectangulo[3][1])):
                particion.append(x)   

        elif ejeDeCorte == "Y":


            if x in rectangulo:
                particion.append(x)
            elif  ((rectangulo[0][0] <= x[0] <= rectangulo[1][0]) and 
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
        return [(P[0], P[1]), (P[0], P[1]), (P[0], P[2]), (P[1], P[2])]#cicloTresCiudad(P)
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
    particionIzq = obtenerPuntosRectangulo(P, rectanguloIzq, ejeDeCorte) 
    
    P.remove(p_c)
    particionDer = obtenerPuntosRectangulo(P, rectanguloDer, ejeDeCorte) 

    if ((len(particionIzq) == 0 and len(particionDer) > 3) or
           (len(particionIzq) > 3 and len(particionDer) == 0)): 

        if ejeDeCorte == "X": 
            ejeDeCorte = "Y" 
        else:
            ejeDeCorte = "X" 
        
        p_c = obtenerPuntoDeCorte(P, ejeDeCorte)
        (rectanguloIzq, rectanguloDer) = aplicarParticion(P, ejeDeCorte, p_c, rectangulo)
        particionIzq = obtenerPuntosRectangulo(P, rectanguloIzq, ejeDeCorte) 
        particionDer = obtenerPuntosRectangulo(P, rectanguloDer, ejeDeCorte) 
        
        if ((len(particionIzq) == 0 and len(particionDer) > 3) or
           (len(particionIzq) > 3 and len(particionDer) == 0)):

            p_c = rd.choice(P)
            (rectanguloIzq, rectanguloDer) = aplicarParticion(P, ejeDeCorte, p_c, rectangulo)
            particionIzq = obtenerPuntosRectangulo(P, rectanguloIzq, ejeDeCorte) 
            particionDer = obtenerPuntosRectangulo(P, rectanguloDer, ejeDeCorte) 

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

    C1, C2 = 0, 0

    while C1 < len(ciclo1):    
        if ciclo1[C1] == ladosEliminarC1:       
            ciclo1.pop(C1)
        else:
            C1 = C1 + 1
   
    while C2 < len(ciclo2):    
        if ciclo2[C2] == ladosEliminarC2:       
            ciclo2.pop(C2)
        else:
            C2 = C2 + 1
    
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
        ciudades.append((int(float(linea[0])),int(float(linea[1]))))
f.close()
ciudadesB = ciudades[:]
print("ciudades", ciudades)

TS = divideAndConquerTSP(ciudades)
suma = 0
for lados in TS:
    suma = suma + distancia(lados[0], lados[1])

print("\nTour solución valida: \n{}".format(TS))
print("La distancia del Tour solución es: {}".format(suma))





#print("ciudadesB",ciudadesB)
v = ciudadesB[0]
g = []
t = []
for l in range(len(TS)):
    for i in TS:
        #print("v, i",v, i)
        if v == i[0]:
            g.append(i[1])
        elif v == i[1]:
            g.append(i[0])
    #print("g",g)

    if len(t) <= (len(TS)//2)+2:
        t.append(v)
        t.append(max(g))
        v = max(g)
    else:
        t.append(v)
        t.append(min(g))
        v = min(g)        
    g = []
    #print("t", t)
print("\nPAR",t, len(t))

listada = []
for i in TS:
    if type(i) == tuple:
        listada.extend(i)

print("lo que queda", listada)







#puntosSOL = [(1, 1), (0, 9), (0, 9), (3, 8), (3, 8),  (6, 6), (6, 6), (10, 7), (10, 7), (7, 3), (7, 3), (5, 1), (5, 1), (4, 0), (1, 1)]
#print("puntosSOL", puntosSOL)
puntos_x, puntos_y = zip(*listada)
plt.figure()

resp = input("Imprimir Y/N")
if resp == "y":
    plt.title("Recorrido entre ciudades")
    plt.plot(puntos_x,puntos_y, 'o-')
    plt.show()
