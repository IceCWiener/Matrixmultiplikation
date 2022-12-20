from utility import Utility


class Decomposition:
    def __init__(self):
        self.util = Utility

    def get_products(self, upper, lower):
        rows_upper = len(upper)
        cols_upper = len(upper[0])
        rows_lower = len(lower)
        cols_lower = len(lower[0])

        if cols_upper != rows_lower:
            print("Matrizen können nicht multipliziert werden. Inkorrekte Dimensionen.")
            return

        result_matrix = [[0 for row in range(cols_lower)] for col in range(rows_upper)]

        for i in range(rows_upper):
            for j in range(cols_lower):
                for k in range(cols_upper):
                    result_matrix[i][j] += upper[i][k] * lower[k][j]
        return result_matrix


    def lu_decomposition(self, matrix):
        n = len(matrix)
        lower = []
        upper = []

        for i in range(n):
            lower.append([0.0] * n)

        for i in range(n):
            upper.append([0.0] * n)

        for j in range(n):
            lower[j][j] = 1.0

        return lower, upper


