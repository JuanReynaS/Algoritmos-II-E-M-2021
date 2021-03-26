# Descripción: En este módulo se implementa y ejecuta el algorimo priority 
#              scheduling.
#
#             La ejecución de este módulo se hace a través de la siguiente
#             línea de comando:
#
#             >./priority_scheduling.py <Archivo_entrada>
#
# Creado por: Juan Reyna
# email: 10-10883@usb.ve
# version: 1.0


import matplotlib.pyplot as plt 
import pcpu as pc
import cola_prioridad as prq
import pandas as pd 
import numpy as np
import random as rd
import graphviz as gv
import sys


def  diagrama_gantt(lista):
    """
    Este procedimiento recibe una cola de prioridad y crea un Diagrama de GANTT 
    de la cola dada
    """    

    fig, gnt = plt.subplots() 
     
    # Configuración de limite eje Y.
    gnt.set_ylim(0, len(ids) * 2) 
      
    # Configuración de limite eje x.
    gnt.set_xlim(0, sum(burst)) 
      
    # Etiquelas de eje X e Y.
    gnt.set_xlabel('Segundos desde el comienzo') 
    gnt.set_ylabel('Proceso') 

    # Ejes donde se ubicarán los identificadores de procesos.
    y = [2 * i + 1 for i in range(len(ids))]
    gnt.set_yticks(y) 

    # Etiqueta de los identificadores de procesos. 
    gnt.set_yticklabels(ids) 
      

    gnt.grid(True) 
    colores = ['Orange', 'Blue', 'Red', 'Green', 'Brown', 'Violet', 'Yellow', 'Pink'
                                                                 , 'Beige', 'Black'] 
    tiempo_i = 0
    h = 2
    # Creación de broken_barh de la cola de manera dinámica.
    for i in range(len(lista)):
        iden = ids.index(lista[i].identificador)
        tiempo_f = lista[i].tiempo_quemado
        gnt.broken_barh([(tiempo_i, tiempo_f)], (iden * h , h), 
                                      facecolors =(colores[i]))
        
        tiempo_i = + tiempo_i + tiempo_f
    plt.show()

def diagramas_nodos(lista):
    """
    Este procedimiento recibe una cola de prioridad y crea un grafo con la API
    Graphviz en base a cola de prioridad recibida
    """  

    grafo = gv.Graph(format="svg")
    n = len(lista)

    # Creación de nodos y aristas de manera dinámica
    for i in range(0, n):
        A = lista[i].identificador
        if 2 * i + 1 < n: 
            B = lista[2 * i + 1].identificador
            grafo.edge(A, B)
        if 2 * i + 2 < n:
            C = lista[2 * i + 2].identificador
            grafo.edge(A, C)

    grafo.view()
    grafo.render('/tmp/g1') 



def FCMP(proceso1, proceso2):
    """
    Esta función recibe y compara dos procesos, proceso1, proceso2
    Los valores que retorna FCMP son como sigue:
    
    * 1 si la prioridad del objeto prioridad1 es mayor que la prioridad 
    del objeto prioridad2.

    * 0 si la prioridad del objeto prioridad1 es igual que la prioridad 
    del objeto prioridad2.

    *-1 si la prioridad del objeto prioridad1 es menor que la prioridad 
    del objeto prioridad2.

    """
    if proceso1.prioridad_CPU > proceso2.prioridad_CPU:
        return 1
    
    elif proceso1.prioridad_CPU == proceso2.prioridad_CPU:  
        return 0

    elif proceso1.prioridad_CPU < proceso2.prioridad_CPU:
        return -1

if __name__ == '__main__':
    #Creación de dataframe con los datos de un archivo.
    datos = pd.read_csv(sys.argv[1], names=["Identificador", "Prioridad de CPU",
                                            "Burst time (seg.)", "Tiempo llegada"])
    df_datos = pd.DataFrame(datos)
    print(df_datos)
    ids = sorted(df_datos["Identificador"].tolist())
    burst = sorted(df_datos["Burst time (seg.)"].tolist())
    tiem_lleg = sorted(df_datos["Tiempo llegada"].tolist())
    cola = prq.ColaPrioridad([], FCMP)

    for i in range(len(df_datos)):
        lista = df_datos.iloc[i].tolist()
        cola.insertar(pc.Proceso(lista[0], lista[2], lista[1], lista[3]))

    cola.mostrar()


    diagrama_gantt(cola.arreglo_inicial)
    diagramas_nodos(cola.arreglo_inicial)

    print(cola.extraer_minimo())

    print("EXITOSO")


