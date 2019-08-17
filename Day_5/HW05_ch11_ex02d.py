#!/usr/bin/env python3
# HW08_ch11_ex02d.py
# (1) Write a more concise version of invert_dict_old.

# (2) Paste in your completed functions from HW08_ch11_ex02a.py

# (3) Update print_hist_new from HW08_ch11_ex02b.py to be able to print
# a sorted version of the dict (print key/value pairs from 0 through the
# largest key values, (and those in between))
# Ex. If d = {1:["this, that"], 3: ["the"]}, it prints:
#    '1: ["this", "that"]'
#    '2:'
#    '3: ["the"]'
###############################################################################
# Imports
import HW08_ch11_ex02a


# Body
def invert_dict_old(d):
    inverse = dict()
    for key in d:
        val = d[key]
        if val not in inverse:
            inverse[val] = [key]
        else:
            inverse[val].append(key)
    return inverse


def invert_dict_new(d):
    pass


def print_hist_newest(d):
    pass


###############################################################################
def main():  # THE CODE SHOULD EVENTUALLY RUN WITH THE BELOW
    pledge_histogram = HW08_ch11_ex02a.histogram_new(
                       HW08_ch11_ex02a.get_pledge_list())

    pledge_invert = invert_dict_new(pledge_histogram)
    print_hist_newest(pledge_invert)


if __name__ == '__main__':
    main()
