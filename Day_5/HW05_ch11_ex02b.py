#!/usr/bin/env python3
# HW08_ch11_ex02b
# This borrows from exercise two in the book.
# Dictionaries have a method called keys that returns the keys of the
# dictionary, in no particular order(?), as a list.

# (1) Modify print_hist_old to print the keys and their values in alphabetical
# order.

# (2) Paste in your completed functions from HW08_ch11_ex02a.py

# (3) Within main() make the appropriate function calls (importing from
# HW08_ch11_ex02a) to print the alphabetical histogram of pledge.txt
###############################################################################
# Imports
import HW08_ch11_ex02a


# Body
def print_hist_old(h):
    for word in h:
        print(word, h[word])


def print_hist_new(h):
    pass


###############################################################################
def main():
    """ Calls print_hist_new with the appropriate arguments, importing from
    HW08_ch11_ex02a to print the histogram of pledge.txt.
    """
    pass

if __name__ == '__main__':
    main()
