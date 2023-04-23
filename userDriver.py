#!/usr/bin/python3
import pyfiglet
from responses import target
from sqlalchemy import true
import hostScan, portScanner, dummyScript, contentDiscovery, codeExitor, credsBruter, webCrawler, hostDigger
from threading import *
from globals import *

print(banner)

opers = F"""{colors['CCYAN']}{colors['CBOLD']}
[0] List running processes
[1] Scan for live hosts on a network
[2] Scan for open ports on a target host
[3] Fuzz for directories/files
[4] Stuff credentials against login page
[5] Perform information look up on a domain name
[6] To exit{colors['CEND']}
"""

works = []

def choice(op1):
    switcher = {
        0: dummyScript,
        1: hostScan,
        2: portScanner,
        3: contentDiscovery,
        4: credsBruter,
        5: webCrawler,
        6: codeExitor
    }

    pkg = switcher.get(op1, None)
    if pkg ==None:
        print("Oops! Invalid option.")
    elif pkg==dummyScript:
        dummyScript.setStage(works)
    elif pkg==codeExitor:
        codeExitor.env_exit(works)
    else:
        pkg.setStage()
        td = Thread(target=pkg.launchAttack, name = pkg.operation, daemon=True)
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