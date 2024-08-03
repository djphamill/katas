from math import ceil

def chop(int_to_find: int, list_to_search: list):
    lower_index = 0
    upper_index = len(list_to_search) - 1

    while lower_index < upper_index:
        middle_index = ceil(upper_index - lower_index / 2) + lower_index
        if list_to_search[middle_index] <= int_to_find:
            lower_index = middle_index
        else:
            upper_index = middle_index - 1
        
    found_int = list_to_search and list_to_search[lower_index] == int_to_find
    return -1 if not found_int else lower_index
