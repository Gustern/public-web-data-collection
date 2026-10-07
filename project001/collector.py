import requests
from bs4 import BeautifulSoup
import pandas as pd


def collect_page(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()

    except requests.exceptions.RequestException as error:
        print(f"Error accessing {url}")
        print(error)

        return [], None

    soup = BeautifulSoup(response.text, "html.parser")

    data = []

    for quote in soup.select(".quote"):
        text = quote.select_one(".text").get_text(strip=True)
        author = quote.select_one(".author").get_text(strip=True)

        data.append({
            "author": author,
            "quote": text
        })

    next_page = soup.select_one("li.next a")

    if next_page:
        next_url = "https://quotes.toscrape.com" + next_page["href"]
    else:
        next_url = None

    return data, next_url


url = "https://quotes.toscrape.com/"
all_data = []

while url:
    print(f"Collecting: {url}")

    data, url = collect_page(url)

    all_data.extend(data)


df = pd.DataFrame(all_data)

df.to_csv("quotes.csv", index=False, encoding="utf-8")

print(f"\n{len(df)} records collected.")
print("File saved: quotes.csv")
