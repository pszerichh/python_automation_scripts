import os, platform, socket
from datetime import datetime as dt

from sympy import ln

# net = input("enter network address: ")

operation = "Host Scanning"

net1 = []
net2 = ""
rng = []
oSystem = platform.system()
outFile = ""

def scanIP(ipaddr):
    sockObj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(1)
    res = sockObj.connect_ex((ipaddr, 135))

    if res==0:
        if     
    

def launchAttack():
    fd = open(outFile, 'w')




# def launchAttack():
#     filw = open(outFile, 'w')
#     filw.write("ping sweep result for network"+net2+"*")
#     oper = platform.system()
#     if oper == "Windows":
#         pinc = "ping -n 1 "
#     else:
#         pinc = "ping -c 1 "

#     for ip in range(rng[0], rng[1]):
#         addr = net2 + str(ip)
#         com = pinc + addr
#         res = os.popen(com)
#         for line in res.readlines():
#                 if(line.count("TTL")):
#                 	break;
#                 if(line.count("TTL")):
#                 	filw.write(addr+" ---> live")


def setStage():
    net = input("Enter network address: ")
    net1 = net.split('.')
    global net2
    net2 = net1[0] + '.' + net1[1] + '.' + net[2] + '.'
    st = int(input("Enter first number for last octet: "))
    en = int(input("Enter last number for last octet: "))
    en +=1
    rng.append(st); rng.append(en)
    name = dt.isoformat(dt.now())
    global outFile
    outFile = "outputs/HostScanner/"+name+".txt"
    print("Results will be written to file: ",outFile)