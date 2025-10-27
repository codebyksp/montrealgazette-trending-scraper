# Montreal Gazette Trending Scraper

A Python script that scrapes the 5 trending news stories from the [Montreal Gazette](https://montrealgazette.com/category/news/) and saves them in a structured JSON file.

## 📰 Overview
This project demonstrates web scraping techniques for collecting structured data from live web pages. The scraper:
- Collects trending article links from the Montreal Gazette news page.
- Extracts the **title**, **publication date**, **author**, and **blurb** from each article.
- Caches requests to avoid excessive server load.
- Outputs results to a `.json` file.

This project was developed for **COMP 370 – Homework 7: Web Scraping** (Fall 2025).

---

## ⚙️ Installation

Clone the repository:
```bash
git clone https://github.com/<your-username>/montrealgazette-trending-scraper.git
cd montrealgazette-trending-scraper
