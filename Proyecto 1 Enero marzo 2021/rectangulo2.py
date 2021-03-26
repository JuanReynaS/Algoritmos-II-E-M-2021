import math as mt
import random as rd

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
        pc = min([x for x in P if x > pc])
        rectanguloDer = obtener_rectangulo([pc, v2, v3])

    elif ejeDeCorte == "Y":
        rectanguloIzq = obtener_rectangulo([pc, v3, v4])
        pc = (pc[0], pc[1]-1)
        rectanguloDer = obtener_rectangulo([pc, v1, v2])
        
    print("rectangulo Izquierdo",rectanguloIzq)
    print("rectangulo Derecho",rectanguloDer)
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
          
    return particion