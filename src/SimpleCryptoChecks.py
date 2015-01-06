__author__ = 'Origen'
__project__ = 'Pandora'

import sys
import binascii
import string

# NOTES-----------------
# ord('a') returns ascii value of character a
# chr(97) returns character of given ascii value
# binascii allows me to convert between binary and ascii

#This module takes a dumb brute-force approach to tackling the more common and simple
#cryptos that we come across.  It takes the inputted string and tries every possible conversion
#that is programmed in.

## A few of these are not fully functional yet and need worked on!!

#Resources
rot13 = string.maketrans(
    "ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz",
    "NOPQRSTUVWXYZnopqrstuvwxyzABCDEFGHIJKLMabcdefghijklm")
rot23 = string.maketrans(
    "ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz",
    "XYZABCDEFGHIJxyzabcdefghijKLMNOPQRSTUVWklmnopqrstuvw")

class bcolors:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   ENDC = '\033[0m'

input = raw_input(bcolors.CYAN + 'Unidentified Data --> ' + bcolors.ENDC)
print('\n\n\n'+bcolors.CYAN + "Original Input: " + bcolors.BOLD + input + bcolors.ENDC)

print '\n'+bcolors.BOLD+bcolors.GREEN+'Transformed into ASCII Values: '+bcolors.ENDC
try:
	for ch in input:
		print ord(ch),
except:
	pass
	print bcolors.PURPLE + "Transforming into ASCII values failed." + bcolors.ENDC

print '\n'+bcolors.BOLD+bcolors.GREEN+'Transformed into text Values: '+bcolors.ENDC
try:
	for num in input:
		#NOT WORKING!!!
		print chr(int(num))
except:
	pass
	print bcolors.PURPLE + "Transforming into text failed." + bcolors.ENDC

print '\n'+bcolors.BOLD+bcolors.GREEN+'Transformed into binary Values: '+bcolors.ENDC
try:
	for item in input:
		print bin(int(binascii.hexlify(item), 16)), + '\n'
except:
	pass
	print bcolors.PURPLE + "Transforming into binary failed." + bcolors.ENDC

print '\n'+bcolors.BOLD+bcolors.GREEN+'Transformed into hex Values:UNFINISHED*** '+bcolors.ENDC
try:
        for item in input:
		n = int(item, 2)
                print binascii.unhexlify('%x' % n)
except:
        pass
        print bcolors.PURPLE + "Transforming into hex failed." + bcolors.ENDC

print '\n'+bcolors.BOLD+bcolors.GREEN+'ROT13: '+bcolors.ENDC
try:
	print string.translate(input, rot13)
except:
	pass
	print bcolors.PURPLE + "ROT13 failed." + bcolors.ENDC

print '\n'+bcolors.BOLD+bcolors.GREEN+'ROT23: '+bcolors.ENDC
try:
        print string.translate(input, rot23)
except:
        pass
        print bcolors.PURPLE + "ROT23 failed." + bcolors.ENDC

print '\n'+bcolors.BOLD+bcolors.GREEN+'Transformed hex to base10 as singles: '+bcolors.ENDC
try:
	for hex in input:
		print int(hex, 16),
except:
	pass
	print bcolors.PURPLE + "Single hex to base10 failed." + bcolors.ENDC

print '\n'+bcolors.BOLD+bcolors.GREEN+'Transformed hex to base10 as pairs: '+bcolors.ENDC
try:
	# NOT FINISHED
			print int(ch,16)

except:
	pass
	print bcolors.PURPLE + "Pair-wise hex to base10 failed." + bcolors.ENDC


