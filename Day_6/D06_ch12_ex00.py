#!/usr/bin/env python3
# See section 12.4
# Many of the built-in functions use variable-length argument tuples.
# For example, max and min can take any number of arguments:
# >>> max(1,2,3)
# 3
# But sum does not.
# >>> sum(1,2,3)
# TypeError: sum expected at most 2 arguments, got 3
# (1) Write a function called sumall that takes any number of arguments and
#     returns their sum.
###############################################################################
# Imports

# Body


##############################################################################
def main():   # DO NOT CHANGE BELOW
    print(sumall(1, 2, 3, 4, 5))
    print(sumall(1))
    print(sumall(1, 2))


if __name__ == '__main__':
    main()
