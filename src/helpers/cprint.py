import sys
import os

cwd = os.getcwd()
sys.path.append(cwd.rsplit('\\', 1))  # This should append the path just above cwd


class cprint():
    def __call__(self, string, code):
        '''
          Code => 1 SUCCESS, 2 WARN, 3 FAIL
        '''

        rets = "cprint() Failed."

        if code == 1:
            rets = f"[+] {string}"
        elif code == 2:
            rets = f"[-] {string}"
        elif code == 3:
            rets = f"[!] {string}"

        return rets


sys.modules[__name__] = cprint(string, code)
