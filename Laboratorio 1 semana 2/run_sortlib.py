# Descripción: En este módulo se ejecuta las diversas pruebas de exigidas por
#             el usuario sobre los algoritmos en el módulo sortlib.py
#
#             La ejecución de este módulo se hace a través de la siguiente
#             línea de comando:
#
#             python3 sortlib.py -t[#num] -m[#num] -s[tipo] -n[num]
#
# Creado por: Juan Reyna
# email: 10-10883@usb.ve

import getopt as gto
import math
import random
import random as rd
import string as st
import sys
import time
import sortlib as sl


def sreal(n):
    """Secuencia de n ́umeros reales en el intervalo [0, 1]
       generados aleatoriamente."""
    try:
        assert(n > 0)
        lista = [round(rd.uniform(0, 1), 2) for x in range(0, n)]
        return lista
    except AssertionError:
        print('Error: Indico una longitud para la lista no positiva')


def sortedreal(n):
    """Una secuencia de tipo sreal, pero en donde todos los elementos están
       ordenados."""
    try:
        assert(n > 0)
        lista = sorted(sreal(n))
        return lista
    except AssertionError:
        print('Error: Indico una longitud para la lista no positiva')


def invsortedreal(n):
    """Una secuencia de tipo sreal, pero en donde todos los elementos estan
       ordenados de forma inversa."""
    try:
        lista = sorted(sreal(n), reverse=True)
        return lista
    except AssertionError:
        print('Error: Indico una longitud para la lista no positiva')
        sys.exit()


def sint(n):
    """Secuencie de n ́umeros enteros en el intervalo [0, N] generados
       aleatoriamente, donde N es el tama ̃no de la secuencia a ordenar."""
    try:
        assert (n > 0)
        lista = [rd.randint(0, n) for x in range(n)]
        return lista
    except AssertionError:
        print('Error: Indico una longitud para la lista no positiva')
        sys.exit()


def sortedint(n):
    """Una secuencia de tipo sint, pero en donde todos los elementos estan
       ordenados"""
    try:
        assert (n > 0)
        lista = sorted(sint(n))
        return lista
    except AssertionError:
        print('Error: Indico una longitud para la lista no positiva')
        sys.exit()


def invsortedint(n):
    """Una secuencia de tipo sint, pero en donde todos los elementos estan
       ordenados de forma inversa"""
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
    try:
        assert(tipo in ['sreal', 'sortedreal', 'invsortedreal', 'sint',
                                             'invsortedint', 'sortedint',
                                             'sstr', 'sortedstr',
                                             'invsortedstr'])

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
        return lista
    except AssertionError:
        print("¡Error!,  \"{}\" no hace referencia a un "
              "tipo de lista válida".format(tipo))
        sys.exit()


def verify_list(list_test):
    """Esta función verifica  si una secuencia eterminada fue ordenada por un
       algoritmo. Si dicha secuencia no fue ordenada se aborta la ejecución del
       programa.

       Si de eliminan los numerales (#) es este módulo se tendrán mas detalle
       sobre la secuencia que no fue ordenada"""

    list_aux = sorted(list_test)
    lista = [x for x in range(0, len(list_test))
                 if list_test[x] != list_aux[x]]
    if lista:
        print("\n***** SU ALGORITMO NO ORDENÓ LA LISTA DADA *****")
        # print("\nLa lista ordenada debería ser así:")
        # print(list_aux)

        # print("\nSu algoritmo arrojó la siguiente secuencia:")
        # print(list_test)

        # print("\nLos indices de la lista que apuntan a los elementos mal ")
        # print("ubicados por error del algoritmo de ordenamiento son:\n")
        # print(lista)
        sys.exit()
    else:
        pass


try:
    listao = []
    o, m = 0, 0
    option, remaining = gto.getopt(sys.argv[1:], 's:t:m:n:')

    if remaining:
        raise NameError("¡Error! Introdujo valores de "
                        "mas:{}".format(remaining))

    for ops, arg in option:
        if ops in listao:
            raise NameError("¡Error!, El parámetro {} "
                            "está repetido".format(ops))
        else:
            listao.append(ops)
            if ops == '-n':
                n = int(arg)
            elif ops == '-t':
                t = int(arg)
            elif ops == '-s':
                s = arg
            elif ops == '-m':
                o, m = ops, int(arg)
