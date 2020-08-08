import sys
import os

cwd = os.getcwd()
sys.path.append(cwd.rsplit('\\', 1))  # This should append the path just above cwd
from helpers import colors, \
    cprint


class atbash:
    '''
      Simple substitution cipher.  Key is constant; always a backwards alphabet.
    '''

    def __call__(self):
        key = str.maketrans(
            "ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz",
            "ZYXWVUTSRQPONzyxwvutsrqponMLKJIHGFEDCBAmlkjihgfedcba")

        try:
            output = str(string.translate(crypto_in, key))
            print('\n[-] ' + "ATBASH: ")
            print(output)
        except:
            pass
            print('\n[X] ' + "ATBASH failed.")


sys.modules[__name__] = atbash()
