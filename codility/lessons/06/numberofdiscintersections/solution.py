from typing import List

def solution(radii: List[int]):
    pass

def populate_points_with_disc_numbers(radius: int, disc_number: int, current_coverage: List[List[int]]) -> List[List[int]]:
    start_postion_to_populate = max(disc_number - radius, 0)
    end_position_to_populate = disc_number + radius
    for position in range(start_postion_to_populate, end_position_to_populate + 1):
        if len(current_coverage) < position + 1:
            current_coverage.append([])
        current_coverage[position].append(disc_number)
    return current_coverage