except gto.GetoptError as error:
    print("error", error)
    sys.exit()
except ValueError:
    print("\"{}\" es inválido. Ingrese un entero positivo"
          " a parámetro {}".format(arg, ops))
    sys.exit()

if '-n' not in listao or '-s' not in listao or '-t' not in listao:
    raise NameError("""Argumentos obligatorios:
                      '-s': Tipo de secuencia a ordenar
                      '-t': Número de intentos
                      '-m': Tamaño se los strings
                      '-n': Longitud de secuencia a ordenar""")


if m == 0 and s in ['sstr', 'sortedstr', 'invsortedstr']:
    raise NameError("¡Error! No puede usar -s:"
                    "{} sin combinar con -m".format(s))
elif m > 0 and s not in ['sstr', 'sortedstr', 'invsortedstr']:
    raise NameError("¡Error! No puede combinar -m con -s: {}".format(s))

if m < 0 or n <= 0 or t <= 0:
    raise NameError("¡Error! uno de sus argumentos posee valor no positivo")

lista_t_insertion = []
lista_t_bubble = []
lista_t_selection = []
lista_t_shell = []

print("\nInsertion Sort")
for i in range(t):
    lista_apoyo = seleccion_lista(s, n, m)[:]
    lista = lista_apoyo[:]
    inicio = time.time()
    listaX = sl.insertion_sort(lista)
    fin = time.time()
    tiempo = fin - inicio
    verify_list(listaX)
    lista_t_insertion.append(tiempo)

    print("El tiempo de ejecución en"
          "intento {} fue: {:.2f}".format(i + 1, tiempo))
media_insertion = sum(lista_t_insertion) / len(lista_t_insertion)
print("El promedio de los tiempos es: {:.2f} s y la desviación"
      "es: {:.2f}s".format(media_insertion, SD(lista_t_insertion,
                                               media_insertion)))

print("\nBubble Sort")
for i in range(t):
    lista_apoyo = seleccion_lista(s, n, m)[:]
    lista = lista_apoyo[:]
    inicio = time.time()
    listaX = sl.bubble_sort(lista)
    fin = time.time()
    tiempo = fin - inicio
    verify_list(listaX)
    lista_t_bubble.append(tiempo)

    print("El tiempo de ejecución en"
          "intento {} fue: {:.2f}".format(i + 1, tiempo))
media_bubble = sum(lista_t_bubble) / len(lista_t_bubble)
print("El promedio de los tiempos es: {:.2f} s y la desviación"
      "es: {:.2f} s".format(media_bubble, SD(lista_t_bubble, media_bubble)))

print("\nSelection Sort")
for i in range(t):
    lista_apoyo = seleccion_lista(s, n, m)[:]
    lista = lista_apoyo[:]
    inicio = time.time()
    listaX = sl.selection_sort(lista)
    fin = time.time()
    tiempo = fin - inicio
    verify_list(listaX)
    lista_t_selection.append(tiempo)

    print("El tiempo de ejecución en"
          "intento {} fue: {:.2f}".format(i + 1, tiempo))
media_selection = sum(lista_t_selection) / len(lista_t_selection)
print("El promedio de los tiempos es: {:.2f} s y la desviación es: {:.2f} "
      "s".format(media_selection, SD(lista_t_selection, media_selection)))

print("\nShell Sort")
for i in range(t):
    lista_apoyo = seleccion_lista(s, n, m)[:]
    lista = lista_apoyo[:]
    inicio = time.time()
    listaX = sl.shell_sort(lista)
    fin = time.time()
    tiempo = fin - inicio
    lista_t_shell.append(tiempo)
    verify_list(listaX)
    print("El tiempo de ejecución"
          "en intento {} fue: {:.2f}".format(i + 1, tiempo))
media_shell = sum(lista_t_shell) / len(lista_t_shell)
print("El promedio de los tiempos"" es: {:.2f} s y la desviación"
      "es: {:.2f} s".format(media_shell, SD(lista_t_shell, media_shell)))
