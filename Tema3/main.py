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


def transpose_matrix(A,a_size):
    result = [[] for _ in range(a_size)]
    for i in range(a_size):
        for j in range(len(A[i])):
            result[int(A[i][j][1])].append([A[i][j][0], i])
    for i in range(a_size):
        if result[i] == []:
            del result[i]
    for i in range(len(result)):
        result[i] = sorted(result[i], key = lambda x: x[1] )
    return result


def multiply_matrix(A, B, b_size):
    B = transpose_matrix(B, b_size)
    result = [[] for _ in range(len(A))]

    for i in range(len(A)):
        for j in range(len(A)):
            sum = 0
            k = 0
            l = 0
            len_b = len(B[j])
            len_a = len(A[i])
            while l < len_b and k < len_a:
                if A[i][k][1] != B[j][l][1]:
                    if A[i][k][1] < B[j][l][1]:
                        k = k + 1
                    else:
                        l = l + 1
                else:
                    sum = sum + B[j][l][0] * A[i][k][0]
                    k = k + 1
                    l = l + 1
            if sum != 0:
                result[i].append([sum, j])
    return result



def sum_matrix(A, B, n):
    result = [[] for _ in range(n)]
    for i in range(n):
        for j in range(len(A[i])):
            result[i].append(A[i][j])
    for i in range(n):
        for j in range(len(B[i])):
            flag = 0
            for k in range(len(result[i])):
                column_result = result[i][k][1]
                column_B = B[i][j][1]
                if column_B == column_result:
                    result[i][k][0] = result[i][k][0] + B[i][j][0]
                    flag = 1
            if flag == 0:
                result[i].append(B[i][j])
    for i in range(n):
        result[i] = sorted(result[i], key=lambda x: x[1])
    return result


def equals(operatie, A, B):
    e = math.pow(10, -10)
    flag = True
    for i in range(len(A)):
        for j in range(len(A[i])):
            if A[i][j][1] != B[i][j][1]:
                flag = False
            else:
                if e < abs(A[i][j][0] - B[i][j][0]):
                    flag = False
    if flag == True:
        print(operatie + "corecta")
    else:
        print(operatie + "gresita")


if __name__ == "__main__":
    a_rare, a_size = read_matrix("a.txt")
    b_rare, b_size = read_matrix("b.txt")
    aplusb, aplusb_size = read_matrix("aplusb.txt")
    myaplusb = sum_matrix(a_rare,b_rare, a_size)


    equals("Adunare ",myaplusb, aplusb)

    a_rare, a_size = read_matrix("a.txt")
    b_rare, b_size = read_matrix("b.txt")

    aorib, aorib_size = read_matrix("aorib.txt")
    #print(aorib[0])
    myaorib = multiply_matrix(a_rare, b_rare, b_size)
    #print(myaorib[0])

    equals("Inmultire ", myaorib, aorib)