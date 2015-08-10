#!/usr/bin/env python
# HW05_ex00_TextAdventure.py
##############################################################################
# Imports
from sys import exit
import sys
# Body


def infinite_stairway_room(username, count=0):
    print "%s walk through the door to see a dimly lit hallway." % username
    print "At the end of the hallway is a", count * 'long ', 'staircase going towards some light'
    next = raw_input("> ")
    
    # infinite stairs option
    if next == "take stairs":
        print username + 'take the stairs'
        print count
        if (count > 0):
            print "but you're not happy about it"
        infinite_stairway_room(username, count + 1)
    # option 2 == ?????
    if next == "take magic mushroom":
        cthulhu_room(username)


def gold_room(username):
    print "This room is full of gold.  How much do %s take?" % username

    next = raw_input("> ")
    if "0" in next or "1" in next:
        how_much = int(next)
    else:
        why = "Man, learn to type a number."
        dead(why, username)

    if how_much < 50:
        print "Nice, you're not greedy, you win!"
        exit(0)
    else:
        dead("%s, you greedy bastard!") % username


def bear_room(username):
    print "There is a bear here."
    print "The bear has a bunch of honey."
    print "The fat bear is in front of another door."
    print "How are %s going to move the bear?" % username
    bear_moved = False

    while True:
        next = raw_input("> ")

        if next == "take" or next == "honey":
            why = "The bear looks at %s then slaps your face off... now you're in hell" % username
            print(why)
            #dead(why, username)
            infinite_stairway_room(username, count=0)

        elif next == "taunt" and not bear_moved:
            print "The bear has moved from the door. %s can go through it now." % username
            bear_moved = True
        elif next == "taunt" and bear_moved:
            dead("The bear gets pissed off and chews your leg off.")
        elif next == "open" or next == "door" and bear_moved:
            gold_room(username)
        else:
            print "I got no idea what that means."


def cthulhu_room(username):
    print "Here %s see the great evil Cthulhu." % username
    print "He, it, whatever stares at %s and %s goes insane." % (username, username)
    print "Do %s flee for your life or eat your head?" % username

    next = raw_input("> ")

    if "flee" in next:
        main()
    elif "head" in next:
        dead("Well that was tasty!")
    else:
        cthulhu_room(username)


def dead(why, username):
    print why, "Good job!"
    exit(0)


##############################################################################
def main():

    # START the TextAdventure game
    username = sys.argv[1]
    print username + "... what a horrible name"

    print username + " is in a dark room."
    print "There is a door to your right and left."
    print "Which one does %s take?" % username

    next = raw_input("> ")

    if next == "left":
        bear_room(username)
    elif next == "right":
        cthulhu_room(username)
    else:
        why = "%s stumble around the room until you starve." % username
        dead(why, username)

if __name__ == '__main__':
    main()
