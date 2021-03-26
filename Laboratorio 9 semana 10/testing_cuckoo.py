import CuckooEntry as ce
import cuckoo_table as ct
import random as rd
import sys
a, b = 0, 0
n = int(sys.argv[1])
print(n, type(n))
lista = [rd.randint(0, (2 * n) // 3) for x in range(0,n)]
#print(lista)

lista_tupla = [(i,str(i)) for i in lista]
#print(lista_tupla)

tabla = ct.crearCuckooTable(1021)

for i in range(len(lista_tupla)):
	if tabla.buscar(lista_tupla[i][0]) is None:
		tabla.agregar(lista_tupla[i][0], lista_tupla[i][1])
		a += 1
	else:
		tabla.eliminar(lista_tupla[i][0])
		b += 1

tabla.mostrar()
print("Verificaciones: {}".format(a + b))