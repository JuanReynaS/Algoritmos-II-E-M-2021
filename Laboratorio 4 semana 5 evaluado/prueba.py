import random as rd
import sys


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

"""def mergesort(myList):
    if len(myList) > 1:
        mid = len(myList) // 2
        left = myList[:mid]
        right = myList[mid:]

        # Recursive call on each half
        mergesort(left)
        mergesort(right)

        # Two iterators for traversing the two halves
        i = 0
        j = 0
        
        # Iterator for the main list
        k = 0
        
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
              # The value from the left half has been used
              myList[k] = left[i]
              # Move the iterator forward
              i += 1
            else:
                myList[k] = right[j]
                j += 1
            # Move to the next slot
            k += 1

        # For all the remaining values
        while i < len(left):
            myList[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            myList[k]=right[j]
            j += 1
            k += 1
    return myList"""

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
    U.append(2 * max(T))
    V.append(2 * max(T))
    for k in range(0, M + N):
        if U[i] < V[j]:
            T[k] = U[i]
            i = i + 1
        else:
            T[k] = V[j]
            j = j + 1
    return T


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
        sys.exit()
    else:
        pass


if __name__ == '__main__':
    for i in range(500):
        lista = [rd.randint(0, 1) for i in range(0, 10000)]
        # print(lista)
        lista1 = mergesort(lista)
        # print(lista1)
        verify_list(lista1)
        print("Tuvo exito al ordenar a lista merge_sort")
