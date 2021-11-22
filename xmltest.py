import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'http://py4e-data.dr-chuck.net/comments_868888.xml'
data = urllib.request.urlopen(url, context=ctx).read()

tree = ET.fromstring(data)

lst = tree.findall('comments/comment')

allscore = []
for comment in lst:
	name = comment.find('name').text
	score = int(comment.find('count').text)
	allscore.append(score)
print(sum(allscore))
	