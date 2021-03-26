# Descripción: En este módulo se ejecuta las diversas pruebas de exigidas por
#              el usuario sobre los algoritmos de ordenamiento en el módulo 
#              sortlib.py.
#
#             La ejecución de este módulo se hace a través de la siguiente
#             línea de comando:
#
#             >./ python3 run_sortlib.py -t[#num] -m[#num] -s[tipo] -n[num1 num2 num3 ...] -a [alg]
#
# Creado por: Juan Reyna
# email: 10-10883@usb.ve
# version: 4.0

import getopt as gto
import math
import random
import random as rd
import string as st
import sys
import time
import sortlib as sl

import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def sreal(n):
    """Secuencia de n números reales en el intervalo [0, 1]
       generados aleatoriamente."""
    try:
        assert(n > 0)
        lista = [round(rd.uniform(0, 1), 2) for x in range(0, n)]
        return lista
    except AssertionError:
        print('Error: Indico una longitud para la lista no positiva')


def sortedreal(n):
    """Una secuencia de tipo sreal de longitud n,pero en donde todos
       los elementos están ordenados."""
    try:
        assert(n > 0)
        lista = sorted(sreal(n))
        return lista
    except AssertionError:
        print('Error: Indico una longitud para la lista no positiva')


def invsortedreal(n):
    """Una secuencia de tipo sreal de longitud n, donde todos los
       elementos estan ordenados de forma inversa."""
    try:
        lista = sorted(sreal(n), reverse=True)
        return lista
    except AssertionError:
        print('Error: Indico una longitud para la lista no positiva')
        sys.exit()


def sint(n):
    """Secuencia de n números enteros en el intervalo [0, N] generados
       aleatoriamente, donde N es el tama ̃no de la secuencia a ordenar."""
    try:
        assert (n > 0)
        lista = [rd.randint(0, n) for x in range(n)]
        return lista
    except AssertionError:
        print('Error: Indico una longitud para la lista no positiva')
        sys.exit()


def sortedint(n):
    """Una secuencia de tipo sint de longitud n, pero en donde todos
       los elementos estan ordenados"""
    try:
        assert (n > 0)
        lista = sorted(sint(n))
        return lista
    except AssertionError:
        print('Error: Indico una longitud para la lista no positiva')
        sys.exit()


def invsortedint(n):
    """Una secuencia de tipo sint de longitud n, pero en donde todos
       los elementos estan ordenados de forma inversa"""
    try:
        assert (n > 0)
        lista = sorted(sint(n), reverse=True)
        return lista
    except AssertionError:
        print('Error:Indico una longitud para la lista no positiva')
        sys.exit()


def sstr(n, m):
    try:
        assert (n > 0 and m > 0)
        lista = ["".join([rd.choice(st.printable) for x in range(m)])
                                                    for y in range(n)]
        return lista
    except AssertionError:
        print('Error:Indico una longitud para la lista no positiva')
        sys.exit()


def sortedstr(n, m):
    try:
        assert (n > 0 and m > 0)
        lista = sorted(sstr(n, m))
        return lista
    except AssertionError:
        print('Error:Indico una longitud para la lista no positiva')
        sys.exit()


def invsortedstr(n, m):
    try:
        assert (n > 0 and m > 0)
        lista = sorted(sstr(n, m), reverse=True)
        return lista
    except AssertionError:
        print('Error:Indico una longitud para la lista no positiva')
        sys.exit()


def unocero(n):
    """ Esta función genera una secuencia de tamaño n de uno y ceros
        distribuidos de manera aleatoria"""
    lista = [rd.randint(0, 1) for x in range(0, n)]
    return lista


def SD(lista, media):
    """Dada una lista con el tiempo de ordenamiento de un algoritmo y el
       promedio de los tiempos contenidos en la lista, esta función devolverá
       la desviación estandar de los tiempos de la lista con respecto a su
       promedio"""

    try:
        assert (len(lista) > 0 and media >= 0)
        acumulador = 0
        for i in lista:
            acumulador += (abs(i - media)) ** 2
        return math.sqrt(acumulador / len(lista))
    except AssertionError:
        print('Error:Su longitud o media son no positivos')
        sys.exit()
    except ZeroDivisionError:
        print("¡Error!, su media es cero")


def seleccion_lista(tipo, valN, valM):
    """Dado la longitud de los arreglos (valN), la longitud de los
       strings(valM), esta fuinción devuelve una lista según haya solicitado
       el usuario (tipo)"""
    if tipo == "sreal":
        lista = sreal(valN)
    elif tipo == "sortedreal":
        lista = sortedreal(valN)
    elif tipo == "invsortedreal":
        lista = invsortedreal(valN)
    elif tipo == "sint":
        lista = sint(valN)
    elif tipo == "sortedint":
        lista = sortedint(valN)
    elif tipo == "invsortedint":
        lista = invsortedint(valN)
    elif tipo == "sstr":
        lista = sstr(valN, valM)
    elif tipo == "sortedstr":
        lista = sortedstr(valN, valM)
    elif tipo == "invsortedstr":
        lista = invsortedstr(valN, valM)
    elif tipo == "unocero":
        lista = unocero(valN)
    return lista


