import requests, queue, os
# import urllib.parse, urllib.request, urllib.error
from datetime import datetime as dt
from globals import colors

targetUrl = ''
direWordlist = '/home/sam/Shop/python_automation_scripts/resources/directories_mini.txt'
pageWordlist = '/home/sam/Shop/python_automation_scripts/resources/pages_mini.txt'
subdWordlist = '/home/sam/Shop/python_automation_scripts/resources/'
userAgent = 'Mozilla/5.0 (X11; Linux x86_64; rv:19.0) Gecko/20100101 Firefox/19.0'
operation = ''

ext = ['.php', '.txt', '.bak', '.js', '.html', '.log']

direQueue = queue.Queue()
pageQueue = queue.Queue()
subdQueue = queue.Queue()
outFile = ''

def makeDictionary(attackType):
	if attackType==1:
		fd = open(direWordlist, 'r')
		rawWords = fd.readlines()
		fd.close()

		for line in rawWords:
			direQueue.put(line.rstrip())
	
	elif attackType==2:
		fd = open(pageWordlist, 'r')
		rawWords = fd.readlines()
		fd.close()

		for line in rawWords:
			pageQueue.put(line.rstrip())

	elif attackType==3:
		fd = open(subdWordlist, 'r')
		rawWords = fd.readlines()
		fd.close()

		for line in rawWords:
			subdQueue.put(line.rstrip())
	
	else:
		makeDictionary(1)
		makeDictionary(2)
		makeDictionary(3)


# def launchAttack(extensions=None):
# 	fd = open(outFile, 'w')

# 	while not wordQueue.empty():
# 		attempt = wordQueue.get()
# 		attempt_list = []
# 		if "." not in str(attempt):
# 			attempt_list.append('/{}/'.format(attempt))
# 		else:
# 			attempt_list.append('/{}'.format(attempt))

# 		if extensions:
# 			for extension in extensions:
# 				attempt_list.append('/{}{}'.format(attempt, extension))

# 		for brute in attempt_list:
# 			url = "%s%s" % (targetUrl, urllib.parse.quote(brute))

# 			try:
# 				headers = {}
# 				headers["User-Agent"] = userAgent
# 				r = urllib.request.Request(url, headers=headers)

# 				response = urllib.request.urlopen(r)
# 				if len(response.read()):
# 					resp = str(response.code) +" :: "+url+"\n"
# 					fd.write(resp)
# 			except urllib.error.HTTPError as e:
# 				if hasattr(e, 'code') and e.code != 404:
# 					resp = '[!!!]' + ' :: ' +str(e.code) + ' :: ' + url+'\n'
# 					fd.write(resp)


def launchAttack():
	pass


def setStage():
	# global wordQueue
	global wordlist, wordQueue, outFile, operation, targetUrl
	targetUrl = input('Enter target url to fuzz: ')

	print(F'[1] Perform directory fuzzing\n[2] Perform page fuzzing\n[3] Perform subdomain fuzzing\n[4] Perform all of these\n')
	atkChoice = int(input('Your choice: '))

	if atkChoice==1 or atkChoice==4:
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
		
	if atkChoice==2 or atkChoice==4:
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

	if atkChoice==3 or atkChoice==4:
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
	print(F'[!] Results will be written to file:\n\t{colors["CBOLD"]}{colors["CURL"]}{outFile}')
	
	operation = 'directory fuzzing for host '+targetUrl

