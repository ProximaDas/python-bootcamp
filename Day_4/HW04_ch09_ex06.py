#!/usr/bin/env python3

# (1)
# Write a function called is_abecedarian that returns True if the letters in a
# word appear in alphabetical order (double letters are ok).
#   - write is_abecedarian
# (2)
# How many abecedarian words are there in roster.txt?
#   - write additional function(s) to assist you
#   - number of abecedarian words:
##############################################################################
# Imports


# Body
def is_abecedarian(word):
    return word == "".join(sorted(word))


def how_many_abecedarian():
    with open("words2.txt", "r") as fin:
        words = [word.strip() for word in fin.readlines()]
    return sum([is_abecedarian(word) for word in words])


##############################################################################
def main():
    pass  # Call your function(s) here.
    # print(is_abecedarian("abc"))
    # print(is_abecedarian("zyxwvutsrqponmlkjihgfedcba"))
    print(how_many_abecedarian())


if __name__ == '__main__':
    main()
