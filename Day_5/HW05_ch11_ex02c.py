#!/usr/bin/env python3
# HW08_ch11_ex02c.py
# (1) Modify reverse_lookup_old so that it builds and returns a list of all
# keys that map to v, or an empty list if there are none.

# (2) Paste in your completed functions from HW08_ch11_ex02a.py

# (3) Do not edit what is in main(). It should print what is returned, a list
# of the keys that map to the values passed.
###############################################################################
# Imports
import HW08_ch11_ex02a


# Body
def reverse_lookup_old(d, v):
    for k in d:
        if d[k] == v:
            return k
    raise ValueError


def reverse_lookup_new(d, v):
    pass


###############################################################################
def main():   # THE CODE SHOULD EVENTUALLY RUN WITH THE BELOW
    pledge_histogram = HW08_ch11_ex02a.histogram_new(
                       HW08_ch11_ex02a.get_pledge_list())

    print("Using a list comprehension:")
    print(reverse_lookup_new(pledge_histogram, 1))
    print(reverse_lookup_new(pledge_histogram, 9))
    print(reverse_lookup_new(pledge_histogram, "Python"))


if __name__ == '__main__':
    main()
