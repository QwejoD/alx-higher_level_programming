#!/usr/bin/python3
'''A function that prints all integers in a list'''

'''function definition'''
def print_list_integer(my_list=[]):

    '''print integer'''
    for i in my_list:
        print("{:d}".format(int(i)))
