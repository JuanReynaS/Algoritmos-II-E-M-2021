#!/usr/bin/python3

import sys
import sortlib_par as sp
import random

def verificar_orden(A, B):
    assert(len(A) == len(B))
    n = len(A)
    print(A)
    print(B)
    for i in range(n-1):
        if A[i] > A[i+1]:
            print("Error en arrglo A", A[i], A[i+1])
            sys.exit()
        elif A[i] == A[i+1]:
            if B[i] > B[i+1]:
                print("Error en arrglo B", B[i], B[i+1])
                sys.exit()
        else:
            pass

def verificar_pares(A0, B0, A1, B1):
    assert(len(A0) == len(A1) == len(B0) == len(B1))
    n = len(A0)
    orig = set()
    for i in range(n):
        orig.add( (A0[i], B0[i]) )
    for i in range(n):
        if (A1[i], B1[i]) not in orig:
            print("Error, este par no es de los arreglos originales ", (A1[i], B1[i]) )
            sys.exit(1)
            
def generar_arreglo(n):
    random.seed(19)
    A = []
    B = []
    for i in range(n):
        A.append( random.randint(0, n) )
        B.append( random.randint(0, n) )
    return (A, B)

def verificar_resultados(A1, B1, alg):
    A0 = A1.copy()
    B0 = B1.copy()
    print("\nProbando "+alg.__name__)
    print("Ordenando ............")
    alg(A1, B1)
    print("Listo ordenamiento")
    print("Verificando orden")
    verificar_orden(A1,B1)
    print("Lista la verificacion de orden")
    print("Verificando pares")
    verificar_pares(A0, B0, A1, B1)
    print("Lista la verificacion de pares")
    print("Pruebas superadas con exito!\n")
    
#######################
#
# Main
#
#######################

def main(argv):
    n = int(argv[0])
    m = int(argv[1])
    (A, B) = generar_arreglo(n)
    verificar_resultados(A, B, sp.bubblesort_par)
    (A, B) = generar_arreglo(m)
    verificar_resultados(A, B, sp.quicksort_par)

if __name__ == "__main__":
    main(sys.argv[1:])