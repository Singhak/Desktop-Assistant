# http://www.imdb.com/search/title?title={}&title_type=feature&countries=in
from bs4 import BeautifulSoup
import urllib.request

def movieRating(query):
	# open a connection to a URL using urllib
	# fh = open("julie.txt", "r")
	# data = fh.read()
	url = "http://www.imdb.com/search/title?title={}&title_type=feature&countries=in"
	webUrl  = urllib.request.urlopen(url.format(query.replace(" ", "+")))
	data = webUrl.read()
	soup = BeautifulSoup(data, "lxml")
	raw_movie_list = soup.find_all('div', {'class':"lister-item-content"})#h3 class="lister-item-header
	for raw in raw_movie_list:
		title = raw.find('h3', {'class':"lister-item-header"}).find('a').getText()
		year = raw.find('h3', {'class':"lister-item-header"}).find('span', {'class':"lister-item-year text-muted unbold"})
		year = year.getText().strip() if year else ""
		
		details = raw.find('p', {'class':"text-muted"})
		summary = raw.find_all('p', {'class':"text-muted"})[1]
		summary = summary.getText().strip() if summary else "-"
		
		certificate = details.find('span', {"class":"certificate"})
		certificate = certificate.getText().strip() if certificate else "-"
		
		runtime = details.find('span', {"class":"runtime"})
		runtime = runtime.getText().strip() if runtime else "-"
		
		genre = details.find('span', {"class":"genre"})
		genre = genre.getText().strip() if genre else "-"
		
		rating = raw.find('span', {"class":"value"})
		rating = rating.getText().strip() if rating else "-"
		
		print("Title: "+title)
		print("Release Year: "+year)
		print("Certificate: "+certificate)
		print("Duration: "+runtime)
		print("Genre: "+genre)
		print("Rating: "+rating)
		print("Summary: "+summary)
		print("---------------------------------------------------------\n")
		# break;