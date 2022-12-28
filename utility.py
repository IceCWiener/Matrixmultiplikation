class Utility:
    def get_products(self, matrix_a, matrix_b):
        rows_a = len(matrix_a)
        cols_a = len(matrix_a[0])
        rows_b = len(matrix_b)
        cols_b = len(matrix_b[0])

        if cols_a != rows_b:
            message = "Matrizen können nicht multipliziert werden. Inkorrekte Dimensionen."
            return message

        result_matrix = [[0 for row in range(cols_b)] for col in range(rows_a)]

        for i in range(rows_a):
            for j in range(cols_b):
                for k in range(cols_a):
                    result_matrix[i][j] += matrix_a[i][k] * matrix_b[k][j]
        return result_matrix

    def pretty_print_matrix(self, matrix: list[list[float]]):
        for i in matrix:
            print(f"{i}")
