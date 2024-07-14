from parameterized import parameterized
from solution import solution, cut_out_foundation_brick

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
    actual = solution(heights)
    assert actual == expected

@parameterized.expand([
    ("two blocks", [1, 2], [[2]]),
    ("saw tooth", [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3], [[2, 3], [2, 3], [2, 3], [2, 3], [2, 3], [2, 3]]),
    ("ends on minimum height", [1, 2, 2, 3, 2, 1, 1], [[2, 2, 3, 2]]),
    ("has minimum hieght appear multiple times in middle", [2, 2, 3, 2, 2, 2, 5, 3], [[3], [5, 3]]),
    ("base is 50", [60, 70, 50, 70], [[60, 70], [70]]),
])
def test_cut_out_foundation_brick(_, heights, expected):
    actual = cut_out_foundation_brick(heights)
    assert actual == expected

