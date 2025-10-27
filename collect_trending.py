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
    # Title
    title_tag = soup.select_one("h1.article-title")
    title = title_tag.get_text(strip=True) if title_tag else ""

    # Blurb / subtitle
    blurb_tag = soup.select_one("p.article-subtitle")
    blurb = blurb_tag.get_text(strip=True) if blurb_tag else ""

    # Author
    author_tag = soup.select_one("span.published-by__author a")
    author = author_tag.get_text(strip=True) if author_tag else ""

    # Publication date
    date_tag = soup.select_one("div.published-date__since")
    if date_tag:
        publication_date = date_tag.get_text(strip=True).replace("Published ", "")
    else:
        publication_date = ""

    return {
        "title": title,
        "publication_date": publication_date,
        "author": author,
        "blurb": blurb
    }

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
    
    # Step 4: Extract article info for each link
    url = "https://montrealgazette.com/news/crime/baby-found-abandoned-in-longueuil-bus-shelter"  
    soup = fetch(url)
    article_info = extract_article_info(soup, url)
    print(json.dumps(article_info, indent=2))


if __name__ == "__main__":
    main()
