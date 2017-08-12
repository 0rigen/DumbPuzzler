#!/usr/bin/env python3
""" Provides a number of crypto checks to try and quickly decipher simple crypto

Takes a string of ciphertext and a chunk size, then attempts to decipher
each chunk according to a series of known cipher methods.  All outputs
are displayed to the console.

This is basically encoding 101 - nothing tricky and nothing multi-step.

If you're past the first stage of a puzzle, this probably won't help you,
    at least not in a single run.
"""

__author__ = "0rigen"
__email__ = "0rigen@0rigen.net"
__web__ = "0rigen.net"
__license__ = "GPL"
__version__ = 3.0

import os
import sys

print('\n\033[95m' + 'DumbPuzzler v1.0' + '\033[0m')
print('\033[92m' + 'by: @_0rigen' + '\033[0m')
print('\nSelect an option to continue')

#######################
# Menu for operations #
#######################
class Menu:
    def showmenu(self):
        print("(" + '\033[1m\033[95m' + "S" + '\033[0m' + ")imple Encoding Checks")
        print("(" + '\033[1m\033[95m' + "P" + '\033[0m' + ")unch 1o57 in the face")
        print("(" + '\033[1m\033[95m' + "Q" + '\033[0m' + ")uit DumbPuzzler")


#######################
# Solver #
#######################
class Solver:
    def simple(self):
        try:
            exec (compile(open("SimpleEncodingChecks.py").read(), "SimpleEncodingChecks.py", 'exec'))
        except KeyboardInterrupt:
            print('Interrupted - See ya later!')
            try:
                sys.exit(0)
            except SystemExit:
                os._exit(0)

#######################
# Chooser - for menu  #
#######################
class Chooser:
    def getchoice(self):
        choice = input(">>> ")
        if choice in ('S', 's'):
            print('You chose Simple.')
            s.simple()
        if choice in ('P', 'p'):
            print('You punched 1057!  That was bad, and you should feel bad!\n')
        if choice in ('Q', 'q'):
            print('Good luck!')
            sys.exit(0)

# create instances of classes
m = Menu()
s = Solver()
c = Chooser()

# loop through main menu until the user chooses to quit
while True:
    m.showmenu()
    c.getchoice()