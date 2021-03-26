# Descripción: En este módulo se implementa una cola de prioridad.
#              Los procesos de menor prioridad serán ejecutados por el procesador 
#
# Creado por: Juan Reyna
# email: 10-10883@usb.ve
# version: 1.0

import sys
import pandas as pd
class ColaPrioridad(object):

    def __init__(self, arreglo_inicial, fcmp):
        self.arreglo_inicial = arreglo_inicial
        self.fcmp = fcmp
        self.n = len(self.arreglo_inicial)
        
    def minimo(self):
        """Retorna el elemento con menor prioridad de la cola"""
        return self.arreglo_inicial[0].prioridad_CPU

    def extraer_minimo(self):
        """Elimina y retorna el elemento con menor prioridad de la cola"""        
        if self.n < 1:
            print("Error: Heap underflow")
            sys.exit()
        else:
            minimo = self.minimo()
            self.n -= 1
            self.arreglo_inicial.pop(0)
            self.disminuir_clave(self.arreglo_inicial[self.n-1],self.n-1)
        return minimo
    
    def disminuir_clave(self, elem, posicion):       
        """Ubica nuevo elemento de cola prioridad en ubicación con menor clave
        """
        A = self.arreglo_inicial    
        parent = posicion // 2   
        i = posicion
        j = posicion - 1
        
        while j > parent - 1 and i > parent :          

            if (self.fcmp(A[i], A[j]) == 0) and A[j].tiempo_llegada > A[i].tiempo_llegada:
                A[i], A[j] = A[j], A[i]
                i = posicion
                j = posicion - 1
            else:
                i = i - 1
                j = j - 1

        while posicion > 0 and (self.fcmp(A[parent], elem) == 1):       
            A[parent], A[posicion] = A[posicion], A[parent]
            elem =  A[parent]
            posicion = parent
            parent = posicion // 2
       
    def insertar(self, elem):
        """Inserta elemento en cola de prioridad"""
        if self.n == 0:
            self.arreglo_inicial.append(elem)
            self.n += 1
        else:
            self.arreglo_inicial.append(elem)
            self.n += 1
            self.disminuir_clave(elem, self.n-1)

    def mostrar(self):
        """ Muestra la cola de prioridad"""
        print("########## Cola Prioridad  ##########")
        for i in range(len(self.arreglo_inicial)):
            print("Proceso", self.arreglo_inicial[i].identificador,self.arreglo_inicial[i].prioridad_CPU,self.arreglo_inicial[i].tiempo_llegada)


