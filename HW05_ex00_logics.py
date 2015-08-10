#!/usr/bin/env python
# HW05_ex00_logics.py
##############################################################################

def even_odd():
    """ Print even or odd:
        Takes one integer from user
            accepts only non-word numerals
            must validate
        Determines if even or odd
        Prints determination
        returns None
    """
    

    while True:
        number = raw_input("Give me a number and only a number-- ")

        # try to see if you can evaluate the input... if it's a string then will fail
        try:
            eval(number)

        except:
            print "Not a number you peasant!"

        else:
            # test even/odd using modu of 2
            if int(number) % 2 == 0:
                print "It's even"
                break
            else:
                print "It's odd"
                break


def ten_by_ten():
    """ Prints integers 1 through 100 sequentially in a ten by ten grid."""
    for index in range(1,101):
        if index < 11:
            print(str(index) + " "),
        elif index % 10 == 1:
            print("\n")
            print(index),
        else:
            print(index),   


def find_average():
    """ Takes numeric input (non-word numerals) from the user, one number
    at a time. Once the user types 'done', returns the average.
    """
    count = 0
    added = 0

    while True:
        number = raw_input("Give me a number until you are done--")
        try:
            eval(number)
        except:
            if number == "done":
                break
            else:
                print "Try again"
        else:
            temp = int(number)
            added = added + temp
            count += 1
    average = round(float(added)/float(count),1)
    return average

##############################################################################
def main():
    
    even_odd()
    ten_by_ten()
    print(find_average())


if __name__ == '__main__':
    main()
