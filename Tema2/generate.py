import numpy as np
if __name__ == "__main__":
    A = np.random.randint(1, 11, size=(100, 100))
    b = np.random.randint(1, 21, size=(1, 100))
    A = np.matrix(A)
    with open('A.txt', 'wb') as f:
        for line in A:
            np.savetxt(f, line, fmt='%i')
    with open('b.txt', 'wb') as f:
        np.savetxt(f, b, fmt='%i')