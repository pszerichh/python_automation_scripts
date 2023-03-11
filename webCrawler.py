import bs4
import requests
import re
from datetime import datetime as dt
url = ""

def back():
	web = requests.get(url) #http request
	soup = bs4.BeautifulSoup(web.text, 'html.parser') #soup object
	for link in soup.find_all('a'):
		l_href = link.get('href') #extracting the href value
		if(type(l_href) == str): #avoiding urls with href value NoneType
			if(len(l_href) >= 2): #avoiding page refreshing links
				div = re.split('/', link.get('href'))
				if(len(div) >= 2): #avoiding javascripts
					if(div[0] == 'https:'):
						i = 0
						for it in (mod.nex_it):
							if(it == l_href):
								i = i+1
							else:
								continue

						if( i == 0 ):
							mod.nex_it.append(l_href) #collecting url
							config.logger.info(l_href)
						else:
							continue

					elif(div[0] == 'http:'):
						i = 0
						for it in (mod.nex_it):
							if(it == l_href):
								i = i+1
							else:
								continue

						if( i ==0 ):
							mod.nex_it.append(l_href) #collecting url
							config.logger.info(l_href)
						else:
							continue

					else:
						i = 0
						temp_href = urls + l_href
						for it in (mod.nex_it):
							if(it == temp_href):
								i = i+1
							else:
								continue

						if(i == 0):
							
						else:
							continue

				else:
					continue

			else:
				continue

		else:
			continue



def fun():
	global url
	url = input("Enter url to scrape: ")
	name = dt.isoformat(dt.now())
	file_name = "outputs/webScrape/"+name+".txt"
	print("Results will be written to file: ",file)
	return file_name