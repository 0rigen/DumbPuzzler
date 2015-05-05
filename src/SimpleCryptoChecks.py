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
class TextColors:
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

crypto_in = raw_input(TextColors.GREEN + 'Your new data to analyze --> ' + TextColors.ENDC)  # string of crypto
input_length = raw_input(
    TextColors.GREEN + '\nLength of Data Chunks (1 for text/ROTs/etc) --> ' + TextColors.ENDC)  # length of chunks
print(
    '\n\n' + TextColors.GREEN + "Original Input (chunk length " + input_length + "): " + TextColors.BOLD + crypto_in + TextColors.ENDC)

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
    list_of_chunks = lambda lst, sz: [lst[i:i+sz] for i in range(0, len(lst), sz)]
    chunked_array = list_of_chunks(inarray, chunk_size)

    # create strings out of the chunks
    i = 0
    while i < chunked_array.__len__():
        chunked_array[i] = ''.join(chunked_array[i])
        i += 1
    print TextColors.GREEN + 'Your chunked data: %s ' % chunked_array + TextColors.ENDC

except ValueError:
    print TextColors.RED + "Failed to parse your input string - shutting down" + TextColors.ENDC
    sys.exit(0)

print TextColors.GREEN + 'Input is ' + str(len(crypto_in)) + ' elements long, divided into %d chunks' % \
                                                             chunked_array.__len__() + TextColors.ENDC

#######################
# Start Crypto Checks #
#######################

# Check for ASCII Code Conversion
print '\n' + TextColors.PURPLE + TextColors.BOLD + 'Transformed into ASCII Code Values: ' + TextColors.ENDC
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
print '\n\n' + TextColors.BOLD + TextColors.PURPLE + 'Transformed into text Values: ' + TextColors.ENDC
if chunk_size > 1:
    try:
        for code in chunked_array:
            dig = int(code)
            print chr(dig),
    except:
        pass
        print "Transforming into text failed."
else:
    print "It can't be ASCII code at that chunk size!"

# Convert into Binary
print '\n\n' + TextColors.BOLD + TextColors.PURPLE + 'Transformed into binary Values: ' + TextColors.ENDC
try:
    # This transform fails if it encounters a 'b' in the input.  That is handled as a special case
    for item in chunked_array:
        if item != 'b':
            print bin(int(binascii.hexlify(item), 16)),
        elif item == 'b':
            print '0b01100010'
except:
    pass
    print "Transforming into binary failed."

# Convert FROM Binary to Integer (INCOMPLETE)
print '\n\n' + TextColors.BOLD + TextColors.PURPLE + 'Transforming binary to Integers: ' + TextColors.ENDC
try:
    for item in chunked_array:
        print int(item, 2),  # puts the item into integer form, from base 2 :D Python so ez!
except:
    pass
    print "Transforming binary to Integer failed."

# Convert into Hex Values
print '\n\n' + TextColors.BOLD + TextColors.PURPLE + 'Transformed into hex Values:UNFINISHED*** ' + TextColors.ENDC
if chunk_size == 2:
    try:
        for item in chunked_array:
            n = int(item, 2)
            print binascii.unhexlify('%x' % n)
    except:
        pass
        print "Transforming into hex failed."
else:
    print "Can't be hex values unless chunk size is 2..."

# ROT13
print '\n' + TextColors.BOLD + TextColors.PURPLE + 'ROT13: ' + TextColors.ENDC
try:
    print string.translate(crypto_in, rot13)
except:
    pass
    print "ROT13 failed."

# ROT23
print '\n' + TextColors.BOLD + TextColors.PURPLE + 'ROT23: ' + TextColors.ENDC
try:
    print string.translate(crypto_in, rot23)
except:
    pass
    print "ROT23 failed."

# Convert from Hex to Base10
print '\n' + TextColors.BOLD + TextColors.PURPLE + 'Transformed hex to base10 as singles: ' + TextColors.ENDC
if chunk_size == 2:
    try:
        for h in chunked_array:
            print int(h, 16),
    except:
        pass
        print '\n' + "Single hex to base10 failed."
else:
    print "It can't be hex2b10 since the chunk size isn't 2..."

print TextColors.BOLD + TextColors.YELLOW + "\n\nI'm done!  Hope you found what you were looking for!\n" + TextColors.ENDC