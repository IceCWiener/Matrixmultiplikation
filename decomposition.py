from utility import Utility


class Decomposition:
    def __init__(self):
        self.util = Utility

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


