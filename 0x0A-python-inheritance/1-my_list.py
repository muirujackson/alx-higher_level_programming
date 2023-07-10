#!/usr/bin/pythom3
"""
    This module create a MyList and sort the list in ascending order
"""

class Mylist(list):
    """ This class extend the list """


    def print_sorted(self):
        """ this method sort a list in ascending order """


        print(sorted(self))

