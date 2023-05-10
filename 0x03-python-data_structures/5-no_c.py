#!/usr/bin/python3

'''a function that removes all characters c and C from a string'''
def no_c(my_string):
    return my_string.translate({ord(i): None for i in "Cc"})
