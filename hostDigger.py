import requests, whois, socket, json
from datetime import datetime as dt

targetDomain = ''

outFile = ''

operation = ''

dnsQueryApi = 'https://api.hackertarget.com/dnslookup/'

reverseIpApi = 'https://api.hackertarget.com/reverseiplookup/'

def launchAttack():
	fd = open(outFile, 'w')


	# getting ip address info for the domain
	try:
		domainIp = socket.gethostbyname(targetDomain)
	except Exception as e:
		fd.write(F'[!!!] Exception occurred: {e}\n')

	fd.write(F'Domain digging summary for domain: {targetDomain}\n')


     # looks for whois information
	domObj = whois.query(targetDomain)
	fd.write(F'\n---------------Whois look up results for the domain---------------\n')
	for key in domObj.__dict__.keys():
		fd.write(F'{key} : {domObj.__dict__[key]}\n')


	# getting information about the ip address
	ipLookupRes = requests.get(F'https://ipinfo.io/{domainIp}/json')
	ipDataJson = json.loads(ipLookupRes.text)

	fd.write('\n---------------IP Address look up results for the domain---------------\n')
	fd.write(F'IP address:  {ipDataJson["ip"]}\n')
	fd.write(F'Hostname: {ipDataJson["hostname"]}\n')
	fd.write(F'Organization: {ipDataJson["org"]}\n')
	fd.write(F'City: {ipDataJson["city"]}\n')
	fd.write(F'Region: {ipDataJson["region"]}\n')
	fd.write(F'Country: {ipDataJson["country"]}\n')
	fd.write(F'Postal code: {ipDataJson["postal"]}\n')
	fd.write(F'Coordinates: {ipDataJson["loc"]}\n')
	fd.write(F'Timezone: {ipDataJson["timezone"]}\n')


	# performing dns record lookup on the host name
	dnsQuery = {"q":targetDomain}
	lookupRes = requests.get(dnsQueryApi,params=dnsQuery)
	recordList = lookupRes.text.split('\n')
	fd.write('\n---------------DNS record look up results for the domain---------------\n')
	for record in recordList:
		fd.write(F'{record}\n')

	
	# performing reverse ip look up
	fd.write('\n---------------Reverse IP look up result for the domain--------------\n')
	revIpQuery = {"q":domainIp}
	reverseIpRes = requests.get(reverseIpApi,params=revIpQuery)
	fd.write(F'{reverseIpRes.text}\n')



def setStage():
	global targetDomain, outFile, operation
	targetDomain = input('Enter the target domain to be looked up: ')
	name = dt.isoformat(dt.now())
	outFile = F'outputs/DomainDigger/{name}.txt'
	print(F'Output will be written to file:\n\t{outFile}')


