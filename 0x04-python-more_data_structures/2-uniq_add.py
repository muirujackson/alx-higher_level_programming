#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniqueNumbers = set()
    sum = 0
    for number in my_list:
        uniqueNumbers.add(number)
    for number in uniqueNumbers:
        sum += number
    return (sum)
