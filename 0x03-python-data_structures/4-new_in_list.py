#!/usr/bin/python3

'''Function replaces element in a list at a specific position'''
def new_in_list(my_list, idx, element):
    if idx < 0 or idx >= len(my_list):
        return my_list
    new = my_list.copy()
    new[idx] = element
    return new
