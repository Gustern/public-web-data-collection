import requests
from bs4 import BeautifulSoup
import pandas as pd


def collect_page(url):
    response = requests.get(url, timeout=10)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")
    data = []

    for row in soup.select("table tbody tr"):
        cells = row.select("td")

        title = cells[0].get_text(strip=True)
        company = cells[1].get_text(strip=True)
        location = cells[2].get_text(" ", strip=True)
        job_type = cells[3].get_text(strip=True)
        publication_date = cells[4].get_text(strip=True)

        data.append({
            "title": title,
            "company": company,
            "location": location,
            "type": job_type,
            "publication_date": publication_date
        })

    next_page = soup.select_one("a[rel='next']")

    if next_page:
        next_url = requests.compat.urljoin(url, next_page["href"])
    else:
        next_url = None

    return data, next_url


url = "https://practice.scrapingcentral.com/jobs"

data = []
current_url = url

while current_url:
    records, next_url = collect_page(current_url)
    data.extend(records)

    print(f"Page processed: {current_url}")

    if next_url:
        current_url = next_url
    else:
        current_url = None


df = pd.DataFrame(data)

df["title"] = df["title"].str.strip()
df["company"] = df["company"].str.strip()
df["location"] = df["location"].str.strip()
df["type"] = df["type"].str.strip()
df["publication_date"] = df["publication_date"].str.strip()

print("\nData after cleaning:")
print(df)

df["publication_date"] = pd.to_datetime(df["publication_date"])

print("\nColumn types:")
print(df.dtypes)

duplicates = df.duplicated().sum()
print(f"\nDuplicate records: {duplicates}")

print("\nMissing values by column:")
print(df.isna().sum())

recent = df[df["publication_date"] >= "2026-09-01"]

print("\nRecords published from 2026-09-01:")
print(recent)

print(f"\nNumber of recent records: {len(recent)}")

recent.to_csv(
    "recent_job_listings.csv",
    index=False,
    encoding="utf-8"
)

print("\nFile saved: recent_job_listings.csv")

print(f"\nNumber of records: {len(df)}")

df.to_csv(
    "job_listings.csv",
    index=False,
    encoding="utf-8"
)

print("File saved: job_listings.csv")
