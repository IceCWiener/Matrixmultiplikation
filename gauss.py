from utility import Utility


class Gauss:
    def __init__(self) -> None:
        self.util = Utility()

    def lu_decomposition(self, a_matrix):
        # TODO: in utility einfügen, aber n muss bleiben
        # TODO: round auf 4 stellen (mali)
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
                l_matrix[i][column] = round(a_matrix[i][column] / a_matrix[row][column], 4)
                a_matrix[i] = [round(modified_row - l_matrix[i][column]
                               * pivot_row, 4) for modified_row, pivot_row in self.pair_items(a_matrix[i], a_matrix[row])]
            row += 1
            column += 1

        return l_matrix, a_matrix


    def pair_items(self, part1: tuple, part2: tuple):
        if len(part1) >= len(part2):
            count = len(part2)
        else:
            count = len(part1)

        result = []
        for i in range(count):
            temp = [part1[i], part2[i]]
            result.append(temp)

        return result
