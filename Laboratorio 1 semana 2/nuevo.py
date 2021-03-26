import sys		#Importando este modulo podremos recibir argumentos desde promt
import os		#Importando este modulo podremos manejar archivos en el disco duro
from time import time 	#Importando este modulos podremos manejar las funciones de tiempo en el sistema
from QuickSort import * 				#Modulo creado con el algoritmo de ordenamiento Heap
from Manejo_archivos import *

seguir = True
Archivo = sys.argv[1:]			#Eliminamos el primer indice de la lista que contiene el nombre QuickSort.py para quedarnos solo con los argumentos introducidos en el promt 
ArchivoStr = "".join(Archivo)	#Convertimos la lista "archivo_recibido" en una cadena	
VectorArchivo = Vector_elementos_archivos(ArchivoStr)
LongitudVector = len(VectorArchivo)				#Calculamos la longitud del vector creado en la linea anterior
inicio = time()						########################################################################
VectorOrdenado = QuickSort(VectorArchivo,0,LongitudVector - 1) 		#	Calculamos el tiempo de ejecucion del algoritmo de ordenamiento que 
tiempo = (time() - inicio) * 1000000000000000000000000000000000000000000000000000000000000					#	se encuentra en el modulo QuickSort 
Correctitud(VectorOrdenado)
print("QuickSort",LongitudVector, tiempo)	#Imprimimos los que nos solicitan
inicio = time()						########################################################################
VectorOrdenadoA = RandomizedQuicksort(VectorArchivo,0,LongitudVector - 1) 		#	Calculamos el tiempo de ejecucion del algoritmo de ordenamiento que 
tiempo = (time() - inicio) * 1000000000000000000000000000000000000000000000000000000000000					#	se encuentra en el modulo QuickSort
print("RandomizedQuicksort",LongitudVector, tiempo) #Imprimimos los que nos solicitan

print("¿Desea generar archivos y ordenarlos con QuickSort y RandomizedQuicksort?\n1. Si\n2. No")
N = int(input(""))

if N == 1:
	os.system( "cls" )
	pregunta3()
elif N == 2:
	pass


	