#!/usr/bin/python3
import pyfiglet
from responses import target
from sqlalchemy import true
import hostScan, portScanner, dummyScript, dirFuzzer, codeExitor
from threading import *

banner = pyfiglet.figlet_format("Python Automation Scripts")
print(banner)

opers = """
[0] List running processes
[1] Scan for live hosts on a network
[2] Scan for open ports on a target host
[3] Fuzz for directories/subdomains
[4] To exit
"""

works = []

def choice(op1):
    switcher = {
        0: dummyScript,
        1: hostScan,
        2: portScanner,
        3: dirFuzzer,
        4: codeExitor
    }

    pkg = switcher.get(op1, None)
    if pkg ==None:
        print("Oops! Invalid option.")
    elif pkg==dummyScript:
        dummyScript.fun(works)
    elif pkg==codeExitor:
        codeExitor.env_exit(works)
    else:
        pkg.fun()
        td = Thread(target=pkg.back, name = pkg.operation, daemon=True)
        td.daemon = True
        td.start()
        works.append(td)




while true:
    try:
        print(opers)
        op1 = int(input("Enter option to proceed...:"))
        choice(op1)
    except KeyboardInterrupt:
        print("\nGood Bye")
        exit()