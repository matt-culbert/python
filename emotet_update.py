import re
import urllib.request
import io
u = urllib.request.urlopen("https://paste.cryptolaemus.com/feed.xml", data = None)
f = io.TextIOWrapper(u,encoding='utf-8')

stream = f.read()

match = re.match(r"(?<=<code>)(.*)(?=<\/code>)",stream)