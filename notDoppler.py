import requests
from bs4 import BeautifulSoup
import re

base_url = "http://www.notdoppler.com"
links_to_crawl = [base_url, 'http://www.notdoppler.com/adventure.php']
#a list of addresses to be crawled, to prevent recrawling same pages again
#(see get_links_to_crawl() )
addresses = []

#opening files to write links with line buffering
GAME_LINKS = open("/home/channi/Desktop/notdoppler_game_links", 'w',1)
CRAWL_LINKS = open("/home/channi/Desktop/notdoppler_crawl_links", 'w',1)

def main():
	'''Main function, it do all the job'''
	global links_to_crawl
	global addresses

	for link in links_to_crawl:

		print 'Crawling ' + link		
		soup = BeautifulSoup(requests.get(link).content)
				
		
		#if a game present on page, put the link in file 
			#otherwise print 'No game found'
		print "Extracting game from page"
		game_link = get_game_link(soup)
		#if no game (swf file) is found on page, function returns
			#empty object of Nonetype. 
		if (type(game_link) != type(None)):
			GAME_LINKS.write(game_link+'\n')
		else:
			print "No game found on page"

		for new_link in get_links_to_crawl(soup):
			CRAWL_LINKS.write(new_link +'\n')  
			if new_link not in links_to_crawl:		#precaution in case of link duplication
				links_to_crawl.append(new_link)
				print "Link '"+new_link+"' added to list"



def get_links_to_crawl(soup):
	'''Get the links to crawl from the current page. Returns list of non duplicate links'''
	links = []
	for anchor in soup.find_all('a'):		#get all links
			address = anchor.get('href')		#get href attribute of links
			
			#some links don't have hrefs, in that case empty object of Nonetype is returned
			if type(address) != type(None):	
				#filter empty link, duplicate link and pass link with php extension
				if len(address) > 3 and address not in addresses and 'php' in address:
					addresses.append(address)
					#make link iterable by adding needed info (based on the structure
						#of different links on notdoppler.com)
					if 'http://' in address and "http://www.notdoppler.com" not in address:
						continue
					elif "http://www.notdoppler.com/" in address:
						links.append(address)				
					elif address[0] == '/':
						links.append("http://www.notdoppler.com"+address)
					else:
						links.append("http://www.notdoppler.com/"+address)

	return links	


def get_game_link(soup): #page_link):
	'''Get the game link if one present in the page, or return empty object 
			of Nonetype otherwise'''
	try:
		game_link = soup.find_all('embed',src=re.compile('swf'))[0].get('src')
		return game_link
	except:
		pass

if __name__ == '__main__':
	main()
	GAME_LINKS.close()
	CRAWL_LINKS.close()
