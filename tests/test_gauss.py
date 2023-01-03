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
            [1, 0, 0],
            [4, 1, 0],
            [7, 8, 1]
        ]
        gauss = Gauss()
        self.assertEqual(expected, gauss.lu_decomposition(matrix)[0])

    def test_should_return_upper_matrix(self):
        matrix = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]

        expected = [
            [1, 2, 3],
            [0, 1, 2],
            [0, 0, 1]
        ]
        gauss = Gauss()
        self.assertEqual(expected, gauss.lu_decomposition(matrix)[1])    

    def test_should_raise_value_error(self):
        matrix = [
            [1, 2, 3],
            [4, 5, 6]
        ]

        expected = ValueError

        gauss = Gauss()
        with self.assertRaises(expected): 
            gauss.lu_decomposition(matrix)