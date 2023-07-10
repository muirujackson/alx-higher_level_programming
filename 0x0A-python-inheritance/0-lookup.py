#!/usr/bin/bash
""" function that returns the list of attribute and method """


def lookup(obj):
    """ the function return list """
    return( list(dir(obj))
