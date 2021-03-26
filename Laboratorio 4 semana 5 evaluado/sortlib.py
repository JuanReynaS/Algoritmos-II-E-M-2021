# Descripción: Este módulo contiene los algoritmos de ordenamiento de
#              simples de complejidad computacional On2: 
#              
#              insertionsort, selectionsort, shellsort, bubblesort.
#              

#              Y los algoritmos de complejidad computacional nlgn:
#
#              mergesort(lista), mergesort_iterativo(lista),
#              mergesort_three(lista), mergesort_opt(lista),
#              quicksort_iterativo(lista), quicksort(lista),
#              randomized_quicksort(lista)
#
# Creado por: Juan Reyna
# email: 10-10883@usb.ve
# version: 4.0

import random as rd
import sys
import math as mt

sys.setrecursionlimit(1000000000 * 2)


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
    if len(A) <= 2:
        TimSort(A)
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
    U.append(mt.inf) if type(U[0]) == int or type(U[0]) == float else U.append(2 * max(T))
    V.append(mt.inf) if type(V[0]) == int or type(V[0]) == float else V.append(2 * max(T))
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
    return A


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
    if len(A) <= 500:
        shell_sort(A)
    else:
        mitad = len(A) // 2
        vector1 = A[:mitad]
        vector2 = A[mitad:]
        mergesort(vector1)
        mergesort(vector2)
        A = merge(vector1, vector2, A)
    return A


def quicksort_iterativo(A):
    n, m, longitud = 0, 1, len(A)

    while m < longitud:
        n, m = n + 1, m * 2

    k, p, q = 0, 0, longitud
    x = [0] * (n)
    y = [0] * (n)

    while (k != 0) or (q - p >= 2):
        if (q - p <= 1):
            k = k - 1
            p = x[k]
            q = y[k]
        elif (q - p >= 2):
            mitad = (p + q) // 2
            z = A[mitad]
            r, w, b = p, p, q

            while w != b:

                if A[w] < z:
                    A[r], A[w] = A[w], A[r]
                    r, w = r + 1, w + 1
                elif A[w] == z:
                    w = w + 1
                elif A[w] > z:
                    b = b - 1
                    A[b], A[w] = A[w], A[b]

            if r - p <= q - w:
                x[k] = w
                y[k] = q
                q = r
            elif q - w < r - p:

                x[k] = p
                y[k] = r
                p = w

            k = k + 1

    return A


def partition(A, p, r):
    x = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j] <= x:
            i = i + 1
            A[i], A[j] = A[j], A[i]
    A[i + 1], A[r] = A[r], A[i + 1]
    return i + 1


def quicksort_aux(A, p, r):
    if p < r:
        q = partition(A, p, r)
        quicksort_aux(A, p, q - 1)
        quicksort_aux(A, q + 1, r)
    return A


def quicksort(A):
    return quicksort_aux(A, 0, len(A) - 1)


def RandomizedPartition(A, p, r):
    i = rd.randint(p, r)
    A[r], A[i] = A[i], A[r]
    return partition(A, p, r)


def RandomizedQuicksort(A, p, r):
    if p < r:
        q = RandomizedPartition(A, p, r)
        RandomizedQuicksort(A, p, q - 1)
        RandomizedQuicksort(A, q + 1, r)
    return A


def randomized_quicksort(A):
    return RandomizedQuicksort(A, 0, len(A) - 1)



minrun = 32


def InsSort(arr, start, end):
    for i in range(start + 1, end + 1):
        elem = arr[i]
        j = i - 1
        while j >= start and elem < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = elem
    return arr


def merge1(arr, start, mid, end):
    if mid == end:
        return arr
    first = arr[start:mid + 1]
    last = arr[mid + 1:end + 1]
    len1 = mid - start + 1
    len2 = end - mid
    ind1 = 0
    ind2 = 0
    ind = start

    while ind1 < len1 and ind2 < len2:
        if first[ind1] < last[ind2]:
            arr[ind] = first[ind1]
            ind1 += 1
        else:
            arr[ind] = last[ind2]
            ind2 += 1
        ind += 1

    while ind1 < len1:
        arr[ind] = first[ind1]
        ind1 += 1
        ind += 1

    while ind2 < len2:
        arr[ind] = last[ind2]
        ind2 += 1
        ind += 1

    return arr


def TimSort(arr):
    n = len(arr)

    for start in range(0, n, minrun):
        end = min(start + minrun - 1, n - 1)
        arr = InsSort(arr, start, end)

    curr_size = minrun
    while curr_size < n:
        for start in range(0, n, curr_size * 2):
            mid = min(n - 1, start + curr_size - 1)
            end = min(n - 1, mid + curr_size)
            arr = merge1(arr, start, mid, end)
        curr_size *= 2
    return arr


if __name__ == '__main__':
#    lista = [rd.randint(0, 2000) for i in range(0, 20)]
    lista = [1,4,3,10,2,7,8,9,14,16]
    print(heapsort(lista))
