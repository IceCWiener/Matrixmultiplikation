import unittest
from utility import Utility


class TestUtility(unittest.TestCase):
    def test_should_return_products(self):
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
