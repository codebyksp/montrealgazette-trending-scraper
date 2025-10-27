# collect_trending.py
import argparse, json
import logging
from urllib.parse import urljoin, urlparse
# imports for requests, bs4, requests_cache
import requests, requests_cache
from bs4 import BeautifulSoup
requests_cache.install_cache('gazette_cache', expire_after=3600)

BASE_URL = "https://montrealgazette.com"
NEWS_HOME = "https://montrealgazette.com/category/news/"

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("collect_trending")

def fetch(url):
    r = requests.get(url, headers={"User-Agent": "COMP370-scraper/1.0"}, timeout=10)
    #print(r.status_code)  # 200 means success
    #print(r.text[:500])   # first 500 characters of the HTML
    r.raise_for_status()
    # print(r.from_cache)  # True or False using cache
    return BeautifulSoup(r.text, "html.parser")

def find_trending_links(soup, limit=5):
    # Find the container with the trending articles
    trending_list = soup.select_one("ol.list-widget__content")
    if not trending_list:
        return []

    links = []
    # Loop over each article card in the list
    for a in trending_list.select("article.article-card a.article-card__link[href]"):
        href = a['href']
        full_url = urljoin(BASE_URL, href)
        if full_url not in links:
            links.append(full_url)
        if len(links) >= limit:
            break

    return links

def extract_article_info(soup, url): 
    pass
def collect_trending(output): 
    pass

def main():
    # Step 1: Fetch the page
    soup = fetch(NEWS_HOME)
    
    # Step 2: Print the first 500 characters to make sure we got HTML
    print("Fetched HTML preview:\n", soup.prettify()[:500], "\n")
    
    # Step 3: Extract trending links
    links = find_trending_links(soup)
    print(f"Found {len(links)} trending links:")
    for link in links:
        print(link)


if __name__ == "__main__":
    main()
