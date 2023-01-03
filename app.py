from decomposition import Decomposition
from utility import Utility
from gauss import Gauss
import numpy as np


def collect_matrix():
    return []


if __name__ == '__main__':
    util = Utility()

    # a_matrix = [[1, 2, 3],
    #             [4, 5, 6],
    #             [7, 8, 9]]
    #
    # b_matrix = [[3, 5, 1],
    #             [7, 2, 4],
    #             [5, 7, 1]]
    #
    # matrix = collect_matrix()
    #
    # decomposition = Decomposition()
    # result_matrix = util.get_products(a_matrix, b_matrix)
    # util.pretty_print_matrix(result_matrix)
    # print(f'\nMatrix 1: {matrix}\n')

    # Beispielmatrix
    a_matrix = np.array([[4, 12, -16], [12, 37, -43], [-16, -43, 98]])

    # Durchführen der LR-Zerlegung
    gauss_obj = Gauss(a_matrix)
    l_matrix, r_matrix = gauss_obj.lr_decomposition(a_matrix)

    # Überprüfen, ob L*R die Matrix A ergibt
    print("Matrix A")
    print(np.dot(l_matrix, r_matrix))