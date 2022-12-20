import unittest
from decomposition import Decomposition


class TestDecomposition(unittest.TestCase):

    def test_should_return_lower_matrix(self):
        matrix = [
            [2, 3, 1],
            [6, 13, 5],
            [2, 19, 10]
            ]

        lower = [
            [1.0, 0.0, 0.0],
            [3.0, 1.0, 0.0],
            [1.0, 4.0, 1.0]
        ]
        decomposition = Decomposition()
        self.assertEqual(lower, decomposition.lu_decomposition(matrix)[0])

    def test_should_return_upper_matrix(self):
        matrix =[
            [2, 3, 1],
            [6, 13, 5],
            [2, 19, 10]
        ]

        upper = [
            [1, 1.5, 0.5],
            [0, 7.5, 4.5],
            [0, 0, 9.5]
        ]
        decomposition = Decomposition()

        self.assertEqual(upper, decomposition.lu_decomposition(matrix)[1])


