from math import ceil
from typing import List, Tuple


def chop(number_to_find: int, list_to_search: List[int]) -> int:
    "The recursive choppper"
    if not list_to_search:
        return -1

    if len(list_to_search) == 1:
        if list_to_search[0] == number_to_find:
            return 0
        else:
            return -1
    
    bottom_half, top_half = split_list(list_to_search)
    if should_look_in_top_half(top_half, number_to_find):
        position_in_list = chop(number_to_find, top_half)
        correction = len(bottom_half)
    else:
        position_in_list = chop(number_to_find, bottom_half)
        correction = 0

    is_number_not_in_list = position_in_list == -1
    if is_number_not_in_list:
        return -1
    return position_in_list + correction


def split_list(list_to_split: list) -> Tuple[list, list]:
    length_of_list = len(list_to_split)
    half_length_of_list = int(length_of_list / 2)

    return list_to_split[:half_length_of_list], list_to_split[half_length_of_list:]


def should_look_in_top_half(top_half: List, number_to_find: int) -> bool:
    first_element_in_top_half = top_half[0]

    return first_element_in_top_half <= number_to_find
