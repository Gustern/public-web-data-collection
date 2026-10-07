# Book Data Collection & Price Analysis

## Overview

This is a personal practice project focused on collecting, organizing,
transforming, and analyzing publicly available book data from a practice
website.

The program automatically navigates through the catalog, collects book
information, normalizes prices, and produces structured CSV files.

## What the Project Does

The program:

- automatically navigates through the catalog pages;
- collects book information;
- normalizes price values and converts them to numbers;
- organizes the collected data into a structured dataset;
- calculates basic price statistics;
- identifies the 10 cheapest and 10 most expensive books;
- exports the results to CSV files.

## Data Collected

Each book record contains:

- Title
- Price
- Availability

A total of **1,000 books** were collected.

## Process

The scraper:

1. accesses the catalog using `Requests`;
2. parses the HTML with `BeautifulSoup`;
3. identifies books on each page;
4. extracts title, price, and availability;
5. normalizes and converts the price to a numeric value;
6. automatically navigates through all catalog pages;
7. organizes the data using `Pandas`;
8. calculates basic price statistics;
9. identifies the 10 cheapest and 10 most expensive books;
10. exports the results to CSV files.

## Technologies

- Python
- Requests
- BeautifulSoup
- Pandas
- CSV

## Results

A total of **1,000 books** were collected.

### Price Summary

- Average price: **£35.07**
- Minimum price: **£10.00**
- Maximum price: **£59.99**

### Output Files

```text
books.csv
10_cheapest_books.csv
10_most_expensive_books.csv
```

`books.csv` contains the complete collected dataset.

The other two files contain subsets generated from the price analysis.

## Skills Demonstrated

- Web Data Collection
- Web Scraping
- HTML Parsing
- Data Extraction
- Pagination Handling
- Data Cleaning and Transformation
- Basic Data Analysis
- Pandas
- CSV Data Processing
- Python

## Project Objective

This project is part of a practical laboratory focused on collecting,
processing, and analyzing publicly available web data.

The objective is to develop skills applicable to:

- web scraping;
- data extraction and organization;
- data cleaning and transformation;
- basic data analysis with Pandas;
- CSV generation;
- automation of data collection and processing tasks.

## Project Type

**Personal Practice Project**

This project was created for learning and portfolio development.
It was not developed for a paid client.
