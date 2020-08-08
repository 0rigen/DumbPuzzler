#!/usr/bin/env python3
""" Performs checks for the 'simple' encode

This module is called when the user wants to perform (S)imple
checks.  The module will run through a series of encode
and all output (valid or otherwise) is displayed in the console.
"""
__author__ = "0rigen"
__email__ = "0rigen@0rigen.net"
__web__ = "0rigen.net"
__license__ = "GPL"
__version__ = 3.0

'''
OLD FILE DO NOT USE
REFACTORING THIS OUT
'''

import base64
import binascii
# import string
import sys
import time


###############
# Resources   #
###############


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

crypto_in = input('Your new data to analyze --> ')  # string of crypto

###########################################################################################################
# Ok, the chunk thing can be a little confusing... so take a look at this:
# A chunk is the length of a single value of enciphered/encoded text.
#
# For example: a string of numbers with no separation, "1634534734543", would be chunk size
# '1', since every number, as far as you know, is to be evaluated individually.  The same is true of strings
# of non-organized (!words) letters, "abcddefgh".
#
# If, on the other hand, you have a string of hex, "10 a1 16 3b c3 7d", the chunk size
# would be '2', since the hex codes are each length 2 in the input string.
#
# Binary input is chunk size '8', since 1 = 00000001, 2 = 00000020, and so forth in binary.
#
# Thus, choose a chunk size that represents what you believe to represent how the data is
# to be read as individual units.  Look for some form of separators.
# If all else fails, just use '1' and see what comes out.
##########################################################################################################
input_length = input(
    TextColors.GREEN + '\nLength of Data Chunks (1 for text/ROTs, 2 for hex, etc.) --> ' \
    + TextColors.ENDC)  # length of chunks

# Convert inputted chunk size to an integer
try:
    chunk_size = int(input_length)
    done = True  # I dont remember why this is here ^.^

except ValueError:
    print(TextColors.RED + TextColors.BOLD + '\nChunk size must be an Integer!')
    print(
        TextColors.GREEN + '[-] ' + "I'm just going to assume you meant " + \
        TextColors.BLUE + TextColors.BOLD + "'1'\n" + TextColors.ENDC)
    chunk_size = 1
    time.sleep(2)

# Strip out all spaces, they're nasty
crypto_in = crypto_in.replace(" ", "")

######################
# Chunk up the input #
######################
print("""
 -------- Processing Input ---------
""")

try:
    inarray = list(crypto_in)  # turn the input into an array of elements

    # Break the array up into chunks of size input_length
    list_of_chunks = lambda lst, sz: [lst[i:i + sz] for i in range(0, len(lst), sz)]
    chunked_array = list_of_chunks(inarray, chunk_size)

    # create strings out of the chunks
    i = 0
    while i < chunked_array.__len__():
        chunked_array[i] = ''.join(chunked_array[i])
        i += 1
    print(TextColors.GREEN + '[-] ' + TextColors.ENDC + 'chunked data: %s ' % chunked_array \
          + TextColors.ENDC)

except ValueError:
    print(
        TextColors.RED + "[!] " + TextColors.ENDC + "Failed to parse your input string - shutting down" + TextColors.ENDC)
    sys.exit(0)

print(TextColors.GREEN + '[-] ' + TextColors.ENDC + 'Data is ' + str(
    len(crypto_in)) + ' elements long, divided into %d chunks' % \
      chunked_array.__len__() + TextColors.ENDC)
print("""
 -------- Begin Checks ---------
""")

##########################
# Check for a palindrome #
##########################
# Fun pythonic way to do this easily!
if str(crypto_in) == str(crypto_in)[::-1]:
    print(TextColors.GREEN + '[+] ' + "Looks like a palindrome to me" + TextColors.ENDC)
else:
    print(TextColors.RED + '[X] ' + "Not a palindrome" + TextColors.ENDC)

########################
# Alpha --> ASCII Code #
########################
try:
    output = ""

    for thing in chunked_array:
        if ord(thing) > 176:  # #s > 176 are not ASCII
            output += " [Non-ASCII]"
        else:
            output = output + " " + str(ord(thing))

    print(TextColors.GREEN + '\n[-] ' + "Alpha to ASCII Codes: " + TextColors.ENDC)
    print(output)

except:
    pass
    print(TextColors.RED + '\n[X] ' + TextColors.ENDC + "Transforming into ASCII values failed." + TextColors.ENDC)

########################
# ASCII Code --> Alpha #
########################
try:
    fails = 0
    output = ""

    for thing in chunked_array:
        if int(thing) > 176:  # #s greater than 176 are non-ascii
            output += " [Non-Alpha]"
            fails += 1
        else:
            output = output + " " + str(chr(int(thing)))

    print(TextColors.GREEN + '\n[-] ' + "ASCII Codes to Alpha: " + TextColors.ENDC)
    print(output)

except:
    pass
    print(TextColors.RED + '\n[X] ' + TextColors.ENDC + "Transforming into alpha values failed." + TextColors.ENDC)

