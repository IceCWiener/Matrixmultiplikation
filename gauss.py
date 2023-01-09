import numpy as np


class Gauss:

    def row_mod(self, matrix, i_row, j_row, factor):
        matrix[i_row] = [a + factor * b for a, b in zip(matrix[i_row], matrix[j_row])]
        return matrix[i_row]

    def lu_decomposition(self, a_matrix):

        # TODO: in utility einfügen
        # Überprüft, ob die Matrix quadratisch ist
        n = len(a_matrix)
        for x in range(n):
            m = len(a_matrix[x])
            if m != n:
                raise ValueError("Die Matrix ist nicht quadratisch.")

        # TODO: in utility einfügen
        # Erstellt eine leere untere Dreiecksmatrix
        l_matrix = [0.] * n
        for y in range(n):
            l_matrix[y] = [0.] * n
        for z in range(n):
            l_matrix[z][z] = 1.

        # Zerlegt a_matrix in l_matrix und u_matrix (im Code weiterhin als a_matrix)
        row, col = 0, 0
        rows, cols = n, n
        while row < rows and col < cols:
            pivot = a_matrix[row][col]
            for i in range(row + 1, rows):
                if a_matrix[i][col] != 0:
                    l_matrix[i][col] = a_matrix[i][col] / pivot
                    a_matrix[i] = self.row_mod(a_matrix, i, row, -a_matrix[i][col] / pivot)
            row += 1
            col += 1

        return l_matrix, a_matrix
