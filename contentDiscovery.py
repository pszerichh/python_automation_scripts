import requests, queue, os
# import urllib.parse, urllib.request, urllib.error
from datetime import datetime as dt
from globals import colors

targetHost = ''
direWordlist = '/home/sam/Shop/python_automation_scripts/resources/directories_mini.txt'
pageWordlist = '/home/sam/Shop/python_automation_scripts/resources/directories_mini.txt'
subdWordlist = '/home/sam/Shop/python_automation_scripts/resources/subdomains_mini.txt'
# userAgent = 'Mozilla/5.0 (X11; Linux x86_64; rv:19.0) Gecko/20100101 Firefox/19.0'
operation = ''

extensions = [
	'.asp', '.aspx', '.bak', '.bat', '.css', '.com', '.config',
	'.dat', '.dll', '.exe', 'html', '.js', '.log', '.pcap', '.php', '.phps',
	'.phtml', '.properties', '.rsa', '.sh', '.sql', '.tar', '.txt', '.xml', '.zip'
]

statusCodes = [200, 204, 301, 302, 307, 401, 403, 405, 500]

direQueue = queue.Queue()
pageQueue = queue.Queue()
subdQueue = queue.Queue()
outFile = ''

def makeDictionary(attackType):
	if attackType in [1,4,5,7]:
		fd = open(direWordlist, 'r')
		rawWords = fd.readlines()
		fd.close()

		for line in rawWords:
			direQueue.put(line.rstrip())
	
	if attackType in [2,4,6,7]:
		fd = open(pageWordlist, 'r')
		rawWords = fd.readlines()
		fd.close()

		for line in rawWords:
			for ext in extensions:
				pageQueue.put(line.rstrip()+ext)

	if attackType in [3,5,6,7]:
		fd = open(subdWordlist, 'r')
		rawWords = fd.readlines()
		fd.close()

		for line in rawWords:
			subdQueue.put(line.rstrip())
	

def launchAttack():
	global targetHost
	fd = open(outFile, 'w')

	if 'http' in targetHost or 'https' in targetHost:
		targetHost = targetHost.split('://')[1]

	# print(targetHost)

	# subdomain fuzzing part
	if not subdQueue.empty():
		fd.write('---------------subdomain fuzzing result---------------\n')
	while not subdQueue.empty():
		pref = subdQueue.get()
		url = F"http://{pref}.{targetHost}"
		# print(url)
		
		res = requests.get(url)
		if res.status_code in statusCodes:
			fd.write(F'[!!!] {res.status_code} : {url}\n')


	targetHost = F"http://{targetHost}"

	# directory fuzzing part
	if not direQueue.empty():
		fd.write('---------------directory fuzzing result---------------\n')
	while not direQueue.empty():
		suff = direQueue.get()
		url = targetHost + F"/{suff}/"
		# print(url)
		
		res = requests.get(url)
		if res.status_code in statusCodes:
			fd.write(F"[!!!] {res.status_code} : {url}\n")

	# page fuzzing part
	if not pageQueue.empty():
		fd.write('---------------page fuzzing result---------------\n')
	while not pageQueue.empty():
		suff = pageQueue.get()
		url = targetHost + F"/{suff}"
		# print(url)
		
		res = requests.get(url)
		if res.status_code in statusCodes:
			fd.write(F"[!!!] {res.status_code} : {url}\n")

	fd.close()



def setStage():
	# global wordQueue
	global direWordlist, pageWordlist, subdWordlist, wordQueue, outFile, operation, targetHost
	targetHost = input('Enter target url to fuzz: ')

	print('Enter the corresponding option for the action you want to perform')
	print('[1] Directory fuzzing\n[2] Page fuzzing\n[3] Subdomain fuzzing')
	print('[4] Directory and Page fuzzing\n[5] Directory and Subdomain fuzzing')
	print('[6] Page and Subdomain fuzzing\n[7] All of the operations\n')
	atkChoice = int(input('Your choice: '))

	if atkChoice in [1,4,5,7]:
		print(F'Current dictionary for directory fuzzing:\n\t{colors["CBOLD"]}{colors["CURL"]}{direWordlist}{colors["CEND"]}')
		ch = input('Change dictionary? (y/N): ')
		if ch=='y' or ch =='Y':
			wordlistBuffer = input('Enter path to dictionary: ')
			if os.path.exists(wordlistBuffer):
				direWordlist = wordlistBuffer
				print(F'{colors["CBLUE"]}[!] Wordlist for directory fuzzing changed{colors["CEND"]}\n')
			else:
				print(F'{colors["CRED"]}[!!!] Supplied file does not exist{colors["CEND"]}')
				print(F'Continuing with\n\t{colors["CBOLD"]}{colors["CEND"]}{direWordlist}{colors["CEND"]}\n')
		
	if atkChoice in [2,4,6,7]:
		print(F'Currrent dictionary for page fuzzing:\n\t{colors["CBOLD"]}{colors["CURL"]}{pageWordlist}{colors["CEND"]}\n')
		ch = input('Change dictionary? (y/N): ')
		if ch=='y' or ch=='Y':
			wordlistBuffer = input('Enter path to dictionary: ')
			if os.path.exists(wordlistBuffer):
				pageWordlist = wordlistBuffer
				print(F'{colors["CBLUE"]}[!] Wordlist for page fuzzign changed{colors["CEND"]}\n')
			else:
				print(F'{colors["CRED"]}[!!!] Supplied file does not exist{colors["CEND"]}')
				print(F'Continuing with\n\t{colors["CBOLD"]}{colors["CURL"]}{pageWordlist}{colors["CEND"]}\n')

	if atkChoice in [3,5,6,7]:
		print(F'Current dictionary for subdomain fuzzing:\n\t{colors["CBOLD"]}{colors["CURL"]}{subdWordlist}{colors["CEND"]}')
		ch = input('Change dictionary? (y/N): ')
		if ch=='y' or ch=='Y':
			wordlistBuffer = input('Enter path to dictionary: ')
			if os.path.exists(wordlistBuffer):
				subdWordlist = wordlistBuffer
				print(F'{colors["CBLUE"]}[!] Wordlist for sub-domain fuzzing changed{colors["CEND"]}\n')
			else:
				print(F'{colors["CRED"]}[!!!] Supplied file does not exist{colors["CEND"]}\n')
				print(F'Continuing with file at\n\t{colors["CBOLD"]}{colors["CURL"]}{subdWordlist}{colors["CEND"]}')
	

	makeDictionary(atkChoice)

	name = dt.isoformat(dt.now())
	outFile = 'outputs/DirFuzzer/'+name+'.txt'
	print(F'[!] Results will be written to file:\n\t{colors["CBOLD"]}{colors["CURL"]}{outFile}{colors["CEND"]}')
	
	operation = 'directory fuzzing for host '+targetHost

