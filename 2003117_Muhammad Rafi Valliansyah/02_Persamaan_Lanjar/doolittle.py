import numpy as np
from numpy.linalg import inv

def luDecomposition(mat, b, n):

    lower = [[0 for x in range(n)]
             for y in range(n)]
    upper = [[0 for x in range(n)]
             for y in range(n)]

    # Decomposisi Matriks LU (Bawah dan Atas)
    for i in range(n):

        # Upper (Atas)
        for k in range(i, n):

            # Penjumlahan dari L(i, j) * U(j, k)
            sum = 0
            for j in range(i):
                sum += (lower[i][j] * upper[j][k])

            # Mengevaluasi U(i, k)
            upper[i][k] = float(mat[i][k] - sum)

        # Lower (Bawah)
        for k in range(i, n):
            if (i == k):
                lower[i][i] = 1  # Diagonal = 1
            else:

                # Penjumlahan of L(k, j) * U(j, i)
                sum = 0
                for j in range(i):
                    sum += (lower[k][j] * upper[j][i])

                # Mengevaluasi L(k, i)
                lower[k][i] = float((mat[k][i] - sum) / upper[i][i])

    print("Lower\t\t\t\tUpper")
    # Hasil :
    for i in range(n):

        # Lower
        for j in range(n):
            print("%0.2f" % lower[i][j], end="\t")
        print("", end="\t")

        # Upper
        for j in range(n):
            print("%0.2f" % upper[i][j], end="\t")
        print("")
        print("", end="\n")

    # deklarasi variabel untuk menyimpan matriks L dan U
    L = np.array(lower)
    U = np.array(upper)

    # deklarasi variabel untuk menyimpan matriks invers dari L dan U
    invL = inv(L)
    invU = inv(U)

    print("Invers Lower\t\t\t\tInvers Upper")

    for i in range(n):

        # Invers Lower
        for j in range(n):
            print("%0.2f" % invL[i][j], end="\t")
        print("", end="\t")

        # Invers Upper
        for j in range(n):
            print("%0.2f" % invU[i][j], end="\t")
        print("")
        print("", end="\n")

    # menurut pada rumus Ly = b menjadi y = invers(L) . b
    # mengalikan matriks invers L dengan matriks b

    # b = np.array([[1], [2], [3]])
    y = np.dot(invL, b)

    # menurut rumus Ux = y menjadi x = invers(U) . y
    # mengalikan matriks invers U dengan matriks y dan disimpan dalam variabel eks(x)
    eks = np.dot(invU, y)

    # mengisi variabel x,y,z
    # print(eks)
    for i in range(n):
        print("Nilai X[%d] adalah %0.4f" % (i, eks[i][0]))

# "%.2f" %

# Matriks
# mat = [[2, -1, -2],
#       [-4, 6, 3],
#       [-4, -2, 8]]


# mat = [[1, -1, 2, -1],
#        [1, 1, 1, 0],
#        [2, -2, 3, -3],
#        [1, -1, 4, 3]]

mat = [[1, 2, 3],
       [3, -1, 2],
       [4, -6, -4]]

riks = np.array([[5], [8], [-2]])

# mat = [[8, -2, -1, 0, 0, 0],
#        [-2, 9, -4, -1, -1, 0],
#        [-1, -3, 7, -1,-1,-2],
#        [0, -4, -2, 12, 12,-5],
#        [0, 0, -7, -3, -3, 15]]

# riks = np.array([[5],[2],[0],[1],[5]])


# mat = np.array([[4, 1, 2],
#        [3, 3, 1],
#        [2, 1, 3]])

# riks = np.array([[1], [2], [3]])

# riks = np.array([[1], [2], [3], [4]])

luDecomposition(mat, riks, 3)
# luDecomposition(mat, riks, 4)