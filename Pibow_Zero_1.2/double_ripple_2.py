#!/usr/bin/python3
"""
Double Ripple 2 - Pibow Zero 1.2

Retrieves the rainbows and sends them to the ripple function.
With the GPIO pins at the top of the Raspberry Pi, the rainbows ripple
from the top left to the bottom right.

....................

Functions:
- double_ripple_2: Gets 9 rainbows and sends them to the double ripple
      function

....................

Author: Paul Ryan

This program was written on a Raspberry Pi using the Geany IDE.
"""
########################################################################
#                          Import modules                              #
########################################################################

from bfp_unicornphat import print_header
from bfp_unicornphat import stop
from bfp_unicornphat import get_horizontal_rainbow_00
from bfp_unicornphat import get_double_ripple_rainbows_1
from bfp_unicornphat import double_ripple

########################################################################
#                            Functions                                 #
########################################################################


def double_ripple_2():
    """
    Gets 9 rainbows, assigns them in reverse order, and sends them to
    the double ripple function
    """

    rainbow00 = get_horizontal_rainbow_00()

    rainbow08, rainbow07, rainbow06, rainbow05, rainbow04, rainbow03, \
        rainbow02, rainbow01 = get_double_ripple_rainbows_1()

    dr_rainbows_2 = [rainbow01, rainbow02, rainbow03, rainbow04,
                     rainbow05, rainbow06, rainbow07, rainbow08]

    double_ripple(rainbow00, dr_rainbows_2)


if __name__ == '__main__':
    try:
        # STEP01: Print header
        print_header()
        # STEP02: Print instructions in white text
        print("\033[1;37;40mPress Ctrl-C to stop the program.")
        # STEP03:
        double_ripple_2()
        # STEP04: Exit the program.
        stop()
    except KeyboardInterrupt:
        stop()
