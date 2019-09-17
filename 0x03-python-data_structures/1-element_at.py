#!/usr/bin/python3
def element_at(my_list, idx):
    if idx < 0:
        return None
    len_list = len(my_list)
    if idx >= len_list:
        return None
    else:
        return my_list[idx]
