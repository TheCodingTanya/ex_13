import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

url = 'http://py4e-data.dr-chuck.net/comments_1533191.xml'
u = urllib.request.urlopen(url)

d = u.read()
tree = ET.fromstring(d)

counts = tree.findall('.//count')
clst = [int(count.text) for count in counts]
print(sum(clst))
