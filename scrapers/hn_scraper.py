import requests
from bs4 import BeautifulSoup

def get_hn_ideas():
    url = "https://news.ycombinator.com/"
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "lxml")

    return [a.text for a in soup.select(".titleline a") if len(a.text) > 20]
