import pyfiglet
from responses import target
from sqlalchemy import true
import hashIder, hostScan, portScanner, dummy
from threading import *

banner = pyfiglet.figlet_format("Python Automation Scripts")
print(banner)

opers = """
[0] List running processes
[1] Scan for live hosts on a network
[2] Scan for open ports on a target host
[3] Identify hash type
"""

works = []

def choice(op1):
    switcher = {
        0: dummy,
        1: hostScan,
        2: portScanner,
        3: hashIder
    }

    pkg = switcher.get(op1, dummy)
    if(pkg!=dummy):
        file_name = pkg.fun()
        td = Thread(target=pkg.back(file_name), name = pkg.operation)
        td.start(); td.join()
        works.append(td)
    else:
        dummy.fun(works)



while true:
    try:
        print(opers)
        op1 = int(input("Enter option to proceed...:"))
        choice(op1)
    except KeyboardInterrupt:
        print("\nGood Bye")
        exit()