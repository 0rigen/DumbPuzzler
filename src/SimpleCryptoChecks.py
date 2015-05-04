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

#######################
# Get input from user #
#######################

crypto_in = raw_input(bcolors.CYAN + 'Your new data to analyze --> ' + bcolors.ENDC)  # string of crypto
input_length = raw_input(
    bcolors.CYAN + '\nLength of Data Chunks (1 for text/ROTs/etc) --> ' + bcolors.ENDC)  # length of chunks
print(
    '\n\n' + bcolors.CYAN + "Original Input (chunk length " + input_length + "): " + bcolors.BOLD + crypto_in + bcolors.ENDC)

# Convert inputted chunk size to an integer
try:
    chunk_size = int(input_length)
except ValueError:
    print 'Chunk size must be an Integer!'

######################
# Chunk up the input #
######################
try:
    inarray = list(crypto_in)  # turn the input into an array of elements

    # Break the array up into chunks of size input_length
    lol = lambda lst, sz: [lst[i:i+sz] for i in range(0, len(lst), sz)]
    chunked_array = lol(inarray, chunk_size)

    # create strings out of the chunks
    i = 0
    while i < chunked_array.__len__():
        chunked_array[i] = ''.join(chunked_array[i])
        i += 1
    print 'Your chunked data: %s ' % chunked_array

except ValueError:
    print "Failed to parse your input string - shutting down"
    sys.exit(0)

print 'Input is ' + str(len(crypto_in)) + ' elements long, divided into %d chunks' % chunked_array.__len__()

#######################
# Start Crypto Checks #
#######################

# Check for ASCII Converion
print '\n' + 'Transformed into ASCII Values: '
try:
    for thing in chunked_array:
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
    for item in chunked_array:
        if item != 'b':
            print 'failing on ' + item
            print bin(int(binascii.hexlify(item), 16)), + '\n'
        elif item == 'b':
            print '0b01100010'
except:
    pass
    print "Transforming into binary failed."

# Convert FROM Binary to Integer (INCOMPLETE)
print '\nTransforming binary to Integers: '
try:
    for item in chunked_array:
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
    for item in chunked_array:
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
    for h in chunked_array:
        print int(h, 16),
except:
    pass
    print '\n' + "Single hex to base10 failed."