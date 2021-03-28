import CuckooEntry as ce
import cuckoo_table as ct
import tabla_hash as th
import random as rd
import time as tm
import sys
import hashEntry as he
import matplotlib.pyplot as plt


def get_size(obj, seen=None):
    """Recursively finds size of objects"""
    size = sys.getsizeof(obj)
    if seen is None:
        seen = set()
    obj_id = id(obj)
    if obj_id in seen:
        return 0
    # Important mark as seen *before* entering recursion to gracefully handle
    # self-referential objects
    seen.add(obj_id)
    if isinstance(obj, dict):
        size += sum([get_size(v, seen) for v in obj.values()])
        size += sum([get_size(k, seen) for k in obj.keys()])
    elif hasattr(obj, '__dict__'):
        size += get_size(obj.__dict__, seen)
    elif hasattr(obj, '__iter__') and not isinstance(obj, (str, bytes, bytearray)):
        size += sum([get_size(i, seen) for i in obj])
    return size


# n = int(sys.argv[1])
lista_exp = [500000, 1000000, 1500000, 2000000, 2500000, 3000000,
             3500000, 4000000]

# lista_exp = [500000, 700000, 1000000, 1500000]

lista_tiempo_ct = []
lista_mem_ct = []

lista_tiempo_ht = []
lista_mem_ht = []

lista_tiempo_htE = []
lista_mem_htE = []

for n in lista_exp:
    a, b, c, d, e, f = 0, 0, 0, 0, 0, 0
    lista = [rd.randint(0, (2 * n) // 3) for x in range(0, n)]
    lista_tupla = [(i, str(i)) for i in lista]

    ##########################################################################
    print("********** CUCKOO TABLE **********")
    print("Numeros de Elementos a procesar: {}...".format(n))
    tm.sleep(3)

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
    lista_tiempo_ct.append(round(tiempo_ct,3))

    mem_ct = (get_size(tabla.tabla1) + get_size(tabla.tabla2)) / (1024 ** 2)
    lista_mem_ct.append(round(mem_ct,3))

    ###########################################################################
    print("\n\n********** HASH TABLE **********")
    print("Numeros de Elementos a procesar: {}...".format(n))
    tm.sleep(3)
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
    lista_tiempo_ht.append(round(tiempo_th, 3))

    mem_th = get_size(tabla.tabla) / (1024 ** 2)
    lista_mem_ht.append(round(mem_th, 3))

    ###########################################################################
    print("\n\n********** HASH TABLE elementos tipo HashEntry **********")
    print("Numeros de Elementos a procesar: {}...".format(n))
    tm.sleep(3)
    tabla = th.crear_tabla(1021)
    inicio = tm.time()
    for i in range(len(lista_tupla)):
        objeto_te = he.HashEntry(lista_tupla[i][0], lista_tupla[i][1])
        key_search = tabla.buscar(lista_tupla[i][0])
        if key_search is None:
            tabla.agregar_elem(objeto_te)
            e += 1
        else:
            tabla.eliminar_elem(objeto_te)
            f += 1
    fin = tm.time()

    tiempo_thE = fin - inicio
    lista_tiempo_htE.append(round(tiempo_thE, 3))

    mem_thE = get_size(tabla.tabla) / (1024 ** 2)
    lista_mem_htE.append(round(mem_thE, 3))



# #############################################################################

    # print("\n********** HASH TABLE **********")
    # print("* Longitud/Slots de la tabla: {}".format(long_th))
    # print("* Agregados: {}, Eliminados: {}".format(c, d))
    # print("* Elementos procesados: {}".format(c + d))
    # print("* Tiempo de ejecución de la tabla HASH: {} s".format(round(tiempo_th, 2)))
    # print("* Consumo de Memoria de la tabla HASH: {} Mb".format(round(mem_th, 2)))

    # print("\n********** CUCKOO TABLE **********")
    # print("* Longitud/Slots de la tabla: {}".format(long_ct))
    # print("* Agregados: {}, Eliminados: {}".format(a, b))
    # print("* Elementos procesados: {}".format(a + b))
    # print("* Tiempo de ejecución de la Cuckoo tabla: {} s".format(round(tiempo_ct, 2)))
    # print("* Consumo de memoria de la Cuckoo tabla: {} Mb".format(round(mem_ct, 2)))

print("Lista tiempo_th TH\n", lista_tiempo_ht)
print("Lista Memoria HT\n", lista_mem_ht)
print("Lista tiempo_th THE\n", lista_tiempo_htE)
print("Lista Memoria HTE\n", lista_mem_htE)
print("Lista tiempo_th CT\n", lista_tiempo_ct)
print("Lista Memoria CT\n", lista_mem_ct)


plt.title("Tiempo en procesar claves en tabla Hash")
plt.xlabel('Numeros de claves procesados')
plt.ylabel('Tiempo(seg)')
plt.plot(lista_exp, lista_tiempo_ht, 'ro-', label="Hash Table")
plt.plot(lista_exp, lista_tiempo_ct, 'b^-', label="Cuckoo Table")
plt.plot(lista_exp, lista_tiempo_htE, 'g+-', label="Hash tipo Entry")
plt.legend()
plt.show()

plt.title("Memoria usada por las tablas Hash")
plt.xlabel('Numeros de claves procesados')
plt.ylabel('Memoria (Mb)')
plt.plot(lista_exp, lista_mem_ht, 'b^-', label="Hash Table")
plt.plot(lista_exp, lista_mem_ct, 'gs-', label="Cuckoo Table")
plt.plot(lista_exp, lista_mem_htE, 'r+-', label="Hash tipo Entry")
plt.legend()
plt.show()
