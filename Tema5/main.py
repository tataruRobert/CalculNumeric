import numpy as np
import random
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


def generateMatrix(p, n, rare=False):
    if rare:
        result = [[] for _ in range(p)]
        nr_columns = 10

        for i in range(len(result)):
            used_columns = []
            values_columns = []

            for p in result[i]:
                used_columns.append(p[1])

            new_columns = random.sample([x for x in range(n) if x not in used_columns], nr_columns)

            for _ in range(nr_columns):
                values_columns.append((random.uniform(-10.0, 10.0)))

            for l in range(nr_columns):
                result[i].append((values_columns[l], new_columns[l]))
            for l in range(nr_columns):
                result[new_columns[l]].append(([values_columns[l], i]))

        return result
    else:
        return np.random.uniform(-10.0, 10.0, (p, n))


def is_symmetrical(matrix):
    for i in range(len(matrix)):
        for j in matrix[i]:
            at = 0
            for k in matrix[j[1]]:
                if k[1] == i:
                    at = k[0]
                    break
            if at == 0:
                return False
    return True


def initial_vector(n):
    v = np.random.randn(n)
    v /= np.linalg.norm(v)
    return v


def power_method(matrix, maxK = 1000000):
    eps = math.pow(10, -10)
    n = len(matrix)
    v = initial_vector(n)
    w = multiply_matrix_with_vector(matrix, v)
    lambd = np.dot(w, v)

    for k in range(maxK):
        v = w / np.linalg.norm(w)
        w = multiply_matrix_with_vector(matrix, v)
        lambd = np.dot(w, v)
        if (np.linalg.norm(w-lambd * v) <= n * eps):
            break
    return lambd, v


def multiply_matrix_with_vector(A, B):
    result = []
    for i in range(len(A)):
        sum = 0
        j = 0
        while j < len(A[i]):
            value_matrix = A[i][j][0]
            value_vector = B[A[i][j][1]]
            sum += value_vector * value_matrix
            j += 1
        result.append(sum)
    return result


if __name__ == "__main__":
    p = int(input("Input p: "))
    n = int(input("Input n: "))
    resultMsg = ""

    map = {1: "a_300.txt",
           2: "a_500.txt",
           3: "a_1000.txt",
           4: "a_1500.txt",
           5: "a_2020.txt",
           }

    if p == n:
        if n > 500:

            A = generateMatrix(p, n, rare=True)
            print("Este simetrica A: " + str(is_symmetrical(A)))
            read = False
            while read is False:
                pick = int(input('Selecteaza numarul fisierului pe care vrei sa il incarci: '))
                if pick >= 1 and pick <= 5:
                    read = True
                else:
                    print('Alegerea trebuie sa fie intre 1 si 5')
            matrix_read, size_matrix = read_matrix(map[pick])
            print("Este simetrica Matricea citita: " + str(is_symmetrical(matrix_read)))


            print("Cea mai mare valoare proprie a lui A: " + str(power_method(A)[0]))
            print("Cea mai mare valoare proprie a Matricei citite: " + str(power_method(matrix_read)[0]))
    else:
        if p > n:
            A = generateMatrix(p, n)
            _, singular_values, _ = np.linalg.svd(A)

            print("Valori singulare ale matricei A:", singular_values)
            print("Rank-ul matricei A:", np.linalg.matrix_rank(A))
            print("Nr de conditionare al matricei A:", np.linalg.cond(A))


