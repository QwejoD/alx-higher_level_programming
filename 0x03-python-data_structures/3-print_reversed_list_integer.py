#!/usr/bin/python3
'''Prints all integers of a list in the reverse order'''

'''Function definition'''
def print_reversed_list_integer(my_list=[]):
    if my_list:
        '''reverse list'''
        reversed_list = my_list[::-1]
        '''print integer line by line'''
        for i in reversed_list:
            print("{:d}".format(i))
