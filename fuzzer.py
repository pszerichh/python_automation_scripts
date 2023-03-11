import urllib
import urllib.parse, urllib.request, urllib.error
import queue
from datetime import datetime as dt

target_url = ""
word_file = "sample_list.txt"
resume = None
user_agent = "Mozilla/5.0 (X11; Linux x86_64; rv:19.0) Gecko/20100101 Firefox/19.0"
operation=""

ext = [".php", ".txt", ".bak", ".js", ".html"]

wrd_queue = queue.Queue()
file_name = ""

def list_build():
	fd = open(word_file, "r")
	raw_words = fd.readlines()
	fd.close()

	found_res = False
	words = queue.Queue()

	for word in raw_words:
		word = word.rstrip()

		if resume is not None:
			if found_res:
				words.put(word)
			else:
				if word == resume:
					found_res = True
		else:
			words.put(word)

	return words

def back(extensions=None):
	fd = open(file_name, "w")

	while not wrd_queue.empty():
		attempt = wrd_queue.get()
		attempt_list = []
		if "." not in str(attempt):
			attempt_list.append("/{}/".format(attempt))
		else:
			attempt_list.append("/{}".format(attempt))

		if extensions:
			for extension in extensions:
				attempt_list.append("/{}{}".format(attempt, extension))

		for brute in attempt_list:
			url = "%s%s" % (target_url, urllib.parse.quote(brute))

			try:
				headers = {}
				headers["User-Agent"] = user_agent
				r = urllib.request.Request(url, headers=headers)

				response = urllib.request.urlopen(r)
				if len(response.read()):
					resp = str(response.code) +" :: "+url+"\n"
					fd.write(resp)
			except urllib.error.HTTPError as e:
				if hasattr(e, 'code') and e.code != 404:
					resp = "[!!!]" + " :: " +str(e.code) + " :: " + url+"\n"
					fd.write(resp)

		


def fun():
	global wrd_queue
	wrd_queue = list_build()
	print("Enter the target url to fuzz:")
	global target_url
	target_url = input()
	global word_file
	print("Currently using dictionary at:",word_file)
	ch = input("Change dictionary? (y/N): ")
	if(ch=="y" or ch =="Y"):
		word_file = input("Enter path to dictionary: ")
	
	name = dt.isoformat(dt.now())
	global file_name
	file_name = "outputs/DirFuzz/"+name+".txt"
	print("[!] Results will be written to file:\n",file_name)
	global operation
	operation = "directory fuzzing for host "+target_url

