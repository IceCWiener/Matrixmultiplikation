import unittest
from utility import Utility


class TestUtility(unittest.TestCase):
    def test_should_return_products_when_2x2_matrix(self):
        matrix_1 = [
            [2, 3],
            [1, 4]
        ]

        matrix_2 = [
            [5, 2],
            [4, 3]
        ]

        expected = [
            [22, 13],
            [21, 14]
        ]
        util = Utility()
        self.assertEqual(expected, util.get_products(matrix_1, matrix_2))

    def test_should_return_products_when_3x3_matrix(self):
        matrix_1 = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]]

        matrix_2 = [
            [3, 5, 1],
            [7, 2, 4],
            [5, 7, 1]
        ]

        expected = [
            [32, 30, 12],
            [77, 72, 30],
            [122, 114, 48],
        ]

        util = Utility()
        self.assertEqual(expected, util.get_products(matrix_1, matrix_2))

    def test_should_return_products_when_some_0(self):
        matrix_1 = [
            [2, 0],
            [1, 4]
        ]

        matrix_2 = [
            [0, 0],
            [4, 0]
        ]

        expected = [
            [0, 0],
            [16, 0]
        ]
        util = Utility()
        self.assertEqual(expected, util.get_products(matrix_1, matrix_2))

    def test_should_return_string_message_when_incorrect_dimensios(self):
        matrix_1 = [
            [2, 1],
            [1, 4]
        ]

        matrix_2 = [
            [1, 1],
            [4, 1],
            [1, 2]
        ]

        expected = "Matrizen können nicht multipliziert werden. Inkorrekte Dimensionen."
        util = Utility()
        self.assertEqual(expected, util.get_products(matrix_1, matrix_2))