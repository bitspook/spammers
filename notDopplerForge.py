import requests
from bs4 import BeautifulSoup
import re
import MySQLdb

# soup = BeautifulSoup(requests.get("http://www.notdoppler.com/action.php").content)

def get_game_link(page_link):
	'''Returns the game link if one present in the page, or return empty object 
			of Nonetype otherwise'''
	soup = BeautifulSoup(requests.get(page_link).content)
	try:
		game_link = soup.find_all('embed',src=re.compile('swf'))[0].get('src')
		return game_link
	except:
		pass

def get_game_details(soup):
	'''Returns a dict containing game_name and game_type
		detail_dict['game_name'] = [game_type, thumb, game_page, game_link]'''

	name_list = []
	game_pages = []
	#loop to get lists of game_names and game_types, and game_pages
	for span in soup.find_all('span'):		
		if span.has_key('class') and span['class']==['gamephp1']: #tag['class'] returns a list
			if(span.a['href'][0]=='/'):
				game_pages.append(span.a['href'])

			for string in span.a.stripped_strings:
				name_list.append(string)

	thumbs = []
	#loop to get thumbnails
	for span in soup.find_all('span'):
	    if span.has_key('class') and span['class']==['gamephp1']:
	    	if(span.parent.parent.parent.previous_sibling and type(span.parent.parent.parent.previous_sibling)==type(soup.a)):
	    		thumbs.append(span.parent.parent.parent.previous_sibling.img['src'])

	detail_dict = {}
	detail_list = []
	name_cur = 1 	
	game_cur = 0
	thumb_cur = 0
	#loop tp populate dict with game_name, game_type and thumbnail uri
	while(name_cur<len(name_list) and thumb_cur<len(thumbs)):	
	    detail_dict[name_list[name_cur]]=[name_list[name_cur+1],thumbs[thumb_cur], game_pages[game_cur]]
	    name_cur += 2
	    game_cur += 2
	    thumb_cur += 1

	base_url = "http://www.notdoppler.com"
	game_links = []

	# game_link = get_game_link(base_url+detail_dict['PLAZMA BURST 2'][2])
	# game_links.append(game_link)

	for game in detail_dict:
		game_link = get_game_link(base_url+detail_dict[game][2])
		#if no game (swf file) is found on page, function returns
			#empty object of Nonetype. 
		if (type(game_link) != type(None)):
			game_links.append("Game not found")
		else:
			game_links.append(game_link)

	#loop to enter game link of the game
	for game,link in map(None, detail_dict, game_links):
		detail_dict[game].append(link)
		
	return detail_dict


def main():
	db_user = 'root'
	db_pass = 'root'
	db_name = 'online_games'
	db = MySQLdb.connect('localhost', db_user, db_pass, db_name)

	cursor = db.cursor()

	query = """select * from notDoppler"""
	try:
		cursor.execute(query)
		result = cursor.fetchall()
		print result
	except Exception, e:
		print e
		print "Shit happens"
	finally:
		db.close()


if __name__ == '__main__':
	print main()
