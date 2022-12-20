from decomposition import Decomposition
from utility import Utility


def collect_matrix():
    return []


if __name__ == '__main__':
    util = Utility()

    a_matrix = [[1, 2, 3],
                [4, 5, 6], 
                [7, 8, 9]]

    b_matrix = [[3, 5, 1],
                [7, 2, 4],
                [5, 7, 1]]

    matrix = collect_matrix()

    decomposition = Decomposition()
    result_matrix = util.get_products(a_matrix, b_matrix)
    util.pretty_print_matrix(result_matrix)
    print(f'\nMatrix 1: {matrix}\n')
