# Job Listings Web Research & Data Validation

## Overview

This is a personal practice project focused on collecting, organizing,
validating, and filtering publicly available job listing data from a
practice website.

The project automatically navigates through multiple pages, extracts job
listing information, performs basic data cleaning and validation, and
exports both the complete dataset and a date-filtered subset to CSV.

## What the Project Does

The program:

- navigates through the available job listing pages;
- extracts structured information from each listing;
- cleans text fields;
- converts publication dates into a structured date format;
- checks for duplicate records;
- checks for missing values;
- filters listings based on a publication date;
- exports the results to CSV.

## Data Collected

Each job listing contains:

- Title
- Company
- Location
- Type
- Publication date

## Process

The collector:

1. accesses the pages using `Requests`;
2. parses the HTML with `BeautifulSoup`;
3. identifies rows in the job listing table;
4. extracts the relevant fields;
5. automatically follows pagination;
6. organizes the data using `Pandas`;
7. removes unnecessary whitespace;
8. converts publication dates to a structured format;
9. checks for duplicate records;
10. checks for missing values;
11. filters listings published from a specified date;
12. exports the complete and filtered datasets to CSV.

## Technologies

- Python
- Requests
- BeautifulSoup
- Pandas
- CSV

## Results

A total of **30 job listings were collected across 6 pages**.

Data validation found:

- **0 duplicate records**
- **0 missing values**

Publication dates were converted to a structured date format, and listings
published from **September 1, 2026** were separated into a dedicated file.

The project generates:

```text
job_listings.csv
recent_job_listings.csv
```

`job_listings.csv` contains the complete collected dataset.

`recent_job_listings.csv` contains the subset filtered by publication date.

## Skills Demonstrated

- Web Data Collection
- Web Research
- Web Scraping
- Data Extraction
- Data Cleaning
- Data Validation
- Data Transformation
- Filtering by Criteria
- CSV Data Processing
- Python

## Project Type

**Personal Practice Project**

This project was created for learning and portfolio development.
It was not developed for a paid client.
