from parameterized import parameterized
from solution import solution

TEST_CASES = [
    ("uniform wall", [1,1,1,1], 1),
]

@parameterized.expand(TEST_CASES)
def test_solution(_, heights, expected):
    assert solution(heights) == expected

