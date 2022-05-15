import urllib.request, urllib.parse, urllib.error
import json

u = 'http://py4e-data.dr-chuck.net/comments_1533192.json'
print('Retrieving', u)
with urllib.request.urlopen(u) as url:
    x = json.loads(url.read().decode())

print('Retrieved', len(str(x)))
d = x.get('comments')

num = sum = 0
for i in range(len(d)):
    t = d[i]
    v = t.get('count')
#    num += 1
    sum = sum + int(v)
# print(num)
print(sum)
