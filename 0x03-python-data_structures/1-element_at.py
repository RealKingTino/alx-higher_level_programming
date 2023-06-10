#!/usr/bin/python3
def element_at(my_list, idx):
    lx = len(my_list)
    if idx < 0 or idx >= lx:
        return None
    return my_list[idx]
