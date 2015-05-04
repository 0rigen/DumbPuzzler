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

print "Too bad!  I haven't coded the tough stuff yet!"