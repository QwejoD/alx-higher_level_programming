#!/usr/bin/python3
'''finds all multiples of 2 in a list'''

def divisible_by_2(my_list=[]):
    multiple_of_two = []
    '''return list of all the multiples'''
    for i in my_list:
        if i % 2 == 0:
            multiple_of_two.append(True)
        else:
            multiple_of_two.append(False)
    return multiple_of_two
