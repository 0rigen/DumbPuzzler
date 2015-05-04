__author__ = '0rigen, 0rigen.net'

import sys
import string
import binascii

# This module takes a dumb brute-force approach to tackling the more common and simple
# crypto types that we come across.  It takes the inputted string and tries every possible conversion
# that is programmed in.

###############
# Resources   #
###############

# Rot13 translate key
global rot13
rot13 = string.maketrans(
    "ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz",
    "NOPQRSTUVWXYZnopqrstuvwxyzABCDEFGHIJKLMabcdefghijklm")

# Rot23 translate key
global rot23
rot23 = string.maketrans(
    "ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz",
    "XYZABCDEFGHIJxyzabcdefghijKLMNOPQRSTUVWklmnopqrstuvw")

# global var to hold the cipher in
global crypto_in

#############################
# bcolors for coloring text #
#############################
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

# 'Chunk' means how long each segment is.  If the data string is 235246, a chunk length of 2
# means that it will be analyzed as 23 52 46.
crypto_in = raw_input(bcolors.CYAN + 'Your new data to analyze --> ' + bcolors.ENDC)  # string of crypto
input_length = raw_input(
    bcolors.CYAN + '\nLength of Data Chunks (1 for text/ROTs/etc) --> ' + bcolors.ENDC)  # length of chunks
print(
    '\n\n' + bcolors.CYAN + "Original Input (chunk length " + input_length + "): " + bcolors.BOLD + crypto_in + bcolors.ENDC)

# Process the input string
try:
    inarray = list(crypto_in)  # turn the input into an array of elements

        # i = 0  #inarray pointer
        #for elem in inarray:
        #### This currently only works for chunk size 1 or 2.  Need to add support for >=3 chunk size #####
        #if i % 2 != 0:  #Odd indices...THIS BREAKS IF A MULTIPLE OF 2 THAT IS > 2
        #    inarray[i - 1] = str(inarray[i - 1] + elem)  #bring to previous (even) location and store there
        #    inarray[i] = "!REM!"  #Placeholder value to be removed
        #    i = i + 1  #inc i
        #else:
        #    i = i + 1  #inc i
        #    continue  #let's keep going!

except ValueError:
    print "Failed to parse your input string - shutting down"
    sys.exit(0)

    # inarray = [x for x in inarray if x != '!REM!']  # Remove all of the now-empty places in the array

print inarray
print 'Input is ' + str(len(crypto_in)) + ' elements long'

# Check for ASCII Converion
print '\n' + 'Transformed into ASCII Values: '
try:
    for thing in inarray:
        if ord(thing) > 176:
            print 'Not ASCII',
        else:
            print ord(thing),
except:
    pass
    print "Transforming into ASCII values failed."

# Check for Text Transformation
# the ASCII range of printable chars is 040-176, so I will need to scan the input string
# for combinations of 2-3 digits that match an ASCII code.
print '\n\n' + 'Transformed into text Values: '
try:
    print 'text values go here...if I finish coding this portion'
except:
    pass
    print "Transforming into text failed."

# Convert ino Binary
print '\nTransformed into binary Values: '
try:
    # This transform fails if it encounters a 'b' in the input.  Need to handle that.
    for item in crypto_in:
        if item != 'b':
            print 'failing on ' + item
            print bin(int(binascii.hexlify(item), 16)), + '\n'
        elif item == 'b':
            print '0b01100010'
except:
    pass
    print "Transforming into binary failed."

# Convert FROM Binary to Integer (INCOMPLETE)
import binascii

print '\nTransforming binary to Integers: '
try:
    for item in crypto_in:
        if item != 'b':
            print bin(int(binascii.hexlify(item), 16)), + '\n'
        elif item == 'b':
            continue
except:
    pass
    print "Transforming into binary failed."

# Convert into Hex Values (Requires chunked processing, which is incomplete)
print '\nTransformed into hex Values:UNFINISHED*** '
try:
    for item in crypto_in:
        n = int(item, 2)
        print binascii.unhexlify('%x' % n)
except:
    pass
    print "Transforming into hex failed."

# ROT13
print '\n' + 'ROT13: '
try:
    print string.translate(crypto_in, rot13)
except:
    pass
    print "ROT13 failed."

# ROT23
print '\nROT23: '
try:
    print string.translate(crypto_in, rot23)
except:
    pass
    print "ROT23 failed."

# Convert from Hex to Base10
print '\n' + 'Transformed hex to base10 as singles: '
try:
    for h in crypto_in:
        print int(h, 16),
except:
    pass
    print '\n' + "Single hex to base10 failed."