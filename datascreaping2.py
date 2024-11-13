import requests
from bs4 import BeautifulSoup

def data_scraping():
    url = "https://www.indiatoday.in/world/us-news/story/georgia-election-result-live-donald-trump-kamala-harris-republican-democract-2628764-2024-11-06"
    req = requests.get(url)
    soup = BeautifulSoup(req.text, 'html.parser')

    title = soup.find('h1', attrs={'class': 'headline'}).text.strip()

    content_div = soup.find('div', attrs={'class': 'article-content'})
    paragraphs = content_div.find_all('p')
    content = '\n'.join([p.text for p in paragraphs])

    print("Title:", title)
    print("Content:", content)

data_scraping()
