# Python Web Scraper

A beginner-friendly Python web scraper that collects book information from [Books to Scrape](https://books.toscrape.com/).

## Features
- Extracts 1,000 book records across multiple pages (based on the current run).
- Collects book titles, prices, ratings, and links.
- Saves the collected data into a CSV file.
- Uses a one-second delay between pages.

## Technologies Used
- Python
- Requests
- BeautifulSoup
- CSV

## Installation

Install the required libraries:

```bash
pip install -r requirements.txt
```

## How to Run

```bash
python main.py
```

The scraped data will be saved in `books.csv`.

## Project Structure

```text
web-scraper/
├── main.py
├── requirements.txt
├── README.md
├── .gitignore
└── books.csv
```

## Website
https://books.toscrape.com/

## Author
Thandu Hema vardini