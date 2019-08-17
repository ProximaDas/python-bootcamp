#!/usr/bin/env python3
# HW08_ch11_ex02a
# This is discussed in ThinkPython2 but not formally an exercise.
# Dictionaries have a method called 'get' that takes a key and a default value.
# If the key appears in the dictionary, get returns the corresponding value;
# otherwise it returns the default value. For example:

# >>> h = histogram('a')
# >>> print h
# {'a': 1}
# >>> h.get('a', 0)
# 1
# >>> h.get('b', 0)
# 0

# (1) Use get to write histogram_old more concisely. You should be able to
# eliminate the if statement.

# (2) Use histogram_new to take pledge.txt and create a dict histogram with
# word counts (do not change the case of the words).
###############################################################################
# Imports


# Body
def histogram_old(lst):
    d = dict()
    for word in lst:
        if word not in d:
            d[word] = 1
        else:
            d[word] += 1
    return d


def histogram_new(lst):
    pass


def get_pledge_list():
    """ Opens pledge.txt and converts to a list, each item is a word in
    the order it appears in the original file. Returns the list.
    """
    # Write your code here.
    pass
    # return pledge_list (uncomment this)


###############################################################################
def main():  # DO NOT CHANGE BELOW
    print(histogram_new(get_pledge_list()))


if __name__ == '__main__':
    main()
