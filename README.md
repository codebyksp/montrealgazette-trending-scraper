# Montreal Gazette Trending Scraper

A Python script that scrapes the 5 trending news stories from the [Montreal Gazette](https://montrealgazette.com/category/news/) and saves them in a structured JSON file.

## Overview
This project demonstrates web scraping techniques for collecting structured data from live web pages. The scraper:
- Collects trending article links from the Montreal Gazette news page.
- Extracts the **title**, **publication date**, **author**, and **blurb** from each article.
- Caches requests to avoid excessive server load.
- Outputs results to a `.json` file.

This project was developed for **COMP 370 – Homework 7: Web Scraping** (Fall 2025).

---

## Installation

1. Clone the repository:
```bash
git clone https://github.com/<your-username>/montrealgazette-trending-scraper.git
cd montrealgazette-trending-scraper
```
2. (Optional) Create and activate a virtual environment:
python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows

3. Install required dependencies:
pip install -r requirements.txt

## Usage

Run the scraper with:

```bash
python collect_trending.py -o trending.json
```

-o specifies the output JSON file name.

By default, the script scrapes 5 trending articles. 

## Output Format

The output JSON has the following structure:
```bash
[
  {
    "title": "Update: Woman arrested after abandoned newborn dies in Longueuil",
    "publication_date": "Oct 27, 2025",
    "author": "Jack Wilson",
    "blurb": "The 33-year-old may be subject to a psychological evaluation and could face charges in connection with the infant's death, police said."
  },
  ...
]
```
## Caching

Requests are cached using requests_cache for 1 hour to reduce repeated requests to the Montreal Gazette website. Cached responses are used automatically if available.

## Logging

The script uses Python's logging module:

INFO level logs show progress, such as fetching pages and extracting links.

Logs help debug the scraper and monitor caching.

## License / Credits

Developed for COMP 370 – Web Scraping (Fall 2025)

Data source: Montreal Gazette https://montrealgazette.com/