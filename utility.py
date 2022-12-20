class Utility:
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

    def pretty_print_matrix(self, list: list[list[float]]):
        for i in list:
            print(f"{i}")