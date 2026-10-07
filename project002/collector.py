import requests
from bs4 import BeautifulSoup
import pandas as pd


def collect_page(url):
    response = requests.get(url, timeout=10)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")
    data = []

    for book in soup.select("article.product_pod"):
        title = book.select_one("h3 a")["title"]
        price = book.select_one("p.price_color").get_text(strip=True)

        price = (
            price
            .replace("£", "")
            .replace("Â", "")
            .strip()
        )

        price = float(price)

        availability = book.select_one(
            "p.instock.availability"
        ).get_text(" ", strip=True)

        data.append({
            "title": title,
            "price": price,
            "availability": availability
        })

    next_page = soup.select_one("li.next a")

    if next_page:
        next_url = requests.compat.urljoin(url, next_page["href"])
    else:
        next_url = None

    return data, next_url


url = "https://books.toscrape.com/"

data = []
current_url = url

while current_url:
    books, next_url = collect_page(current_url)
    data.extend(books)

    print(f"Page processed: {current_url}")

    current_url = next_url


df = pd.DataFrame(data)

cheapest = df.sort_values("price").head(10)

print("\n10 cheapest books:")
print(cheapest)

most_expensive = df.sort_values("price", ascending=False).head(10)

print("\n10 most expensive books:")
print(most_expensive)


print("\nData summary:")
print(f"Number of books: {len(df)}")
print(f"Average price: £{df['price'].mean():.2f}")
print(f"Minimum price: £{df['price'].min():.2f}")
print(f"Maximum price: £{df['price'].max():.2f}")

cheapest.to_csv(
    "10_cheapest_books.csv",
    index=False,
    encoding="utf-8"
)

most_expensive.to_csv(
    "10_most_expensive_books.csv",
    index=False,
    encoding="utf-8"
)

print("\nAnalysis files saved.")

df.to_csv("books.csv", index=False, encoding="utf-8")

print(f"\n{len(df)} books collected.")
print("File saved: books.csv")
