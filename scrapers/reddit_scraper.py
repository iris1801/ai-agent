import requests
from bs4 import BeautifulSoup

def get_reddit_ideas(subreddit="SideHustle"):
    url = f"https://www.reddit.com/r/{subreddit}/top/?t=month"
    headers = {"User-agent": "RevenueSeekerBot/0.1"}
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, "lxml")

    ideas = []
    for post in soup.select("h3"):
        if len(post.text.strip()) > 20:
            ideas.append(post.text.strip())
    return ideas
