import CuckooEntry as ce
import cuckoo_table as ct
import tabla_hash as th
import random as rd
import time as tm
import sys

a, b, c, d = 0, 0, 0, 0
n = int(sys.argv[1])
#n=20000

lista = [rd.randint(0, (2 * n) // 3) for x in range(0,n)]
#print(len(lista))

lista_tupla = [(i,str(i)) for i in lista]
#print(len(lista_tupla))

##########################################################################
print("********** CUCKOO TABLE **********")
print(n, type(n))
tm.sleep(2)

tabla = ct.crearCuckooTable(1021)
inicio = tm.time()
for i in range(len(lista_tupla)):
    key_search = tabla.buscar(lista_tupla[i][0])
    if key_search is None:
        tabla.agregar(lista_tupla[i][0], lista_tupla[i][1])
        a += 1
    else:
        tabla.eliminar(lista_tupla[i][0])
        b += 1
fin = tm.time()

tiempo_ct = fin - inicio
long_ct = tabla.n
#tabla.mostrar()

###########################################################################
print("\n\n********** HASH TABLE **********")
print(n, type(n))
tm.sleep(2)
tabla = th.crear_tabla(1021)
inicio = tm.time()
for i in range(len(lista_tupla)):
    key_search = tabla.buscar(lista_tupla[i][0])
    if key_search is None:
        tabla.agregar(lista_tupla[i][0], lista_tupla[i][1])
        c += 1
    else:
        tabla.eliminar(lista_tupla[i][0])
        d += 1
fin = tm.time()

tiempo_th = fin - inicio
long_th = tabla.n
#tabla.mostrar()

##############################################################################
print("\n********** HASH TABLE **********")
print("* Longitud/Slots de la tabla: {}".format(long_th))
print("* Tiempo de ejecución de la tabla HASH: {}s".format(round(tiempo_th, 2)))
print("* Agregados: {}, Eliminados: {}".format(c, d))
print("* Verificaciones: {}".format(c + d))

print("\n********** CUCKOO TABLE **********")
print("* Longitud/Slots de la tabla: {}".format(long_ct))
print("* Tiempo de ejecución de la Cuckoo tabla: {}s".format(round(tiempo_ct, 2)))
print("* Agregados: {}, Eliminados: {}".format(a,b))
print("* Verificaciones: {}".format(a + b))