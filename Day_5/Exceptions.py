x = 2
y = 0
names = ["Guido"]
try
    this = "that"
    print(names[y])
    ans = 3/x
    if x < 2:
        raise ValueError("this function requires x >= 2")
except IndexError:
    print("You attempted to use an index larger than our list of names.")
    print("You attempted: {} Highest Index: {}".format(y, len(names)-1))
except ValueError as e:
    print("Raised ValueError:{e}".format(e=e))
# except NameError as e:
#     print("Debug Note: we haven't defined *this* yet.")
except ZeroDivisionError as e:
    print("x cannot be zero: you just attempted {}".format(e))
# except Exception as e:
#     print("I wasn't prepared for this:")
#     print(type(e), e)
