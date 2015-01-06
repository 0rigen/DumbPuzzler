__author__ = 'Origen'
__project__ = 'Pandora'

import sys, os

print """\
 __             __   __   __
|__)  /\  |\ | |  \ /  \ |__)  /\\
|    /~~\ | \| |__/ \__/ |  \ /~~\\
"""
print "Let's get funky\n\n"

class Menu:
 def Showmenu(self):
  print "(S)imple Crypto Checks"
  print "(A)dvanced Operations"
  print "(P)unch 1o57 in the face"
  print "(Q)uit Pandora"

 def Simple(self):
  execfile("SimpleCryptoChecks.py")

 def getChoice(self):
  choice = raw_input(">>> ")
  if choice in ('S','s'):
   print 'You chose Simple.'
   m.Simple()
  if choice in ('A','a'):
   print 'You chose Advanced'
  if choice in ('P','p'):
   print 'You punched 1057!  I hope you feel a little better now...'
  if choice in ('Q','q'):
   print 'Good luck!'
   sys.exit(0)

#instantitate menu class
m = Menu()

#loop through main menu until the user chooses to quit
while True:
 m.Showmenu()
 m.getChoice()