# Web Data Collection with Python

## Overview

This is a personal practice project focused on collecting and organizing
publicly available web data using Python.

The project collects quotes and their authors from a practice website,
automatically navigating through the available pages and exporting the
collected records to a structured CSV file.

## What the Project Does

The program:

- accesses the website;
- identifies quotes and their authors;
- navigates automatically through the available pages;
- organizes the collected data into a table;
- exports the final dataset to CSV.

## Data Collected

Each record contains:

- Author
- Quote text

A total of **100 quotes** were collected.

## How It Works

The scraper:

1. accesses the page using `Requests`;
2. parses the HTML with `BeautifulSoup`;
3. locates quotes using CSS selectors;
4. extracts the author and quote text;
5. identifies the next page automatically;
6. repeats the process until the end of the pagination;
7. organizes the data using `Pandas`;
8. generates the `quotes.csv` file.

The project also includes basic error handling for HTTP requests.

## Technologies

- Python
- Requests
- BeautifulSoup
- Pandas
- CSV

## Result

The final dataset contains **100 records** and is delivered as:

```text
quotes.csv
```

The CSV file contains:

- 1 header row
- 100 data records

## Skills Demonstrated

- Web Data Collection
- Web Scraping
- HTML Parsing
- Data Extraction
- Pagination Handling
- Data Organization
- CSV Data Processing
- Python

## Project Objective

This project is part of a practical laboratory focused on collecting and
organizing publicly available web data.

The objective is to develop skills applicable to:

- web scraping;
- data extraction;
- data organization and cleaning;
- CSV generation;
- automation of repetitive data collection tasks.

## Project Type

**Personal Practice Project**

This project was created for learning and portfolio development.
It was not developed for a paid client.
