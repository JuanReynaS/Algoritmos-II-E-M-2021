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
    if len(A) <= 2:
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
    U.append(max(T) + 1000)
    V.append(max(T) + 1000)
    for k in range(0, M + N):
        if U[i] <= V[j]:
            T[k] = U[i]
            i = i + 1
        elif V[j] < U[i]:
            T[k] = V[j]
            j = j + 1
    return T


def mergesort_iterativo(array):

    if 0 < len(array):
        q = (0 + len(array)) // 2

        list1 = insertion_sort(array[:q], len(array[:q]))

        list2 = insertion_sort(array[q:], len(array[q:]))

        vector = mergesort_iterativo1(list1, list2, len(list1), len(list2))

    return vector


def mergesort_iterativo1(x, y, M, N):
    a, b, c = 0, 0, 0
    z = [0] * (M + N)
    while (a != M and b != N):

        if x[a] <= y[b]:
            z[c] = x[a]
            a, c = a + 1, c + 1

        elif (y[b] < x[a]):
            z[c] = y[b]
            b, c = b + 1, c + 1

    while (a != M):
        z[c] = x[a]
        a, c = a + 1, c + 1

    while b != N:
        z[c] = y[b]
        b, c = b + 1, c + 1

    return z


def merge_iterativo(A):
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


lista = [rd.randint(0, 2000) for i in range(0, 20)]
print(mergesort_iterativo(lista))
