__author__ = '0rigen, 0rigen.net'

import sys
import string
import binascii

###############
# Resources   #
###############

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

print "Too bad!  I haven't coded the tough stuff yet!"