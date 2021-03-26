import random  as rd
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


def obtenerPuntoDeCorte(P, ejeDeCorte):
    n = len(P)
    pos = (n // 2) - 1
    if ejeDeCorte== "X":
        P.sort()
    elif ejeDeCorte == "Y":
        P.sort(key=lambda comp2: comp2[1])
    return P[pos]

def aplicarParticion(P, ejeDeCorte, pc, rectangulo): #aplicar particion es lo mismo que aplcar corte
    v1, v2, v3, v4 = rectangulo
    if ejeDeCorte == "X":

        rectanguloIzq = obtener_rectangulo([pc, rectangulo[0], rectangulo[3]])
        #pc = min([x for x in P if x > pc])
        rectanguloDer = obtener_rectangulo([pc, rectangulo[1], rectangulo[2]])

    elif ejeDeCorte == "Y":
        rectanguloIzq = obtener_rectangulo([pc, rectangulo[2], rectangulo[3]])
        #pc = (pc[0], pc[1]-1)
        rectanguloDer = obtener_rectangulo([pc, rectangulo[0], rectangulo[1]])
    
    return (rectanguloIzq, rectanguloDer)

def obtenerPuntosRectangulo(P, rectangulo, ejeDeCorte, pc, side):
    particion = []
    for x in P:   
        if ejeDeCorte == "X" and side == "":
            if x in rectangulo:
                particion.append(x)
            elif  ((rectangulo[0][0] <= x[0] <= rectangulo[1][0])  and
                   (rectangulo[0][1] <= x[1] <= rectangulo[3][1])):
                particion.append(x)   

        elif ejeDeCorte == "Y":

            if x in rectangulo  and:
                particion.append(x)
            elif  ((rectangulo[0][0] <= x[0] <= rectangulo[1][0]) and 
                   (rectangulo[0][1] <= x[1] <= rectangulo[3][1])):
                particion.append(x)     
          
    return particion

def obtenerParticiones(P): # Lista
    rectangulo, Xdim, Ydim = obtener_rectangulo(P) 
 
    if Xdim >  Ydim:
        ejeDeCorte = "X"
    else:
        ejeDeCorte = "Y"
    p_c = obtenerPuntoDeCorte(P, ejeDeCorte)

    (rectanguloIzq, rectanguloDer) = aplicarParticion(P, ejeDeCorte, p_c, rectangulo)
    particionIzq = obtenerPuntosRectangulo(P, rectanguloIzq, ejeDeCorte) 
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


coord = [(1,1), (0,9), (3,8), (4,0), (6,6), (10,7), (5,1), (7,3)]
rectangulo = obtener_rectangulo(coord)
lx, ly= dim_rect(rectangulo)

pedIzquierdo, pedDerecho = aplicarParticion(coord, "X", 
                                            obtenerPuntoDeCorte(coord,"X"), 
                                            rectangulo)
print(rectangulo)
print("Longitud x: {}".format(lx))
print("Longitud y: {}".format(ly))
if lx>ly:
    pc = obtenerPuntoDeCorte(coord,"X")
    print(pc)
    print("Punto de corte eje X")
    pedIzquierdo, pedDerecho = aplicarParticion(coord, "X", pc, rectangulo)
    print("Pedazzo izquierdo de la partición", pedIzquierdo)
    print("Pedazzo derecho de la partición", pedDerecho)
    print("\nPuntos interior rectangulo  Izquierdo eje X", obtenerPuntosRectangulo(coord,pedIzquierdo, "X", pc))
    print("Puntos interior rectangulo Derecho eje X", obtenerPuntosRectangulo(coord,pedDerecho, "X", pc))
else:
    pc = obtenerPuntoDeCorte(coord,"Y")
    print("Punto de corte eje Y",pc)
    pedIzquierdo, pedDerecho = aplicarParticion(coord, "Y", pc, rectangulo)
    print("Pedazo izquierdo de la partición", pedIzquierdo)
    print("Pedazo derecho de la partición", pedDerecho)
    print("\nPuntos interior rectangulo  derecho eje Y", obtenerPuntosRectangulo(coord,pedIzquierdo, "Y", pc))
    print("Puntos interior rectangulo izuierdo eje Y", obtenerPuntosRectangulo(coord,pedDerecho, "Y", pc))        
####################################################################################################



print("#######################################################################\n")
coord = [(5,1), (6,6),(7,3), (10,7)]
rectangulo = obtener_rectangulo(coord)
lx, ly= dim_rect(rectangulo)


pedIzquierdo, pedDerecho = aplicarParticion(coord, "X", 
                                            obtenerPuntoDeCorte(coord,"X"), 
                                            rectangulo)
print(rectangulo)
print("Longitud x: {}".format(lx))
print("Longitud y: {}".format(ly))
if lx>ly:
    print("Punto de corte eje X",obtenerPuntoDeCorte(coord,"X"))
    pedIzquierdo, pedDerecho = aplicarParticion(coord, "X", obtenerPuntoDeCorte(coord,"X"), rectangulo)
    print("Pedazzo izquierdo de la partición", pedIzquierdo)
    print("Pedazzo derecho de la partición", pedDerecho)
    print("\nPuntos interior rectangulo  derecho eje X", obtenerPuntosRectangulo(coord,pedIzquierdo, "X"))
    print("Puntos interior rectangulo izuierdo eje X", obtenerPuntosRectangulo(coord,pedDerecho, "X"))
else:
    pc = obtenerPuntoDeCorte(coord,"Y")
    print("Punto de corte eje Y",pc)
    pedIzquierdo, pedDerecho = aplicarParticion(coord, "Y", pc, rectangulo)
    print("Pedazo derecho de la partición", pedDerecho)
    print("\nPuntos interior rectangulo  derecho eje X", obtenerPuntosRectangulo(coord,pedIzquierdo, "Y", pc))
    print("Puntos interior rectangulo izuierdo eje X", obtenerPuntosRectangulo(coord,pedDerecho, "Y", pc))      

