##What the heck?##
This repo is supposed to hold some small scripts which can be used to troll around the internet (if nothing else).
These are actually example code snippets I am making while learning new things. I am posting them here with a hope that these will prove helpful for someone or atleast I myself can use them as examples for teaching some new programmer (I love teaching stuff, and people grasp pretty fast when doing wrong things).  

Here is the list of all the scripts included in this repo with descriptions:

##fullonsms.py##
**You need to sign up at fullonsms.com to use this.**  
This script forge http requests to send sms through fullonsms.com. Since it usess fullonsms.com which is available only in India, this might be of no use for others.

###Usage###
Just run <code>python fullonsms.py</code> from the console and follow the instructions. *You need to sign up at fullonsms.com*

###Dependencies###
*	Python [Requests](https://github.com/kennethreitz/requests) library (<code>pip install requests</code>)  

###Status###
Was working till the push date.

##notDoppler.py##
Illustrating use of BeautifulSoup.  
A crawler to extract all game links (swf files) from notdoppler.com by crawling through all pages. 
**Only work with notdoppler.com**

###Usage###
*	Change GAME_LINKS and CRAWL_LINKS variables to the destination where you want to save the files. (Will overwrite if file already present)
	*	GAME_LINKS = Address of file to save game links (swf files) (e.g. "/home/user/filename")
	*	CRAWL_LINKS = Address of file to save links which script is going to crawl (e.g. "/home/user/filename")
*	Run <code>python ./notDoppler.py</code> from terminal and grab some popcorn :-)

###Dependencies###
*	Python [Requests](https://github.com/kennethreitz/requests) library (<code>pip install requests</code>)  
*	Python [BeautifulSoup](http://www.crummy.com/software/BeautifulSoup) library (<code>pip install bs4</code>)    

###Status###
Was working till push date.  
Fails when touches protected pages. This can be avoided but I didn't do it. 'Cause the purpose is demonstration of BeautifulSoup (moreover, it fails after getting through about 2000 pages, extracting about 1600 swf links, which is enough for task at hand).