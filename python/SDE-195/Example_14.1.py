import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

url = urllib.request.urlopen("http://py4e-data.dr-chuck.net/comments_919080.xml")
tree = ET.fromstring(url.read())

numbers = tree.findall('.//count')

sum = 0
for num in numbers:
    sum = sum + int(num.text)

print(sum)
