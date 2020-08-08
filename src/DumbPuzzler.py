#!/usr/bin/env python3

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
        print("(" + '\033[1m\033[95m' + "S" + '\033[0m' + ")imple Checks (Run all)")
        print("(" + '\033[1m\033[95m' + "M" + '\033[0m' + ")enu of enciphercodements")
        print("(" + '\033[1m\033[95m' + "P" + '\033[0m' + ")unch 1o57 in the face")
        print("(" + '\033[1m\033[95m' + "Q" + '\033[0m' + ")uit DumbPuzzler")


'''
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
'''

#######################
# Chooser - for menu  #
#######################
class Chooser:
    def getchoice(self):
        choice = input(">>> ")
        if choice in ('S', 's'):
            print('You chose Simple.')
            s.simple()
        if choice in ('M', 'm'):
            print('Menu!.')
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