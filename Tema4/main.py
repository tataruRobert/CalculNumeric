import numpy as np
import math


def read_matrix(file_name):
    f = open(file_name, "r+")
    f_arr = f.read().strip().split('\n')
    size_matrix = int(f_arr[0])
    result = [[] for _ in range(size_matrix)]
    del f_arr[0]
    f.close()
    for i in f_arr:
        splitted = i.split(",")
        for el in range(len(splitted)):
            splitted[el] = float(splitted[el])
        value = splitted[0]
        row = splitted[1]
        column = splitted[2]
        flag = 0
        for j in result[int(row)]:
            if int(column) == j[1]:
                j[0] += value
                flag = 1
        if flag == 0:
            result[int(row)].append([value, int(column)])
    for i in range(size_matrix):
        result[i] = sorted(result[i], key=lambda x: x[1])
    return result, size_matrix


def read_vector(file_name):
    f = open(file_name, "r+")
    f_arr = f.read().strip().split('\n')
    size_vector = int(f_arr[0])
    result = []
    del f_arr[0]
    f.close()
    for i in f_arr:
        result.append(float(i))
    return result, size_vector


def my_seidel(a, x, b):
    n = len(a)
    result = []
    for j in range(n):
        column = 0
        d = b[j]
        for i in range(len(a[j])):
            if a[j][i][1] != j:
                d -= a[j][i][0] * xp[a[j][i][1]]
            else:
                column = a[j][i][0]
        result.append(d / column)
    return result


def multiply_matrix(A, B):
    result = []
    for i in range(len(A)):
        sum = 0
        for j in range(len(A[i])):
            sum += A[i][j][0] * B[A[i][j][1]]
        if sum != 0:
            result.append(sum)
    return result

def checkDiagonal(a,e):
    i = 0
    while i < len(a):
        flag = False
        if flag is True:
            flag = False
        for el in a[i]:
            if abs(el[0]) > e and el[1] == i:
                flag = True
                break
        if flag is not True:
            return flag
        i += 1
    return flag

if __name__ == "__main__":
    a_rare, a_size = read_matrix("a_1.txt")
    b_rare, b_size = read_vector("b_1.txt")
    e = math.pow(10, -10)
    xc = [0 for _ in range(b_size)]
    xp = [0 for _ in range(b_size)]
    if checkDiagonal(a_rare, e) is True:
        k = 0
        while True:
            k += 1
            xp = xc
            xc = my_seidel(a_rare, xp, b_rare)
            delta_x = 0
            for i in range(len(xp)):
                delta_x += abs(xp[i] - xc[i])
            print(k, delta_x)
            if (k > 10000 or delta_x < e or delta_x > pow(10, 100)):
                break

        print(xc[:10])
        xgs = xc
        aorixgs = multiply_matrix(a_rare, xgs)
        aorixgs = np.array(aorixgs)
        b_rare = np.array(b_rare)

        print("Norma AXgs - b: ")
        print(np.linalg.norm(aorixgs - b_rare, np.inf))
    else:
        print("Nu se poate aplica Gauss-Seidel")
