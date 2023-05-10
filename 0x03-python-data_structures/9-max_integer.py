#!/usr/bin/python3

'''finds the biggest integer in a list'''
def max_integer(my_list=[]):
    '''return none if list is empty'''
    if my_list == []:
        return None
    maximum = my_list[0]
    '''or loop through the list to return the max'''
    for i in my_list:
        if i > maximum:
            maximum = i
    return maximum
