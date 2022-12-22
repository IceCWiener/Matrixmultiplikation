import unittest
from decomposition import Decomposition


class TestDecomposition(unittest.TestCase):

    def test_should_return_lower_matrix(self):
        matrix = [
            [2, 3],
            [6, 13]
        ]

        lower = [
            [1, 0],
            [3, 1],
        ]
        decomposition = Decomposition()
        self.assertEqual(lower, decomposition.lu_decomposition(matrix)[0])

    def test_should_return_upper_matrix(self):
        matrix = [
            [2, 3],
            [6, 13]
        ]

        upper = [
            [2, 3],
            [0, 4]
        ]

        decomposition = Decomposition()

        self.assertEqual(upper, decomposition.lu_decomposition(matrix)[1])


