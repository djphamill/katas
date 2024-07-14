from solution import solution, populate_points_with_disc_numbers

from parameterized import parameterized

@parameterized.expand([
    ("example provided", [1, 5, 2, 1, 4, 0], 11),
    ("trivial", [4], 0),
    ("none overlap", [0, 0, 0, 0], 0),
    ("kissing only", [1, 0], 1),
    ("only one pair, but lots", [99, 100], 1)
])
def test_solution(_, radii, expected):
    actual = solution(radii)
    assert actual == expected

@parameterized.expand([
    (0, 2, [[], [], [], []], [[], [], [2], []]),
    (2, 2, [[], [], [], [], []], [[2], [2], [2], [2], [2]]),
    (2, 0, [[], [], [], [], []], [[0], [0], [0], [], []]),
    (1, 0, [[], [], [], [], []], [[0], [0], [], [], []]),
    (1, 0, [[], [], [], [], []], [[0], [0], [], [], []]),
    (1, 0, [], [[0], [0]]),
    (1, 0, [[2]], [[2, 0], [0]]),
])
def test_populate_points_with_disc_numbers(radius, disc_number, current_coverage, expected):
    actual = populate_points_with_disc_numbers(radius, disc_number, current_coverage)
    assert actual == expected

