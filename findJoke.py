#Find a joke

from bs4 import BeautifulSoup
from bs4 import UnicodeDammit
import re, random


def tellAJoke():
	with open("joke.txt") as fp:
		soup = BeautifulSoup(fp, "lxml", from_encoding="utf-8")

	raw_joke_list = soup.find_all('p', {'id':re.compile('joke_')})
	joke_list = []
	for joke in raw_joke_list:
		joke_list.append(joke.getText().strip())
		
	return joke_list[random.randint(0, len(joke_list) - 1)]
	
print(tellAJoke())
