import random as rd
import sys

# Algoritmo de ordenamiento Heapsort
def parent(i):
    # Retorna el índice del padre del elemento i
    return i // 2


def rightChild(derecha):
    # Retorna índice de hijo derecho del elemento en la posición i
    return 2 * derecha + 1


def leftChild(izquierda):
    # Retorna índice de hijo izquierdo del elemento en la posición i
    return 2 * izquierda


def maxHeapify(A, i, n):  # borre n
    # Constrye el Heap que incluye el elemento en la posición i

    le = leftChild(i)
    r = rightChild(i)
    if le < n and A[le] > A[i]:
        # cambie n por i
        largest = le
    else:
        largest = i
    if r < n and A[r] > A[largest]:
        largest = r
    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        maxHeapify(A, largest, n)


def buildMaxHeapify(A):
    # Construye en A un heap de tipo Max con los elementos de A
    n = len(A)
    for i in range(n // 2, -1, -1):
        maxHeapify(A, i, n)


def heapsort(A):
    # Implementa heapsort sobre el arreglo A
    buildMaxHeapify(A)
    n = len(A) - 1
    for i in range(n, -1, -1):
        A[0], A[i] = A[i], A[0]
        maxHeapify(A, 0, i)
    return A


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
        print("\nLa lista ordenada debería ser así:")
        print(list_aux)

        print("\nSu algoritmo arrojó la siguiente secuencia:")
        print(list_test)
        print("\nLos indices de la lista que apuntan a los elementos mal ")
        print("ubicados por error del algoritmo de ordenamiento son:\n")
        print(lista)
        sys.exit()
    else:
        pass

lista = [rd.randint(0, 5000) for x in range(0, 100000)]
lista1 = heapsort(lista)
verify_list(lista1)
print("Prueba realizada con éxito")
