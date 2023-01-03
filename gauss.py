import numpy as np


class Gauss:

    def lu_decomposition(self, a_matrix):

        if type(a_matrix) == list:
            a_matrix = np.array(a_matrix)

        # Überprüfen, ob die Matrix quadratisch ist
        n = a_matrix.shape[0]
        if a_matrix.shape[1] != n:
            raise ValueError("Die Matrix ist nicht quadratisch.")

        # Erstellen der leeren unteren Dreiecksmatrix l_matrix
        l_matrix = np.zeros((n, n))
        # Erstellen der leeren oberen Dreiecksmatrix u_matrix
        u_matrix = np.zeros((n, n))

        # Zerlegen der a_matrix in l_matrix und u_matrix
        for i in range(n):  # i = Zeilen
            # Berechnen der Elemente der i-ten Spalte von l_matrix und der i-ten Zeile von u_matrix
            for j in range(i + 1):  # j = Spalten
                s = sum(l_matrix[i][k] * u_matrix[k][j] for k in range(j))
                if i == j:
                    l_matrix[i][j] = np.sqrt(a_matrix[i][i] - s)
                    u_matrix[i][j] = np.sqrt(a_matrix[i][i] - s)
                else:
                    l_matrix[i][j] = (1.0 / l_matrix[j][j] * (a_matrix[i][j] - s))
                    u_matrix[j][i] = (1.0 / u_matrix[j][j] * (a_matrix[i][j] - s))

        return l_matrix.tolist(), u_matrix.tolist()
