import requests, bs4
from datetime import datetime as dt
from requests.exceptions import *
from urllib.parse import urlparse, urlunparse


targetURL = ''

operation = ''

outFile = ''


def launchAttack():
	global targetURL
	if 'http' not in targetURL:
		targetURL = F'http://{targetURL}'
	parsedTarget = urlparse(targetURL)
	res = requests.Response()
	fd = open(outFile,'w')
	fd.write(F'Web crawling summary against target {targetURL} carried out at {dt.now()}\n')
	try:
		res = requests.get(targetURL)
	except URLRequired as ur:
		fd.write('[!!!] Invalid URL provided\n')
	except ConnectTimeout:
		fd.write('[!!!] Connection timed out\n')
	except HTTPError as hte:
		fd.write(F'[!!!] Error occurred: {hte}\n')
	except Exception as e:
		fd.write(F'[!!!] Exception occurred: {e}\n')
	
	if(res.status_code==404):
		fd.write('[!!!] Page not found\n')
	else:
		soupObj = bs4.BeautifulSoup(res.text, 'html.parser')
		for link in soupObj.find_all('a'):
			href = link.get('href')
			parsedURL = urlparse(href)
			if len(parsedURL.scheme) == 0:
				parsedURL = parsedURL._replace(scheme='http')
			if len(parsedURL.netloc) == 0:
				parsedURL = parsedURL._replace(netloc=parsedTarget.netloc)
			fd.write(F'[url] == {urlunparse(parsedURL)}\n')

	fd.close()


def setStage():
	global targetURL, operation, outFile
	targetURL = input('Enter the url of the page to be scraped: ')
	name = dt.isoformat(dt.now())
	outFile = F'outputs/URLCrawler/{name}.txt'
	print(F'output will be written to {outFile}')
	operation = F'URL scraping on target {targetURL}'

