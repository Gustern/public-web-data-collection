import requests
from bs4 import BeautifulSoup
import pandas as pd


def prepare_data(data):
    df = pd.DataFrame(data)

    df["publication_date"] = pd.to_datetime(df["publication_date"])

    job_listings = df[
        [
            "job_title",
            "company",
            "location",
            "job_type",
            "publication_date",
            "job_url",
            "company_url",
            "source_url"
        ]
    ].copy()

    companies = (
        df[["company", "company_url"]]
        .drop_duplicates()
    )

    job_count = (
        df["company"]
        .value_counts()
        .rename("job_count")
    )

    companies = companies.merge(
        job_count,
        left_on="company",
        right_index=True
    )

    companies = (
        companies
        .sort_values("company")
        .reset_index(drop=True)
    )

    return job_listings, companies


def collect_page(url):
    response = requests.get(url, timeout=10)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")
    data = []

    for row in soup.select("table tbody tr"):
        cells = row.select("td")

        job_link = cells[0].select_one("a")
        company_link = cells[1].select_one("a")

        job_title = job_link.get_text(strip=True)
        company = company_link.get_text(strip=True)
        location = cells[2].get_text(" ", strip=True)
        job_type = cells[3].get_text(strip=True)
        publication_date = cells[4].get_text(strip=True)

        job_url = requests.compat.urljoin(
            url,
            job_link["href"]
        )

        company_url = requests.compat.urljoin(
            url,
            company_link["href"]
        )

        data.append({
            "job_title": job_title,
            "company": company,
            "location": location,
            "job_type": job_type,
            "publication_date": publication_date,
            "job_url": job_url,
            "company_url": company_url,
            "source_url": url
        })

    next_page = soup.select_one("a[rel='next']")

    if next_page:
        next_url = requests.compat.urljoin(
            url,
            next_page["href"]
        )
    else:
        next_url = None

    return data, next_url


def collect_all_jobs(start_url):
    all_data = []
    current_url = start_url

    while current_url:
        data, next_url = collect_page(current_url)
        all_data.extend(data)

        print(f"Page processed: {current_url}")

        current_url = next_url

    return all_data


def main():
    url = "https://practice.scrapingcentral.com/jobs"

    all_data = collect_all_jobs(url)

    job_listings, companies = prepare_data(all_data)

    print(f"\nNumber of job listings: {len(job_listings)}")
    print(f"Number of companies: {len(companies)}")

    job_listings.to_csv(
        "job_listings.csv",
        index=False,
        encoding="utf-8"
    )

    companies.to_csv(
        "companies.csv",
        index=False,
        encoding="utf-8"
    )

    job_listings.to_excel(
        "job_listings.xlsx",
        index=False
    )

    companies.to_excel(
        "companies.xlsx",
        index=False
    )

    print("\nExported files:")
    print("job_listings.csv")
    print("companies.csv")
    print("job_listings.xlsx")
    print("companies.xlsx")


if __name__ == "__main__":
    main()
