
# Descripción: Este modulo contiene versiones modificadas de bubblesort y 
#              quicksort. Cada algoritmos de ordenamiento tiene como entrada
#              dos arreglos que ordenara dichos arreglos según la relación de 
#              orden R dada sobre ZxZ dada por:
#               (a, b) R (a', b´) si y solo si a < a' and (b<=b')  
#
# Creado por: Juan Reyna
# email: 10-10883@usb.ve
# version: 1.0

import random as rd
import sys


#sys.setrecursionlimit(1000000000 * 2)

def bubblesort_par(A, B):
    n = len(A)
    for i in range(0, n):
        for j in range(n - 1, i, -1):
            if A[j - 1] > A[j]:
                A[j - 1], A[j] = A[j], A[j - 1]
                B[j - 1], B[j] = B[j], B[j - 1]
            elif A[j - 1] == A[j] and B[j - 1] > B[j]:
                B[j - 1], B[j] = B[j], B[j - 1]
    return A,B


def quicksort_par(A, B):
    pass


def partition(A, B, p, r):
 
    x = A[p]
    i = p - 1
    j = r + 1
 
    while (True):

        j = j - 1
        while (A[j] > x):
            j = j - 1

        i = i + 1
        while (A[i] < x):
            i = i + 1 


        if (i < j):
            A[i], A[j] = A[j], A[i]
            B[i], B[j] = B[j], B[i]
            if A[i] == A[j]:
                B[i], B[j] = B[j], B[i]
        else:
            return j
            

def quicksort_aux(A, B, p, r):
    if p < r:
        q = partition(A, B, p, r)
        quicksort_aux(A, B, p, q)
        quicksort_aux(A, B, q + 1, r)
        return A,B
    


def quicksort(A, B):
    n = len(A)
    return quicksort_aux(A, B, 0, n - 1)


def bubble_sort(A):
    n = len(A)
    for i in range(0, n):
        for j in range(n - 1, i, -1):
            if A[j - 1] > A[j]:
                A[j - 1], A[j] = A[j], A[j - 1]
    return A

if __name__ == '__main__':
    
    #edad = [rd.randint(0, 100) for i in range(0, 4)]
    #peso = [rd.randint(40, 150) for i in range(0, 4)]
    
    edad = [20, 19, 23, 19]
    peso = [60, 71, 58, 65]
    
    # edad = [1, 10, 14, 7, 7, 11]
    # peso = [1, 1, 14, 15, 5, 16]
    
    print("Edad", edad)
    print("Peso", peso)
    # edad_ord, peso_ord = bubblesort_par(edad, peso)
    edad_ord, peso_ord = quicksort(edad, peso)



    print("\nLa lista ordenada de edad es", edad_ord)
    print("La lisla de peso es: ", peso_ord)