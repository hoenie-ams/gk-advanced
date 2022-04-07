"""
Demo of Beautifulsoup
"""
from bs4 import BeautifulSoup
import requests
from metar import Metar

html_string = """
<html>
<head>
    <title>My Website</title>
</head>
<body>
<h1>Welcome to my website!</h1>
<p>So much cool stuff here...</p>
<p class="special">the secret data</p>
</body>
</html>
"""

url = "https://www.knmi.nl/nederland-nu/luchtvaart/vliegveldwaarnemingen"
r = requests.get(url)
soup = BeautifulSoup(r.text)

pre = soup.find("pre", attrs={})

text = pre.text
lines = text.split("\n\n")

measurements = []

for index, line in enumerate(lines):
    data = "METAR" + lines[index].split("METAR")[-1]   # UGLY, use Regex instead
    obj = Metar.Metar(data)
    measurements.append(obj)
