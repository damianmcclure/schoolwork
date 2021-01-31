import urllib.request, urllib.parse, urllib.error
import json

url = urllib.request.urlopen("http://py4e-data.dr-chuck.net/comments_919082.json")
info = json.loads(url.read())

sum = 0
for item in info["comments"]:
    sum = sum + int(item["count"])

print(sum)
