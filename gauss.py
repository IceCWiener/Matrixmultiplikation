import numpy as np


class Gauss:

    def __init__(self, matrix):
        self.matrix = matrix

    def lr_decomposition(self, a_matrix):
        # Überprüfen, ob die Matrix quadratisch ist
        n = a_matrix.shape[0]
        if a_matrix.shape[1] != n:
            raise ValueError("Die Matrix ist nicht quadratisch.")

        # Erstellen der leeren unteren Dreiecksmatrix l_matrix
        l_matrix = np.zeros((n, n))
        # Erstellen der leeren oberen Dreiecksmatrix r_matrix
        r_matrix = np.zeros((n, n))

        # Zerlegen der a_matrix in l_matrix und r_matrix
        for i in range(n):  # i = Zeilen
            # Berechnen der Elemente der i-ten Spalte von l_matrix und der i-ten Zeile von r_matrix
            for j in range(i + 1):  # j = Spalten
                s = sum(l_matrix[i][k] * r_matrix[k][j] for k in range(j))
                if i == j:
                    l_matrix[i][j] = np.sqrt(a_matrix[i][i] - s)
                    r_matrix[i][j] = np.sqrt(a_matrix[i][i] - s)
                else:
                    l_matrix[i][j] = (1.0 / l_matrix[j][j] * (a_matrix[i][j] - s))
                    r_matrix[j][i] = (1.0 / r_matrix[j][j] * (a_matrix[i][j] - s))
        print("R Matrix")
        print(r_matrix)
        print("L Matrix")
        print(l_matrix)
        return l_matrix, r_matrix

