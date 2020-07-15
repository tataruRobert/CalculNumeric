import math
import itertools
from operator import add

def num(v):
    result = 0
    for index, el in enumerate(v):
        result += math.pow(2, index) * el
    return result

def matrix_addition(x,y):
    if x == 1 and y == 1:
        return 1
    else :
        return x + y


def generate_A_submatrices(A_prim, nr_lines, nr_columns, p, m):
    result = []
    for i in range(p):
        A = [[0 for col in range(m)] for row in range(nr_lines)]
        result.append(A)
    print(result)
    print(A_prim)
    for i in range(p):
       for l in range(nr_lines):
           for c in range(m):
               pass
               # result[i][l][c] = A_prim[l][m*i + c]
    return result


def generate_B_submatrices(B_prim, nr_lines, nr_columns, p, m):
    result = []
    for i in range(p):
        A = [[0 for col in range(nr_columns)] for row in range(m)]
        result.append(A)
    # for i in range(p):
    #    for l in range(m):
    #        for c in range(nr_columns):
    #            result[i][l][c] = B_prim[i*m + l][c]
    return result

def indexs_combinations(m):
    result = []
    indexi = [i for i in range(m)]
    for index in indexi:
        for el in itertools.combinations(indexi,index + 1):
            result.append(list(el))
    return result

def generate_sums_Bi(Bi, combinations, columns):
    empty = [0 for i in range(columns)]
    result = [empty]
    for comb in combinations:
        empty = [0 for i in range(columns)]
        # print(comb)
        for row in comb:
            empty = list(map(matrix_addition, empty, Bi[row]))
            # print(empty)
        result.append(empty)
    return result


if __name__ == "__main__":

    u = 1
    while 1 + u != 1:
        #print(u)
        u /= 10
    print(u)
    x = 1.0
    y = u
    z = u
    if (x + y) + z == x + (z + y):
        print("adunare neasoc", y, z)
    else:
        print("fals")

    x = 1.0
    y = u
    z = u
    if (x * y) * z == x * (z * y):
        print("inmultire neasoc", y, z)
    else:
        print("fals")

    n = 8
    m = math.floor(math.log(n, 2))
    p = math.ceil(n/m)
    print(m, p)
    combinations = indexs_combinations(m)

    # X = [[1, 0, 1],
    #      [0, 1, 1],
    #      [1, 1, 0],
    #      [0, 0, 0],
    #      [1, 0, 0],
    #      [1, 1, 1],
    #      [0, 1, 0],
    #      [0, 0, 1]]

    X = [[1, 0, 1, 1, 1],
         [0, 0, 0, 0, 1],
         [1, 1, 1, 0, 1],
         [0, 0, 1, 1, 1],
         [1, 0, 0, 0, 1]]

    A_submatrices = generate_A_submatrices(X, 8, 3, p, m)

    # Y = [[0, 0, 1, 1, 1, 0, 0, 1],
    #      [0, 1, 1, 0, 1, 0, 1, 0],
    #      [1, 0, 1, 0, 0, 0, 1, 1]]

    Y = [[0, 0, 1, 1, 0],
         [1, 0, 1, 0, 1],
         [0, 1, 0, 1, 0],
         [1, 1, 1, 1, 0],
         [1, 0, 0, 1, 0]]

    B_submatrices = generate_B_submatrices(Y, 3, 8, p, m)
    # generate_sums_Bi(Y, indexs_combinations(3), 8)

    # print(A_submatrices)
    # print(B_submatrices)

    C_is = []

    for i in range(p):
        C = []
        Bi = B_submatrices[i]
        posible_sums_for_Bi = generate_sums_Bi(Bi, combinations, 8)
        #print(posible_sums_for_Bi)
        sum_linii_B = []
        sum_linii_B.append([0 for i in range(n)])
        #print(int(math.pow(2, m) - 1))
        print(m)
        for j in range(1, int(math.pow(2, m) - 1) + 1):
            print(j)
            k = 0
            while True:
                if math.pow(2, k) <= j < math.pow(2, k + 1):
                    break
                else:
                    k += 1
            sum_linii_B.append([])
            sum_linii_B[j] = list(map(matrix_addition, sum_linii_B[j - int(math.pow(2, k))], posible_sums_for_Bi[k+1]))
        # for r in range(1, n + 1):
        #     #print(int(num(A_submatrices[i][r])))
        #     C.append(sum_linii_B[int(num(A_submatrices[i][r]))])
        print(C)
        C_is.append(C)







    # result = [[0, 0, 0, 0, 0, 0, 0, 0],
    #           [0, 0, 0, 0, 0, 0, 0, 0],
    #           [0, 0, 0, 0, 0, 0, 0, 0],
    #           [0, 0, 0, 0, 0, 0, 0, 0],
    #           [0, 0, 0, 0, 0, 0, 0, 0],
    #           [0, 0, 0, 0, 0, 0, 0, 0],
    #           [0, 0, 0, 0, 0, 0, 0, 0],
    #           [0, 0, 0, 0, 0, 0, 0, 0]]
    #
    #
    # # iterate through rows of X
    # for i in range(len(X)):
    #     # iterate through columns of Y
    #     for j in range(len(Y[0])):
    #         # iterate through rows of Y
    #         for k in range(len(Y)):
    #             if X[i][k] == 1 and Y[k][j] == 1:
    #                 result[i][j] = 1
    #             else:
    #                 result[i][j] += X[i][k] * Y[k][j]
    #
    # for r in result:
    #     print(r)

