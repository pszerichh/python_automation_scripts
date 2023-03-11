import urllib, queue, os
import urllib.parse, urllib.request, urllib.error
from datetime import datetime as dt

targetUrl = ""
wordlist = "sample_list.txt"
resume = None
userAgent = "Mozilla/5.0 (X11; Linux x86_64; rv:19.0) Gecko/20100101 Firefox/19.0"
operation=""

ext = [".php", ".txt", ".bak", ".js", ".html"]

wordQueue = queue.Queue()
outFile = ''

def makeDictionary():
	fd = open(wordlist, "r")
	rawWords = fd.readlines()
	fd.close()

	for line in rawWords:
		wordQueue.put(line.rstrip())

	# found_res = False
	# words = queue.Queue()

	# for word in rawWords:
	# 	word = word.rstrip()

	# 	if resume is not None:
	# 		if found_res:
	# 			words.put(word)
	# 		else:
	# 			if word == resume:
	# 				found_res = True
	# 	else:
	# 		words.put(word)

def back(extensions=None):
	fd = open(outFile, "w")

	while not wordQueue.empty():
		attempt = wordQueue.get()
		attempt_list = []
		if "." not in str(attempt):
			attempt_list.append("/{}/".format(attempt))
		else:
			attempt_list.append("/{}".format(attempt))

		if extensions:
			for extension in extensions:
				attempt_list.append("/{}{}".format(attempt, extension))

		for brute in attempt_list:
			url = "%s%s" % (targetUrl, urllib.parse.quote(brute))

			try:
				headers = {}
				headers["User-Agent"] = userAgent
				r = urllib.request.Request(url, headers=headers)

				response = urllib.request.urlopen(r)
				if len(response.read()):
					resp = str(response.code) +" :: "+url+"\n"
					fd.write(resp)
			except urllib.error.HTTPError as e:
				if hasattr(e, 'code') and e.code != 404:
					resp = "[!!!]" + " :: " +str(e.code) + " :: " + url+"\n"
					fd.write(resp)

		


def setStage():
	# global wordQueue
	global wordlist, wordQueue, outFile, operation, targetUrl
	print("Enter the target url to fuzz:", end='')
	targetUrl = input()
	print("Currently using dictionary at:",wordlist)
	ch = input("Change dictionary? (y/N): ")
	if(ch=="y" or ch =="Y"):

		wordlist = input("Enter path to dictionary: ")
	
	# global wordQueue
	makeDictionary()
	
	name = dt.isoformat(dt.now())
	# global outFile
	outFile = "outputs/DirFuzzer/"+name+".txt"
	print(F"[!] Results will be written to file:\n\t{outFile}")
	operation = "directory fuzzing for host "+targetUrl

