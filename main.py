
import requests
from bs4 import BeautifulSoup
import csv
from urllib.parse import urljoin
import time

BASE_URL = "https://books.toscrape.com/"

def scrape_books():
    books = []
    url = BASE_URL

    while url:
        print("Scraping:", url)

        try:
            response = requests.get(
                url,
                headers={"User-Agent": "Mozilla/5.0"},
                timeout=15
            )
            response.raise_for_status()

            soup = BeautifulSoup(response.text, "html.parser")

            book_items = soup.find_all(
                "article", class_="product_pod"
            )

            for book in book_items:
                title = book.h3.a["title"]
                price = book.find(
                    "p", class_="price_color"
                ).text.strip()

                rating = book.find(
                    "p", class_="star-rating"
                )["class"][1]

                link = urljoin(url, book.h3.a["href"])

                books.append({
                    "Title": title,
                    "Price": price,
                    "Rating": rating,
                    "Link": link
                })

            next_page = soup.find("li", class_="next")

            if next_page:
                url = urljoin(url, next_page.a["href"])
                time.sleep(1)
            else:
                url = None

        except requests.RequestException as error:
            print("Website error:", error)
            break

    return books


def save_to_csv(books):
    if not books:
        print("No books collected.")
        return

    with open("books.csv", "w", newline="", encoding="utf-8-sig") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=["Title", "Price", "Rating", "Link"]
        )
        writer.writeheader()
        writer.writerows(books)

    print("Data saved successfully in books.csv!")


if __name__ == "__main__":
    print("===== PYTHON WEB SCRAPER =====")
    collected_books = scrape_books()
    print("Total books collected:", len(collected_books))
    save_to_csv(collected_books)
