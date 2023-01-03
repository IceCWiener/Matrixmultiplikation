import unittest
from gauss import Gauss


class TestGauss(unittest.TestCase):
    def test_should_return_lower_matrix(self):
        matrix = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]

        expected = [
            [1, 1, 0],
            [4, 1, 0],
            [7, 8, 1]
        ]
        gauss = Gauss(matrix)
        self.assertEqual(expected, gauss.lr_decomposition(matrix))