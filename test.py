import requests as r
from bs4 import BeautifulSoup
import Filterer as ftr

def make_json(name, platform, genre, developer, summary, review, source, url):
    data = {}
    data["Name"] = name
    data["Platform"] = platform
    data["Genre"] = ""
    data["Developer"] = dev
    data["Summary"] = summary
    data["Review"] = review
    data["Source"] = source
    data["Url"] = url
    return data

headers = {
        'User-Agent': 'WebIR Crawler',
        'From': 'Kasetsart University'
        }

a = r.get("https://www.metacritic.com/game/xbox-one/red-dead-redemption-2/", headers=headers)
critic = r.get("https://www.metacritic.com/game/xbox-one/red-dead-redemption-2/critic-reviews")

soup = BeautifulSoup(a, "html.parser")

name = ftr.extract_name(soup)
platform = ftr.extract_platform(soup)
dev = ftr.extract_developer(soup)
summary = ftr.extract_summary(soup)
genre = ftr.extract_genre(soup)
review = ftr.extract_review(soup)
source = ftr.extract_source(soup)
url = ftr.extract_url(soup)

print(name)
print(platform)
print(dev)
print(summary)
print(genre)
print(review)
print(source)
print(url)

data = make_json(name, platform, genre, dev, summary, review, source, url)

f = open("dict.json", "w")
f.write(str(data))
f.close()