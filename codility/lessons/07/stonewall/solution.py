from typing import List

def solution(heights: List[int]) -> int:
    number_of_bricks = 0
    distinct_heights = set(heights)
    if len(distinct_heights) == 1:
        number_of_bricks += 1
        return number_of_bricks
    else:
        number_of_bricks += 1
        new_group_of_heights = cut_out_foundation_brick(heights)
        for heights in new_group_of_heights:
            number_of_bricks += solution(heights)
        return number_of_bricks

def cut_out_foundation_brick(heights: List[int]) -> List[List[int]]:
    minimum_height = min(heights)
    group_of_new_heights = []
    new_heights = []
    for height in heights:
        if height != minimum_height:
            new_heights.append(height)
        else:
            if new_heights:
                group_of_new_heights.append(new_heights)
            new_heights = []
    if new_heights:
        group_of_new_heights.append(new_heights)
    return group_of_new_heights

