from bs4 import BeautifulSoup
import re, random
import urllib.request

user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
headers={'User-Agent':user_agent,} 

def getfestivalTime(query):
	# open a connection to a URL using urllib
	# fh = open("hello.txt", "w")
	url = 'http://www.google.co.in/search?q={}'.format('+'.join(query.split()))
	# print(url)
	request=urllib.request.Request(url,None,headers) #add header since directly google search not allowing to access result
	webUrl  = urllib.request.urlopen(request)
	data = webUrl.read()
	soup = BeautifulSoup(data, "lxml", from_encoding="utf-8")
	# f = open('f.html', 'w')
	# f.writelines(str(data))
	fest_details = soup.find_all('div', {'class':'_rkc _Qeb'})
	festival_time = "Your question is not correct"
	if len(fest_details) != 0:
		festival_time = fest_details[0].find("span").getText()
	return festival_time