def verify_list(list_test):
    """ Esta función verifica si la secuencia recibida como parametro esta
        ordenada, si dicha secuencia no lo está se anula la ejecución del
        programa run_sortlib.py"""

    list_aux = sorted(list_test)
    lista = [x for x in range(0, len(list_test))
                 if list_test[x] != list_aux[x]]
    if lista:
        print("\n***** SU ALGORITMO NO ORDENÓ LA LISTA DADA *****")
        sys.exit()
    else:
        pass


def algoritmos_On2(lista):
    """Este función recibe una lista que será ordenada por los algoritmos
       que con complejidad comutacional de orden On2:
       
       - insertion_sort(lista)
       - bubble_sort(lista)
       - selection_sort(lista)
       - shell_sort(lista)
       
       y devolverá los tiempos resultantes del ordenamiento de la lista según  
       cada algoritmo"""

    lista_apoyo = lista[:]
    lista = lista_apoyo[:]
    inicio = time.time()
    verify_list(sl.insertion_sort(lista))
    fin = time.time()
    tiempo_ins = fin - inicio

    lista = lista_apoyo[:]
    inicio = time.time()
    verify_list(sl.bubble_sort(lista))
    fin = time.time()
    tiempo_bu = fin - inicio

    lista = lista_apoyo[:]
    inicio = time.time()
    verify_list(sl.selection_sort(lista))
    fin = time.time()
    tiempo_se = fin - inicio

    lista = lista_apoyo[:]
    inicio = time.time()
    verify_list(sl.shell_sort(lista))
    fin = time.time()
    tiempo_she = fin - inicio

    return tiempo_ins, tiempo_bu, tiempo_se, tiempo_she


def algoritmos_nlgn(lista):
    """Este función recibe una lista que será ordenada por los algoritmos
       que con complejidad computacional de orden nlgn:
       
       - mergesort(lista)
       - mergesort_iterativo(lista)
       - mergesort_three(lista)
       - mergesort_opt(lista)
       - quicksort_iterativo(lista)
       - quicksort(lista)
       - randomized_quicksort(lista)
       
       y devolverá los tiempos resultantes del ordenamiento de la lista según  
       cada algoritmo"""


    lista_apoyo = lista[:]
    inicio = time.time()
    verify_list(sl.mergesort(lista))
    fin = time.time()
    t_mer = fin - inicio

    lista = lista_apoyo[:]
    inicio = time.time()
    verify_list(sl.mergesort_iterativo(lista))
    fin = time.time()
    t_mer_it = fin - inicio

    lista = lista_apoyo[:]
    inicio = time.time()
    verify_list(sl.mergesort_three(lista))
    fin = time.time()
    t_mer_thr = fin - inicio

    lista = lista_apoyo[:]
    inicio = time.time()
    verify_list(sl.mergesort_opt(lista))
    fin = time.time()
    t_mer_opt = fin - inicio

    lista = lista_apoyo[:]
    inicio = time.time()
    verify_list(sl.quicksort_iterativo(lista))
    fin = time.time()
    t_qi = fin - inicio

    lista = lista_apoyo[:]
    inicio = time.time()
    verify_list(sl.quicksort(lista))
    fin = time.time()
    t_q = fin - inicio

    lista = lista_apoyo[:]
    inicio = time.time()
    verify_list(sl.randomized_quicksort(lista))
    fin = time.time()
    t_rq = fin - inicio

    lista = lista_apoyo[:]
    inicio = time.time()
    verify_list(sl.TimSort(lista))
    fin = time.time()
    t_t = fin - inicio
    return t_mer, t_mer_it, t_mer_thr, t_mer_opt, t_qi, t_q, t_rq, t_t


def lista_df(nombre, tamaño, intento, tiempo):
    """ Esta función genera una lista con:
        
        - "nombre" de algoritmo.
        - "tamaño" de la secuencia.
        - "intento" para ordenar el algoritmo.
        - "tiempo" en el que se ordeno el algoritmo.

        la lista que retorna esta función será agregada a una lista llamada:

        - array_csv

        que luego será convertida en DataFrame"""

    list_data = []
    list_data.append(nombre)
    list_data.append(tamaño)
    list_data.append(intento + 1)
    list_data.append(tiempo)
    return list_data


localtime = time.asctime(time.localtime(time.time()))
print("Hora de inicio de ejecución :", localtime, "\n")

