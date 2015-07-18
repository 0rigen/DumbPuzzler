#!/usr/bin/env/ python
""" Performs checks for the 'simple' ciphers

This module is called when the user wants to perform (S)imple
checks.  The module will run through a series of ciphers
and all output (valid or otherwise) is displayed in the console.
"""
__author__ = "0rigen"
__email__ = "0rigen@0rigen.net"
__web__ = "0rigen.net"
__license__ = "GPL"
__version__ = 3.0

import sys
import string
import binascii
import base64
import time
import encodings

###############
# Resources   #
###############

# Atbash translate key
global atbash
atbash = string.maketrans(
    "ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz",
    "ZYXWVUTSRQPONzyxwvutsrqponMLKJIHGFEDCBAmlkjihgfedcba")

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

# letters 2 numbers dictionary
l2nd = { x+1: chr(ord('a')+x) for x in range(26) }

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
    '\n' + TextColors.GREEN + "Original Input (chunk length " + input_length + "): " + TextColors.BOLD +
                                                    crypto_in + TextColors.ENDC)

# Convert inputted chunk size to an integer
try:
    chunk_size = int(input_length)
    done=true
except ValueError:
    print TextColors.RED + TextColors.BOLD + '\nChunk size must be an Integer!'
    print "I'm just going to assume you meant " + TextColors.BLUE + TextColors.BOLD + "'1'\n" + TextColors.ENDC
    chunk_size = 1
    time.sleep(2)

# Strip out all spaces, they're nasty
crypto_in = crypto_in.replace(" ", "")

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

########################
# Alpha --> ASCII Code #
########################
print '\n' + TextColors.PURPLE + TextColors.BOLD + 'Transformed into ASCII Code Values: ' + TextColors.ENDC
try:
    for thing in chunked_array:
        if ord(thing) > 176:
            print '[Not ASCII]',
        else:
            print ord(thing),
except:
    pass
    print TextColors.RED+"Transforming into ASCII values failed."+TextColors.ENDC

########################
# ASCII Code --> Alpha #
########################
print '\n' + TextColors.PURPLE + TextColors.BOLD + 'Transforming from ASCII codes to text: ' + TextColors.ENDC
try:
    for thing in chunked_array:
        if int(thing) > 176:
            print '[Not ASCII]',
        else:
            print str(unichr(int(thing))),
except:
    pass
    print TextColors.RED+"Transforming into ASCII values failed."+TextColors.ENDC

########################
#  Numbers to Letters  #
########################
print '\n\n' + TextColors.BOLD + TextColors.PURPLE + 'Transforming from numbers to alpha (1-26): ' + TextColors.ENDC
try:
    for code in chunked_array:
        ltr = int(code.lstrip('0'))
        if ltr > 26:
            print TextColors.RED + "[Not a letter]" + TextColors.ENDC,
        else:
            print(l2nd[ltr]),
except:
    pass
    print TextColors.RED+"Transforming into text failed."+TextColors.ENDC

########################
#  Letters to Numbers  #
########################
print '\n\n' + TextColors.BOLD + TextColors.PURPLE + 'Transforming letters into numeric alphabet (a=1, etc): ' + TextColors.ENDC
try:
    for elem in chunked_array:
        value = ord(elem) - 96
        print value,
except:
    pass
    print TextColors.RED+"Couldn't turn letters into numbers"+TextColors.ENDC

########################
# CipherTxt --> Binary #
########################
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
    print TextColors.RED+"Transforming into binary failed."+TextColors.ENDC

########################
#  Binary --> Integer  #
########################
print '\n\n' + TextColors.BOLD + TextColors.PURPLE + 'Transforming from binary into Integers: ' + TextColors.ENDC
try:
    for item in chunked_array:
        print int(item, 2),  # puts the item into integer form, from base 2 :D Python so ez!
except:
    print TextColors.RED+"\nTransforming binary to Integer failed."+TextColors.ENDC

########################
# Binary --> ASCII Ltr #
########################
print '\n\n' + TextColors.PURPLE + TextColors.BOLD + 'Transformed from binary to text ' + TextColors.ENDC
try:
    for thing in chunked_array:
            n = int(thing, 2)
            print binascii.unhexlify('%x' % n),

except:
    pass
    print TextColors.RED+"\nTransforming from binary to text failed."+TextColors.ENDC

########################
#     Hex --> Text     #
########################
print '\n\n' + TextColors.BOLD + TextColors.PURPLE + 'Transformed out of Hex into ASCII (ignoring chunk' \
                                                     ' size, sry not sry):' + TextColors.ENDC
try:
    out = ''.join(chr(int(crypto_in[i:i+2], 16)) for i in range(0, len(crypto_in), 2))
    print out
except:
    print TextColors.RED+"Transforming into hex failed."+TextColors.ENDC

########################
#        ROT13         #
########################
print '\n' + TextColors.BOLD + TextColors.PURPLE + 'ROT13: ' + TextColors.ENDC
try:
    print string.translate(crypto_in, rot13)
except:
    pass
    print TextColors.RED+"ROT13 failed."+TextColors.ENDC

########################
#         ROT23        #
########################
print '\n' + TextColors.BOLD + TextColors.PURPLE + 'ROT23: ' + TextColors.ENDC
try:
    print string.translate(crypto_in, rot23)
except:
    pass
    print TextColors.RED+"ROT23 failed."+TextColors.ENDC

########################
#        ATBASH        #
########################
print '\n' + TextColors.BOLD + TextColors.PURPLE + 'ATBASH ' + TextColors.ENDC
try:
    print string.translate(crypto_in, atbash)
except:
    pass
    print TextColors.RED+"ATBASH failed."+TextColors.ENDC

########################
#    Hex --> Base10    #
########################
print '\n' + TextColors.BOLD + TextColors.PURPLE + 'Transformed hex to base10 as singles: ' + TextColors.ENDC
if chunk_size == 2:
    try:
        for h in chunked_array:
            print int(h, 16),
    except:
        pass
        print '\n' + TextColors.RED+"Single hex to base10 failed"+TextColors.ENDC
else:
    print TextColors.RED+"It can't be hex2b10 since the chunk size isn't 2..."+TextColors.ENDC

########################
#    Base64 Decoding   #
########################
print '\n' + TextColors.BOLD + TextColors.PURPLE + 'Attempting to decode as base64: ' + TextColors.ENDC
try:
    encoded = crypto_in
    print base64.b64decode(encoded)
except TypeError:
    pass
    print TextColors.RED+'TypeError Decoding Base64: Non-alphabet characters or improper padding of input' \
                         'string, most likely'+TextColors.ENDC
except:
    pass
    print '\n' + TextColors.RED+"Base64 failed"+TextColors.ENDC

########################
# Print final warnings #
########################
print TextColors.BOLD + TextColors.YELLOW + "\n\nSimple Checks Complete!  Hope you found what you were " \
                                            "looking for!\n" + TextColors.ENDC
print TextColors.PURPLE + "Remember, if it's a sequence of numbers, it would be worth searching on" \
                          "http://oeis.org for a named sequence!" + TextColors.ENDC + "\n"