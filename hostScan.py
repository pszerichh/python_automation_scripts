import time
from datetime import datetime as dt
import scapy.all as scapy


netAddr = ''
outFile = ''
operation = 'Network scanning for'

def scanIP(netAddr):

	arpRequest = scapy.ARP(pdst=netAddr)
	broadcast = scapy.Ether(dst='ff:ff:ff:ff:ff:ff')
	arpPacket = broadcast/arpRequest

	responsiveHosts = scapy.srp(arpPacket, timeout=1, verbose=0)[0]
	
	liveHosts = []
	
	for hostConfig in responsiveHosts:
		liveHosts.append(hostConfig[1].psrc)

	return liveHosts

	

def launchAttack():

	liveHosts = scanIP(netAddr)

	fd = open(outFile, 'w')
	for host in liveHosts:
		fd.write(F'[!] {host} is alive\n')

	


def setStage():
	global netAddr, outFile, operation
	netAddr = input('Enter network address in CIDR format (Eg. 192.168.34.25/24): ')

	name = dt.isoformat(dt.now())
	outFile = F'/home/sam/Shop/python_automation_scripts/outputs/HostScanner/{name}.txt'
	print(F'Output will be written to {outFile}')


setStage()
launchAttack()