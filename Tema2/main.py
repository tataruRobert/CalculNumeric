import math
import functools
import numpy as np

A = np.loadtxt('A.txt')
b = np.loadtxt('b.txt')
n = 100
e = math.pow(10, -10)
A_prim = A.copy()
b_prim = b.copy()


def LU(n):
    A = np.zeros((n, n))
    for p in range(n):
        for i in range(p, n):
            sum = 0
            for k in range(p):
                sum += (A[p][k] * A[k][i])
            A[p][i] = A_prim[p][i] - sum
        for i in range(p, n):
            if i != p:
                sum = 0
                for k in range(p):
                    if i == k:
                        sum += A[k][p]
                    else:
                        sum += (A[i][k] * A[k][p])
                A[i][p] = divide(A_prim[i][p] - sum, A[p][p])
    return A

def inversa(A_inv):
    for q in range(n):
        e = np.zeros(n)
        e[q] = 1
        # rezolvam Ly = e
        y = np.zeros(n)
        for i in range(n):
            sum = 0
            for j in range(i):
                if i == j:
                    sum += y[j]
                else:
                    sum += y[j] * A[i][j]
            e[i] -= sum
            y[i] = e[i] / 1
        # rezolvam Ux = y
        x = np.zeros(n)
        for i in range(n - 1, -1, -1):
            sum = 0
            for j in range(n - 1, i, -1):
                sum += x[j] * A[i][j]
            y[i] -= sum
            x[i] = y[i] / A[i][i]
        for l in range(n):
            A_inv[l][q] = x[l]
    return A_inv

def metoda_substitutiei():
    # metoda substitutiei directe
    y = np.zeros(n)
    for i in range(n):
        sum = 0
        for j in range(i):
            if i == j:
                sum += y[j]
            else:
                sum += A[i][j] * y[j]
        b[i] -= sum
        y[i] = b[i] / 1
    # metoda substitutiei inverse
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        sum = 0
        for j in range(n - 1, i, -1):
            sum += A[i][j] * x[j]
        y[i] -= sum
        x[i] = y[i] / A[i][i]
    return x

def determinant(m, flag):
    if flag:
        array = [1 for i in range(m.shape[0])]

        return functools.reduce(lambda a, b : a * b, array)
    else:
        array = [m[i][i] for i in range(m.shape[0])]

        return functools.reduce(lambda a, b: a*b, array)


def divide(a, b):
    if abs(b) > e:
        return a / b
    else:
        print("nu se poate face impartirea")
        return 0


if __name__ == "__main__":
    A = LU(n)
    print("Matricea A:")
    print(A)
    print("Determinant obisnuit:")
    print(np.linalg.det(A_prim))
    print("Determinant cu descompunerea LU:")
    print(determinant(A, 1) * determinant(A, 0))

    x = metoda_substitutiei()
    print("Solutia sistemului Ax=b: prin metoda substitutiei")
    print(x)
    x_prim = x.copy()
    print("Norma: A^init*Xlu - b^init")
    print(np.linalg.norm(A_prim.dot(x) - b_prim, 2))

    # calcul inversa matrice
    A_inv = np.zeros((n, n))
    A_inv = inversa(A_inv)

    x_lib = np.linalg.solve(A_prim, b_prim)
    print("Norma: Xlu - xlib")
    print(np.linalg.norm(x_prim - x_lib, 2))
    print("Norma: Xlu - Ainv_lib*binit")
    print(np.linalg.norm(x_prim - np.linalg.inv(A_prim).dot(b_prim), 2))
    print("Inversa lui A")
    print(A_inv)
    print("Norma: Ainv_LU - Ainv_lib")
    print(np.linalg.norm(A_inv - np.linalg.inv(A_prim), 1))




