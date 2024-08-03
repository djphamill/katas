from parameterized import parameterized, parameterized_class
import unittest

class TestChop(unittest.TestCase):

    def test_chop_empty_list(self):
        expected_value, int_to_find, list_to_search = (-1, 3, [])
        assert expected_value == self.chopper(int_to_find, list_to_search)

    def test_chop_list_of_one_without_int(self):
        expected_value, int_to_find, list_to_search = (-1, 3, [1])
        assert expected_value == self.chopper(int_to_find, list_to_search)

    def test_chop_list_of_one_with_int(self):
        expected_value, int_to_find, list_to_search = (0, 1, [1])
        assert expected_value == self.chopper(int_to_find, list_to_search)

    def test_chop_listt_of_two_int_at_first_element(self):
        expected_value, int_to_find, list_to_search = (0, 1, [1, 2])
        assert expected_value == self.chopper(int_to_find, list_to_search)

    def test_chop_list_of_two_int_at_second_element(self):
        expected_value, int_to_find, list_to_search = (1, 1, [0, 1])
        assert expected_value == self.chopper(int_to_find, list_to_search)

    def test_chop_list_of_two_int_above_list(self):
        expected_value, int_to_find, list_to_search = (-1, 2, [0, 1])
        assert expected_value == self.chopper(int_to_find, list_to_search)

    def test_chop_list_of_two_int_below_list(self):
        expected_value, int_to_find, list_to_search = (-1, 0, [1, 22])
        assert expected_value == self.chopper(int_to_find, list_to_search)

    @parameterized.expand([
        (0,  1, [1, 3, 5]),
        (1,  3, [1, 3, 5]),
        (2,  5, [1, 3, 5]),
        (-1, 0, [1, 3, 5]),
        (-1, 2, [1, 3, 5]),
        (-1, 4, [1, 3, 5]),
        (-1, 6, [1, 3, 5]),
        (0,  1, [1, 3, 5, 7]),
        (1,  3, [1, 3, 5, 7]),
        (2,  5, [1, 3, 5, 7]),
        (3,  7, [1, 3, 5, 7]),
        (-1, 0, [1, 3, 5, 7]),
        (-1, 2, [1, 3, 5, 7]),
        (-1, 4, [1, 3, 5, 7]),
        (-1, 6, [1, 3, 5, 7]),
        (-1, 8, [1, 3, 5, 7]),
        (-1, -1, [2, 3, 5, 6, 8, 10, 11, 13, 22, 99]),
        (-1, 1, [2, 3, 5, 6, 8, 10, 11, 13, 22, 99]),
        (-1, 100, [2, 3, 5, 6, 8, 10, 11, 13, 22, 99]),
        (0, 2, [2, 3, 5, 6, 8, 10, 11, 13, 22, 99]),
        (4, 8, [2, 3, 5, 6, 8, 10, 11, 13, 22, 99]),
        (5, 10, [2, 3, 5, 6, 8, 10, 11, 13, 22, 99]),
        (6, 11, [2, 3, 5, 6, 8, 10, 11, 13, 22, 99]),
    ])
    def test_chops_for_list_of_lengths_greater_than_two(self, expected_value, int_to_find, list_to_search):
        assert expected_value == self.chopper(int_to_find, list_to_search)

