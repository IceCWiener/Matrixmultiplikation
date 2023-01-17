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
                l_matrix[i][column] = a_matrix[i][column] / a_matrix[row][column]
                a_matrix[i] = [modified_row - l_matrix[i][column]
                               * pivot_row for modified_row, pivot_row in self.manual_zip(a_matrix[i], a_matrix[row])]
            row += 1
            column += 1

        return l_matrix, a_matrix


    def manual_zip(self, part1: tuple, part2: tuple):
        #TODO: write test for this function (Nina)
        #TODO: funktion umbenennen (mathe spezifisch :) )(Nina)
        count = len(part1) if len(part1) > len(part2) else len(part2)

        result = []
        for i in range(count):
            temp = []
            temp.append(part1[i])
            temp.append(part2[i])
            result.append(temp)

        return result
