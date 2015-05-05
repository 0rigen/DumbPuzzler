__author__ = '0rigen, 0rigen.net'

import sys

print """\
 _____               _     ______                   _
(____ \             | |   (_____ \                 | |
 _   \ \ _   _ ____ | | _  _____) )   _ _____ _____| | ____  ____
| |   | | | | |    \| || \|  ____/ | | (___  |___  ) |/ _  )/ ___)
| |__/ /| |_| | | | | |_) ) |    | |_| |/ __/ / __/| ( (/ /| |
|_____/  \____|_|_|_|____/|_|     \____(_____|_____)_|\____)_|
"""


#######################
# Menu for operations #
#######################
class Menu:
    def showmenu(self):
        print "(S)imple Crypto Checks"
        print "(A)dvanced Operations"
        print "(P)unch 1o57 in the face"
        print "(Q)uit DumbPuzzler"


#######################
# Solver #
#######################
class Solver:
    def simple(self):
        execfile("SimpleCryptoChecks.py")

    def advanced(self):
        execfile("AdvCryptoChecks.py")


#######################
# Chooser - for menu  #
#######################
class Chooser:
    def getchoice(self):
        choice = raw_input(">>> ")
        if choice in ('S', 's'):
            print 'You chose Simple.'
            s.simple()
        if choice in ('A', 'a'):
            print 'You chose Advanced'
            s.advanced()
        if choice in ('P', 'p'):
            print 'You punched 1057!  I hope you feel a little better now...\n'
        if choice in ('Q', 'q'):
            print 'Good luck!'
            sys.exit(0)

# create instances of classes
m = Menu()
s = Solver()
c = Chooser()

# loop through main menu until the user chooses to quit
while True:
    m.showmenu()
    c.getchoice()