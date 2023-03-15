import os, platform, socket
from datetime import datetime as dt

net1 = []
net2 = ''
ipRange = []

outFile = ''

def scanIP(ipaddr):
	sockObj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	socket.setdefaulttimeout(1)

	res = sockObj.connect_ex((ipaddr, 135))

	if res==0:
		return True
	else:
		return False
	

def launchAttack():
	fd = open(outFile, 'w')
	fd.write(F'Host discovery result for network: {net2}*\n')

	for ip in range(ipRange[0], ipRange[1]):
		ipaddr = net2 + str(ip)
		if(scanIP(ipaddr)):
			fd.write(F'{ipaddr} is alive')


def setStage():
	net = input('Enter network address: ')
	net1 = net.split('.')
	net2 = F'{net1[0]}.{net1[1]}.{net1[2]}.'
	octetSt = int(input('ENter first number of last octet: '))
	octetEn = int(input('Enter last number of last octet: '))
	en +=1
	ipRange.append(octetSt); ipRange.append(octetEn)

	name = dt.isoformat(dt.now())
	outFile = F'/home/sam/Shop/python_automation_scripts/outputs/HostScanner/{name}.txt'
	print(F'Output will be written to {outFile}')