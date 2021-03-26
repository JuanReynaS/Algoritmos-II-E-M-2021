import random as rd


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


lista = [rd.randint(0, 2000) for i in range(0, 10)]
# print("***", lista)
print(merge_iterativo(lista))
