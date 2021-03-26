# Descripción: En este módulo contiene los algoritmos de ordenamiento de
#             simples: insertionsort, selectionsort, shellsort,
#             bubblesort
#
#
# Creado por: Juan Reyna
# email: 10-10883@usb.com

import random as rd


def insertion_sort(A):
    """Dado un arreglo de longitud n. Insertionsort toma uno por uno
       los elementos y se recorren hacia su posición con respecto a los
       anteriormente ordenados.

       Esta función devuelve el mismo arreglo ordenado"""

    m = A.index(min(A))
    n = len(A)
    A[0], A[m] = A[m], A[0]

    for i in range(1, n):
        j = i
        while A[j] < A[j - 1]:
            A[j], A[j - 1] = A[j - 1], A[j]
            j -= 1
    return A


def selection_sort(A):
    """Dado un arreglo de longitud n. Selectionsort encuentra el menor
       de todos los elementos del arreglo e intercambiarlo con el que
       está en la primera posición. Luego el segundo mas pequeño,
       y así sucesivamente hasta ordenar todo el arreglo.

       Esta función devuelve el mismo arreglo ordenado"""

    n = len(A)
    for i in range(0, n):
        lowindex = i
        lowkey = A[i]
        for j in range(i + 1, n):
            if A[j] < lowkey:
                lowkey = A[j]
                lowindex = j
        A[i], A[lowindex] = A[lowindex], A[i]
    return A


def shell_sort(A):

    n = len(A)
    incr = n // 2
    while incr > 0:
        for i in range(incr, n):
            j = i - incr
            while j > -1:
                if A[j] > A[j + incr]:
                    A[j], A[j + incr] = A[j + incr], A[j]
                    j = j - incr
                else:
                    j = -1
        incr = incr // 2
    return A


def bubble_sort(A):
    """Dado un arreglo de longitud n. Insertionsort Se recorre el
       arreglo intercambiando los elementos adjacentes que estén
       desordenados. Se recorre el arreglo tantas veces
       hasta que ya no haya cambios.

       Esta función devuelve el mismo arreglo ordenado"""

    n = len(A)
    for i in range(0, n):
        for j in range(n - 1, i, -1):
            if A[j - 1] > A[j]:
                A[j - 1], A[j] = A[j], A[j - 1]
    return A


def mergesort(A):
    if len(A) <= 10:
        insertion_sort(A)
    else:
        mitad = len(A) // 2
        vector1 = A[:mitad]
        vector2 = A[mitad:]
        mergesort(vector1)
        mergesort(vector2)
        A = merge(vector1, vector2, A)
    return A


def merge(U, V, T):
    i, j = 0, 0
    N = len(U)
    M = len(V)
    U.append(2000 * max(T))
    V.append(2000 * max(T))
    for k in range(0, M + N):
        if U[i] < V[j]:
            T[k] = U[i]
            i = i + 1
        else:
            T[k] = V[j]
            j = j + 1
    return T


def mergesort_iterativo(A):
    k = 1
    N = len(A)
    while k < N:
        a, b, c = 0, k, min(2 * k, N)
        z = [0] * N
        while b < N:
            p, q, r = a, b, a
            while p != b and q != c:
                if A[p] <= A[q]:
                    z[r] = A[p]
                    r, p = r + 1, p + 1
                else:
                    z[r] = A[q]
                    r, q = r + 1, q + 1
            while p != b:
                z[r] = A[p]
                r, p = r + 1, p + 1
            while q != c:
                z[r] = A[q]
                r, q = r + 1, q + 1
            r = a
            while r != c:
                A[r] = z[r]
                r += 1
            a, b, c = a + 2 * k, b + 2 * k, min(c + 2 * k, N)
        k *= 2

    return z


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


def sort_three(A):
    for i in range(0, len(A)):
        for j in range(i + 1, len(A)):
            if A[i] > A[j]:
                A[i], A[j] = A[j], A[i]
            else:
                pass
    return A


def mergesort_three(A):
    if len(A) <= 3:
        sort_three(A)
    else:
        mitad = len(A) // 2
        vector1 = A[:mitad]
        vector2 = A[mitad:]
        mergesort(vector1)
        mergesort(vector2)
        A = merge(vector1, vector2, A)
    return A


def mergesort_opt(A):
    if len(A) <= 250:
        shell_sort(A)
    else:
        mitad = len(A) // 2
        vector1 = A[:mitad]
        vector2 = A[mitad:]
        mergesort(vector1)
        mergesort(vector2)
        A = merge(vector1, vector2, A)
    return A


if __name__ == '__main__':
    lista = sorted([rd.uniform(0, 1) for i in range(0, 200000)])
    mergesort(lista)
    print("HOLA")
