from typing import List
from itertools import combinations


def solution(radii: List[int]):
    discs_on_points: List[List[int]] = []
    for disc_number, radius in enumerate(radii):
        discs_on_points = populate_points_with_disc_numbers(
            radius, disc_number, discs_on_points)

    pairings = set()
    for discs_on_point in discs_on_points:
        for pairing in combinations(discs_on_point, r=2):
            pairings.add(pairing)

    return len(pairings)


def populate_points_with_disc_numbers(radius: int,
                                      disc_number: int,
                                      discs_on_points: List[List[int]]) -> List[List[int]]:
    start_postion_to_populate = max(disc_number - radius, 0)
    end_position_to_populate = disc_number + radius
    for position in range(start_postion_to_populate, end_position_to_populate + 1):
        if len(discs_on_points) < position + 1:
            discs_on_points.append([])
        discs_on_points[position].append(disc_number)
    return discs_on_points
