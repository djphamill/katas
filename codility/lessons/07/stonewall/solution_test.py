from parameterized import parameterized
from solution import solution

TEST_CASES = [
    ("uniform wall of length one", [1], 1),
    ("uniform wall of length four", [3,3,3,3], 1),
]

@parameterized.expand(TEST_CASES)
def test_solution(_, heights, expected):
    assert solution(heights) == expected

