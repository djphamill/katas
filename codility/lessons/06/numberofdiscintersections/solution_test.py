from solution import solution, populate_points_with_disc_numbers

from parameterized import parameterized

def test_solution():
    pass

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

