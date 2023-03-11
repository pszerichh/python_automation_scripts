import os, platform
from datetime import datetime as dt

from sympy import ln

# net = input("enter network address: ")

operation = "Host Scanning"

net1 = []
net2 = ""
rng = []
oSystem = platform.system()
file_name = ""

def back():
    filw = open(file_name, 'w')
    filw.write("ping sweep result for network"+net2+"*")
    oper = platform.system()
    if oper == "Windows":
        pinc = "ping -n 1 "
    else:
        pinc = "ping -c 1 "

    for ip in range(rng[0], rng[1]):
        addr = net2 + str(ip)
        com = pinc + addr
        res = os.popen(com)
        for line in res.readlines():
            if(line.count("TTL")):
                break;
            if(line.count("TTL")):
                filw.write(addr+" ---> live")


def fun():
    net = input("Enter network address: ")
    net1 = net.split('.')
    global net2
    net2 = net1[0] + '.' + net1[1] + '.' + net[2] + '.'
    st = int(input("Enter first number for last octet: "))
    en = int(input("Enter last number for last octet: "))
    en +=1
    rng.append(st); rng.append(en)
    name = dt.isoformat(dt.now())
    global file_name
    file_name = "outputs/HostPing/"+name+".txt"
    print("Results will be written to file: ",file_name)