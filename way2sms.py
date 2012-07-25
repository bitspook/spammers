import requests
from urllib import quote_plus

url = 'http://site5.way2sms.com/'
username = '8557993738'
password = '9780795704'
message = "Hello I am Jinga lala lalal"
reciever = '9592494566'
#Custom headers. Not needed but being an paranoid, I added them anyway

headers = {
	"User-Agent":"Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0)2011-10-16 20:21:07",
	"Accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
	"Accept-Language": "en-US,en;q=0.8,hi-IN;q=0.5,hi;q=0.3",
	"Accept-Charset": "ISO-8859-1,utf-8;q=0.7,*;q=0.7",
	"Referer": "http://site5.way2sms.com/content/index.html",
	"Content-Type": "application/x-www-form-urlencoded"
}

#Create a session 
session = requests.session()

#Data headers needed to make post request for login
data = {
	"username":username,
	"password":password,
	"button":"Login"
}

#make a request using data
print("Logging in to your way2sms account")
login_res = session.post("http://site5.way2sms.com/Login1.action", headers=headers, data=data)
if login_res.status_code==200:
	print("Login Successfull!! :-)")
else:
	print("Login failed! :-(")

print(login_res.content)
print(login_res.cookies)
#time to send message

#data headers to be sent with message post request
msg_data = "HiddenAction=instantsms&catnamedis=Birthday&Action=sa65sdf656fdfd&chkall=on&MobNo="+reciever+"&textArea="+quote_plus(message)

while(True):
	#post request to send message
	print("Sending message")
	send_message = session.post("http://site5.way2sms.com/",data=msg_data)
	print("Message Sent (probably)")
	print(send_message.content)
	print(send_message.cookies)
	prompt=raw_input("Wanna send another message?(y or n)")
	if prompt=='n' or prompt=='N':
		break 
	else:
		message = raw_input("Enter Next message: ")
		reciever = raw_input("Enter reciever no.: ")
	





