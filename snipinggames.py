from bs4 import BeautifulSoup
from requests import get
import re

soup = BeautifulSoup(get('http://www.snipinggames.net/').content)

links = []
for link in soup.find_all('a'):
	if str(link).find('php') > 0:
		if 'http://www.snipinggames.net/' in str(link):
			links.append(str(link.get('href')))
		else:
			links.append('http://www.snipinggames.net/'+str(link.get('href')))

game_links = []
for link in links:	
	game_soup = BeautifulSoup(get(link).content)
	embedded_game = game_soup.find_all(attrs={'src':re.compile("swf")})[0]['src']
	if type(embedded_game) == dict:
		game_link = embedded_game['src']
		print game_link
		game_links.append(game_link)

for i in links:
	print i