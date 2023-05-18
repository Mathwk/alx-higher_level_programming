#!/usr/bin/python3
def uniq_add(my_list=[]):
    new_l = set(my_list)
    result = 0
    for i in new_l:
        result += i
    return result
