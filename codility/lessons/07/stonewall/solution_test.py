from parameterized import parameterized
from solution import solution

TEST_CASES = [
    ("uniform wall of length one", [1], 1),
    ("uniform wall of length four", [3,3,3,3], 1),
    ("example provided", [8, 8, 5, 7, 9, 8, 7, 4, 8], 7),
    ("steps of unit length", [1, 2, 3, 4, 5], 5),
    ("steps of length two", [1, 1, 2, 2, 3, 3, 4, 4, 5, 5], 5),
    ("triangle", [1, 3, 5, 3, 1], 3),
]

@parameterized.expand(TEST_CASES)
def test_solution(_, heights, expected):
    assert solution(heights) == expected

