from typing import List

def solution(heights: List[int]):
    distinct_heights = set(heights)
    if len(distinct_heights) == 1:
        return 1

