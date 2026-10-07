# Web Data Collection & Structured Excel/CSV Delivery

## Overview

This personal practice project simulates a client request for collecting
publicly available job listing data and delivering the results in structured
CSV and Excel files.

The project collects records from all available pages of a public practice
website, validates the dataset, identifies unique companies, and creates
separate datasets for job listings and companies.

## Simulated Client Request

The client requested:

- collection of job listings from a public source;
- navigation through all available pages;
- data organized in spreadsheets;
- no duplicate records;
- source URLs for the collected records;
- delivery in CSV and Excel format.

## Source

Public practice website:

https://practice.scrapingcentral.com/jobs

The data comes from an environment intended for web scraping practice.

## Data Collected

### Job Listings

Each record contains:

- Job title
- Company
- Location
- Job type
- Publication date
- Job URL
- Company URL
- Source URL

### Companies

A second dataset is created containing:

- Company
- Company URL
- Number of job listings found

## Processing

The project performs:

1. page requests using `Requests`;
2. HTML parsing with `BeautifulSoup`;
3. extraction of job listing data;
4. automatic detection of the next page;
5. collection of all available pages;
6. data transformation with `Pandas`;
7. date conversion;
8. dataset validation;
9. identification of unique companies;
10. counting job listings by company;
11. generation of the final files.

## Results

The dataset contains:

- **30 job listings**
- **10 unique companies**
- **0 duplicate records**
- **0 missing values**
- **0 empty values**

## Deliverables

### Job Listings

- `job_listings.csv`
- `job_listings.xlsx`

### Companies

- `companies.csv`
- `companies.xlsx`

## Technologies

- Python
- Requests
- BeautifulSoup
- Pandas
- OpenPyXL

## Project Type

**Personal Practice Project**

This project was created for learning and portfolio development.
It simulates a structured client data-collection request and was not
developed for a paid client.
