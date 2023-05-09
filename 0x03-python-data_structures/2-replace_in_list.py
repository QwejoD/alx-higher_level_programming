#!/usr/bin/python3
'''a function that replaces an element of a list at a specific position '''

'''function definition'''
def replace_in_list(my_list, idx, element):

    '''if index is negative or out of range the fxn should return the original list'''
    if idx < 0 or idx >= len(my_list):
        return my_list
    my_list[idx] = element
    return my_list