########################
#  Numbers to Letters  #
########################
try:
    output = ""

    for code in chunked_array:
        ltr = int(code.lstrip('0'))  # strip any leading 0s, they're dumb and unnecessary
        if ltr > 26:
            output += " [Non-Alpha]"
        else:
            output = output + " " + (l2nd[ltr])

    print(TextColors.GREEN + '\n[-] ' + "Numbers to Letters: " + TextColors.ENDC)
    print(output)

except:
    pass
    print(TextColors.RED + '\n[X] ' + TextColors.ENDC + "Transforming #s into text failed." + TextColors.ENDC)

########################
#  Letters to Numbers  #
########################
try:
    output = ""

    for elem in chunked_array:
        value = ord(elem) - 96  # The actual numerical value is ascii ord - 96
        output = output + " " + str(value)

    print(TextColors.GREEN + '\n[-] ' + "Letters to Numbers: " + TextColors.ENDC)
    print(output)

except:
    pass
    print(TextColors.RED + '\n[X] ' + TextColors.ENDC + "Couldn't turn letters into numbers" + TextColors.ENDC)

########################
# CipherTxt --> Binary #
########################
try:
    output = ""

    # This transform fails if it encounters a 'b' in the input.  That is handled as a special case
    for item in chunked_array:
        if item != 'b':
            output = output + " " + str(bin(int(binascii.hexlify(item), 16)))
        elif item == 'b':
            output += ' 0b01100010'

    print(TextColors.GREEN + '\n[-] ' + "To Binary: " + TextColors.ENDC)
    print(output)

except:
    pass
    print(TextColors.RED + '\n[X] ' + TextColors.ENDC + "Transforming into binary failed." + TextColors.ENDC)

########################
#  Binary --> Integer  #
########################
try:
    output = ""

    for item in chunked_array:
        output = output + " " + str(int(item, 2))

    print(TextColors.GREEN + '\n[-] ' + "Binary to Integer: " + TextColors.ENDC)
    print(output)

except:
    print(TextColors.RED + '\n[X] ' + TextColors.ENDC + "Transforming binary to Integer failed." + TextColors.ENDC)

########################
# Binary --> ASCII Ltr #
########################
try:
    output = ""

    for thing in chunked_array:
        n = int(thing, 2)
        output = output + " " + str(binascii.unhexlify('%x' % n))

    print(TextColors.GREEN + '\n[-] ' + "Binary to ASCII Letters: " + TextColors.ENDC)
    print(output)

except:
    pass
    print(TextColors.RED + '\n[X] ' + TextColors.ENDC + "Transforming from binary to text failed." + TextColors.ENDC)

########################
#     Hex --> Text     #
########################
try:
    out = ''.join(chr(int(crypto_in[i:i + 2], 16)) for i in range(0, len(crypto_in), 2))

    print(TextColors.GREEN + '\n[-] ' + "Hex to Text: " + TextColors.ENDC)
    print(out)
except:
    print(TextColors.RED + '\n[X] ' + TextColors.ENDC + "Transforming into hex failed." + TextColors.ENDC)

########################
#        ROT           #
########################
""" This will go ahead and run through every potential rotation, JFF """

message = crypto_in
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

print("\n++++ ROT ++++")

for key in range(len(alphabet)):

    rot_out = ''

    for symbol in message:  # rot each letter in the input ciphertext
        if symbol.capitalize() in alphabet:
            num = alphabet.find(symbol.capitalize())
            num += key

            if num > 25:  # correct wrap-around
                num -= 26

            rot_out += alphabet[num]  # add to output string

        else:
            rot_out = rot_out + symbol

    print('ROT%s: %s' % (key, rot_out))

########################
#        ATBASH        #
########################


########################
#    Hex --> Base10    #
########################
if chunk_size == 2:
    try:
        output = ""
        for h in chunked_array:
            output = output + " " + str(int(h, 16))

        print(TextColors.GREEN + '\n[-] ' + "Hex to Base10: " + TextColors.ENDC)
        print(output)

    except:
        pass
        print('\n' + TextColors.RED + "\n[X] Hex to base10 failed." + TextColors.ENDC)

else:
    print(
        TextColors.RED + '\n[X] ' + TextColors.ENDC + "It can't be hex2b10 since the chunk size isn't 2..." + TextColors.ENDC)

########################
#    Base64 Decoding   #
########################
try:
    encoded = crypto_in
    output = str(base64.b64decode(encoded))  # Well, that was easy
    print(TextColors.GREEN + '\n[-] ' + "Base64 Decoding: " + TextColors.ENDC)
    print(output)

except TypeError:
    pass
    print(TextColors.RED + '\n[X] TypeError Decoding Base64: Non-alphabet characters or improper padding of input' \
                           'string, most likely' + TextColors.ENDC)
except:
    pass
    print(TextColors.RED + '\n[X] ' + TextColors.ENDC + "Base64 failed" + TextColors.ENDC)

########################
# Print final warnings #
########################
print(TextColors.BOLD + TextColors.YELLOW + "\n\nSimple Checks Complete!  Hope you found what you were " \
                                            "looking for!\n" + TextColors.ENDC)
print(TextColors.PURPLE + "Remember, if it's a sequence of numbers, it would be worth searching on" \
                          "http://oeis.org for a named sequence!" + TextColors.ENDC + "\n")
