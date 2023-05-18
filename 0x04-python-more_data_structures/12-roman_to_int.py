#!/usr/bin/python3
def to_subtract(list_num):
    to_sub = 0
    max_list = max(list_num)
    for n in list_num:
        if max_list > n:
            to_sub += n
    return (max_list - to_sub)


def roman_to_int(roman_string):
    if not roman_string:
        return 0
    if not isinstance(roman_string, str):
        return 0
    r_num = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    roman_keys = list(r_num.keys())
    num = 0
    roman_l = 0
    num_l = [0]
    for c in roman_string:
        for ro_num in roman_keys:
            if ro_num == c:
                if r_num.get(c) <= roman_l:
                    num += to_subtract(num_l)
                    num_l = [r_num.get(c)]
                else:
                    num_l.append(r_num.get(c))
                roman_l = r_num.get(c)
    num += to_subtract(num_l)
    return (num)
