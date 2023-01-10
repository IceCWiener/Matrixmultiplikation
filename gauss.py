class Gauss:

    def lu_decomposition(self, a_matrix):

        # TODO: in utility einfügen, aber n muss bleiben
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

        # Zerlegt a_matrix in L und R Matrix mit Typ 3 der Elementare Zeilenumformungen
        # (R Matrix im Code weiterhin als a_matrix bezeichnet)
        row, column = 0, 0
        while row < n and column < n:
            for i in range(row + 1, n):
                l_matrix[i][column] = a_matrix[i][column] / a_matrix[row][column]
                a_matrix[i] = [modified_row - a_matrix[i][column] / a_matrix[row][column] * pivot_row for modified_row, pivot_row in zip(a_matrix[i], a_matrix[row])]
            row += 1
            column += 1

        return l_matrix, a_matrix
