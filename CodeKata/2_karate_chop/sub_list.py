from typing import Tuple

def return_sub_list(int_to_find:int, absolute_index_of_first_element:int, list_to_split: list) -> Tuple[int, list]:
    pass

def chop(int_to_find: int, list_to_search: list):
    index_of_original_list = 0
    while list_to_search:
        index_of_original_list, list_to_search = return_sub_list(int_to_find, index_of_original_list, list_to_search)
    return index_of_original_list
