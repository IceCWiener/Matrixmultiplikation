import ast
from numbers import Number


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

    def format_matrix_list_to_str(self, matrix: list[list[float]]):
        """changes a list-type matrix into a str-matrix with new-lines added"""
        matrix = str(matrix).split('],')
        result = ""

        for i in range(len(matrix)-1):
            result += matrix[i] + "],\n"
        result += matrix[len(matrix)-1]

        return result

    def format_matrix_str_to_list(self, matrix: str):
        """formats a matrix from string for list and casts all numbers to floats"""
        try:
            result = ast.literal_eval(matrix)
            if isinstance(result[0], Number):
                for i in range(len(result)):
                    result[i] = [result[i]]
            result = [[float(j) for j in i] for i in result]

            return result
        except:
            return (
                "Der eingegebene Matrix-String konnte nicht in eine Liste konvertiert werden. Bitte die Eingabe in das Format: [[1, 2], [3, 4]] ändern.")

    def manual_zip(self, part1: tuple, part2: tuple):
        count = len(part1) if len(part1) > len(part2) else len(part2)

        result = []
        for i in range(count):
            temp = []
            temp.append(part1[i])
            temp.append(part2[i])
            result.append(temp)

        return result
