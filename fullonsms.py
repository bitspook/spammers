import requests
from urllib import quote_plus

url = 'http://www.fullonsms.com/'
username = raw_input("Enter your fullonsms username: ")
password = raw_input("Enter your fullonsms password: ")
message = raw_input("Enter Your message: ")
reciever = raw_input("Enter reciever phone number: ")



#Custom headers. Not needed but being an paranoid, I added them anyway

headers = {
	"User-Agent":"Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0)2011-10-16 20:21:07",
	"Accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
	"Accept-Language": "en-US,en;q=0.8,hi-IN;q=0.5,hi;q=0.3",
	"Accept-Charset": "ISO-8859-1,utf-8;q=0.7,*;q=0.7",
	"Referer": "http://www.fullonsms.com/login.php",
	"Content-Type": "application/x-www-form-urlencoded"
}

#Create a session 
session = requests.session()

#Data headers needed to make post request for login
data = {
	"MobileNoLogin":username,
	"LoginPassword":password,
	"RememberMe":1,
	'x':40,						#meaning of x and y is still unkown to me, tell 
	'y':19						#me if you know what the heck it is	
}

#make a request using data
print("Logging in to your fullonsms account")
login_res = session.post(url+"login.php/", headers=headers, data=data)
if login_res.status_code==200:
	print("Login Successfull!! :-)")
else:
	print("Login failed! :-(")

#data headers to be sent with message post request
msg_data = "ActionScript=%2Fhome.php&CancelScript=%2Fhome.php&HtmlTemplate=%2Fvar%2Fwww%2Fhtml%2Ffullonsms%2FStaticSpamWarning.html&MessageLength=140&MobileNos="+reciever+"&Message="+quote_plus(message)+"&Gender=0&FriendName=Your+Friend+Name&ETemplatesId=&TabValue=contacts"

#post request to send message
print("Sending message")
send_message = session.post(url+"home.php",data=msg_data, prefetch=True)
print("Message Sent (probably)")

