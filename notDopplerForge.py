import requests
from bs4 import BeautifulSoup
import re

soup = BeautifulSoup(requests.get("http://www.notdoppler.com/action.php").content)

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
	'''Returns the game link if one present in the page, or return empty object 
			of Nonetype otherwise'''
	try:
		game_link = soup.find_all('embed',src=re.compile('swf'))[0].get('src')
		return game_link
	except:
		pass

def get_game_image(soup):
	'''Returns the image link for the game to be shown in embed body on html'''

class notDoppler():
 	"""notDoppler class"""

 	def __init__(self, soup):
 		self.soup = soup

	def get_game_name(soup):
		'''Function returns a dict containing game_name and game_type'''

		span_list = []
		for span in soup.find_all('span'):		#loop to get list of all spans of class 'gamephp1'
			if span.has_key('class') and span['class']==['gamephp1']: #tag['class'] returns a list
				span_list.append(span)

		detail_dict = {}
		cur = 1 	#curson to go through loop
		while(cur<len(span_list)):		#loop tp populate dict with game_name and game_type
		    detail_dict[span_list[cur]]=span_list[cur+1]
    		cur += 2

        return detail_dict

	def get_thumbs(soup,thumbs, game_pages):
		'''Returns dictionary of game data.'''
		for i in soup.find_all('td'):
			if i.has_key('width') and i['width']=='175':
				if type(i.img) != type(None):
					thumbs.add(i.img['src'])
					if i.img.parent.has_key('href'):
                		game_pages.add(i.img.parent['href'])
        for game_name,game_page, thumb in game_pages, thumbs:
        	game_data['name']['thumb'] = thumb
        	game_data['name']['game_page'] = game_page


		return thumbs
	game_data = dict()
	thumbs = set()
	game_pages = set()
	return get_thumbs(soup,thumbs)


# from index page
thumbnails = get_thumbs_set(soup)
game_page = ''
genere = ''
game_name = ''
game_description = ''

# from game page
game_link = ''
created_by = ''


if __name__ == '__main__':
	for i in get_thumbs_set(soup):
		print i