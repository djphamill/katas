from parameterized import parameterized
from solution import solution

TEST_CASES = [
    ("no wall", [0,0,0,0], 0),
    ("uniform wall", [1,1,1,1], 1),
]

@parameterized.expand(TEST_CASES)
def test_solution(_, heights, expected):
    assert solution(heights) == expected