try:
    graficar = False
    tip_sec = None
    long_str = None
    lista = []
    lista_parametro = [] 
    array_csv = []
    apoyo = sys.argv[1:]
    ind = apoyo.index("-n") + 1

    while (len(apoyo) != ind and (apoyo[ind] not in ["-a", "-s", "-g",
                                                     "-t", "-m"])):
        if int(apoyo[ind]) < 1:
            print("¡Error!, Las longitudes son números no negativos")
            sys.exit()
        lista.append(int(apoyo[ind]))
        apoyo.pop(ind)
    apoyo.insert(ind, lista)

    option, remaining = gto.getopt(apoyo, 's:t:m:n:a:g')

    if remaining:
        raise NameError("¡Error! Introdujo valores de "
                        "mas:{}".format(remaining))

    for ops, arg in option:

        if ops in lista_parametro:
            raise NameError("¡Error!, El parámetro {} "
                            "está repetido".format(ops))
        else:
            lista_parametro.append(ops)
            if ops == "-n":
                nlis = arg
            elif ops == '-t':
                intentos = int(arg)
                if intentos < 1:
                    raise NameError("¡Error!, -t no puede tener "
                                    "valores negativos")
            elif ops == '-s':
                if arg in (['sreal', 'sortedreal', 'invsortedreal', 'sint',
                            'invsortedint', 'sortedint',
                            'sstr', 'sortedstr',
                            'invsortedstr', 'unocero']):
                    tip_sec = arg
                else:
                    raise NameError("¡Error!, \"{}\" no hace referencia a un "
                                    "tipo de lista válida".format(tip_sec))

            elif ops == '-m':
                long_str = int(arg)
                if long_str < 1:
                    raise NameError("¡Error!, -m no puede tener "
                                    "valores negativos")
            elif ops == "-a":
                if arg in ["on2", "nlgn"]:
                    fam_alg = arg
                else:
                    raise NameError("¡Error!, La familia {} de algoritmos "
                                    "no es válida".format(arg))
            elif ops == "-g":
                graficar = True

    if not('-n' or '-t' or '-s') in lista_parametro:
        raise NameError("¡Error!, -valide nuevo error")
    
    if len(nlis) == 1 and graficar:
        raise NameError("¡Error!, no puede graficar una lista de "
                        "longitudes con un solo elemento")
    
    if ((type(long_str) == int and tip_sec in ['sreal', 'sortedreal',
                                               'invsortedreal', 'sint',
                                               'invsortedint',
                                               'sortedint', 'unocero'])
            or (long_str is None and tip_sec
            in ['sstr', 'sortedstr', 'invsortedstr'])) or tip_sec is None:

        raise NameError("¡Error! Sólo puede usar el parámetro -m con una  "
                        "secuencia tipo string")

except gto.GetoptError as error:
    print("error", error)
    sys.exit()
except ValueError:
    pass


if fam_alg == "on2":
    print("\nLos tiempos obtenidos por el ordenamiento de secuencias "
          "con algoritmos de la familia On2 son:")
    for size in nlis:
        for x in range(intentos):
            lista_u = seleccion_lista(tip_sec, size, long_str)
            ti, tb, ts, tsh = algoritmos_On2(lista_u)

            array_csv.append(lista_df("InsertionSort", size, x, ti))
            array_csv.append(lista_df("BubbleSort", size, x, tb))
            array_csv.append(lista_df("SelectionSort", size, x, ts))
            array_csv.append(lista_df("ShellSort", size, x, tsh))

elif fam_alg == "nlgn": 
    print("\nLos tiempos obtenidos por el ordenamiento de secuencias "
          "con algoritmos de la familia nlgn son:")
    for size in nlis:
        for x in range(intentos):
            lista_u = seleccion_lista(tip_sec, size, long_str)
            tmr, tmrit, tmrth, tmropt, tqi, tq, trq, t_t = algoritmos_nlgn(lista_u)

            array_csv.append(lista_df("MergeSort", size, x, tmr))
            array_csv.append(lista_df("MergeIterativo", size, x, tmrit))
            array_csv.append(lista_df("MergeThree", size, x, tmrth))
            array_csv.append(lista_df("MergeOPT", size, x, tmropt))
            array_csv.append(lista_df("quicksortIterativo", size, x, tqi))
            array_csv.append(lista_df("Quicksort", size, x, tq))
            array_csv.append(lista_df("RdmQuicksort", size, x, trq))
            array_csv.append(lista_df("Timsort", size, x, t_t))

# Se crea un DataFrame con los datos generado en el experimento.
pd.set_option("max_rows", None)
datos = np.array(array_csv)
df_datos = pd.DataFrame(datos, columns=["Algoritmos", "Num. de elementos",
                                        "Intento", "Tiempo(seg)"])
df_datos.drop(df_datos.columns[[0]], axis='columns')
df_datos[["Tiempo(seg)"]] = df_datos[["Tiempo(seg)"]].astype(float)
df_datos[["Intento"]] = df_datos[["Intento"]].astype(int)
df_datos[["Num. de elementos"]] = df_datos[["Num. de elementos"]].astype(int)

# Convertir DataFrame a archivo CSV con el nombre de el tipo de secuencia, tipo algoritmo
# df_datos.to_csv('Algoritmos_' + fam_alg + '_' + tip_sec + '.csv', sep='\t')

# Imprime por consola los resultado de los experimentos 
print(df_datos)

localtime = time.asctime(time.localtime(time.time()))
print("Hora final de ejecución :", localtime, "\n")

# gráfica los datos si -g esta activo
if graficar:
    sns.lineplot(
        data=df_datos, x="Num. de elementos", y="Tiempo(seg)",
        hue="Algoritmos", err_style="bars")
    titulo_grafica = "Tipo de secuencia " + tip_sec
    plt.title(titulo_grafica)
    plt.show()
 