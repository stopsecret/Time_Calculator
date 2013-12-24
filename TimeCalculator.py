#! /usr/bin/env python
"""
    Time Sheet Input Calculator.
    Copyright 2013 Stopsecret Design.
    If you enjoyed, please leave a comment on my website.
    http://stopsecretdesign.wordpress.com/

    You are free to use this script for yourself and your personal projects.
"""

from __future__ import print_function
import sys

# Creates Python 2 and 3 compatible user input
# For more information, see <http://wp.me/P1V5ge-Y6#input/>

# If this is Python 3, use input()
if sys.version_info >= (3, 0):
    get_input = input

# If this is Python 2, use raw_input()
elif sys.version_info <= (2, 7):
    get_input = raw_input


def hours_calc(inputhoursstart, inputhoursend):
    """
    The bulk of the processing takes place in this main function,
    esponsible for taking two input strings and outputting time worked in hours
    """

    # If we don't find a colon in the input string, it's not a valid input
    # and we return an error
    if parsetime(inputhoursstart) == -1 or parsetime(inputhoursend) == -1:
        return "Error! Please make sure input is in <hour>:<minutes> form and try again!"

    # Otherwise, we get the start time in minutes, and the end time in minutes
    minstart = parsetime(inputhoursstart)
    minend = parsetime(inputhoursend)

    # Now, if the end time is less than the start time, we need to add
    # 720 minutes (12 hours) to compensate
    if(minend < minstart):
        minend += 720

    # Take the difference of the minutes to see how long
    # the distance between the two is
    endresult = minend - minstart

    # we now round to the nearest hour
    endresulthours = int(endresult / 60)

    # to get the leftover minutes, we multiply by 60 and subtract
    # the original value. We then take the absolute value of this.
    leftover = abs((endresulthours * 60) - endresult)

    # return a string telling how long we worked
    return '''\nYou worked:
{0}:{1}
({0} hours and {1} minutes)'''.format(endresulthours, leftover)


def parsetime(inputstring):
    """Returns the time as a minutes value"""
    # If there's no colon, return a value of -1
    if(inputstring.find(":") == -1):
        return -1
    # Get the beginning number
    firstpart = int(inputstring[:inputstring.find(":")])
    # Get the end number
    secondpart = int(inputstring[(inputstring.find(":") + 1):])
    # Multiply the hours by 60 to turn them into minutes
    firstpart *= 60
    # Add both these values together
    endresult = firstpart + secondpart
    # Return the added values
    return endresult


def input_new_hours():
    """This is the user-end of things for putting in new hours."""
    print("Input hours below:\n")
    # Get both string input values
    inputstart = get_input("When did you start working? (H:M)\n\n\n")
    inputend = get_input("When did you end working? (H:M)\n\n")
    # Print the results of the calculation
    print(hours_calc(inputstart, inputend))

# A border to make things look nice
border = "_______________________________________________________________"
print ('''{0}
Time Sheet Input Calculator. Copyright 2013 Stopsecret Design.
If you enjoyed, please leave a comment on my website.
http://stopsecretdesign.wordpress.com
{0}\n\n'''.format(border))

# Run the intial solve from the start
input_new_hours()

# Go into this loop if the user wants to calculate more than one time slot
while True:
    new = get_input("\nDo you want to add another time?\n")
    # If the user does, redo the calculation
    if (
        new.lower() == "yes" or
        new.lower() == "yeah" or
        new.lower() == "sure" or
        new.lower() == "y"
    ):
        input_new_hours()
    # If not, then break
    else:
        break

# Display a logout message at the end
print ("{0}\nThanks for using!\n{0}\n\n".format(border))
sys.exit(0)
