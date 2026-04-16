# 💼 Naukri Job Scraper (India Jobs)

## 🚀 Project Overview

This project is a Python-based web scraper that extracts job listings from Naukri.com.

It allows users to:

* Select number of pages to scrape
* Set a limit for total job results
* Extract job data and save it into a structured CSV file

---

## 🛠️ Technologies Used

* Python
* Selenium
* Undetected ChromeDriver
* BeautifulSoup
* Pandas

---

## ⚙️ How It Works

### Step 1: User Input

The script takes input from the user:

* Number of pages to scrape
* Maximum number of job listings (limit)

---

### Step 2: Scraping Data

* Opens Naukri.com job pages
* Navigates through multiple pages
* Simulates human behavior (scrolling & mouse movement)
* Extracts job HTML data
* Saves each job listing as a separate `.html` file

---

### Step 3: Parsing Data

* Reads all saved HTML files
* Extracts:

  * Job Title
  * Job Description / Summary
  * Additional Job Details
* Converts data into structured format
* Saves output into CSV file

---

## 📁 Project Structure

```id="9tt6qg"
project-folder/
│
├── scraper.py
├── parser.py
├── data_files/
│   ├── 1.html
│   ├── 2.html
│   └── ...
│
├── CSV_FILE.csv
└── README.md
```

---

## ▶️ How to Run

### 1. Install Dependencies

```bash id="3p2dpd"
pip install selenium undetected-chromedriver beautifulsoup4 pandas
```

---

### 2. Run Scraper

```bash id="jng4r6"
python scraper.py
```

👉 Enter:

* Number of pages
* Job limit

---

### 3. Run Parser

```bash id="8q6zaz"
python parser.py
```

---

## 📌 Features

* Dynamic input (pages + limit)
* Multi-page scraping
* Controlled data extraction (limit system)
* Human-like behavior simulation
* Automatic HTML storage
* Structured CSV output

---

## 📊 Output Example

| Job Title        | Description             | Details   |
| ---------------- | ----------------------- | --------- |
| Python Developer | Work on backend systems | Full-time |
| Data Analyst     | Analyze data trends     | Remote    |

---

## ⚠️ Notes

* Website structure may change, so selectors may need updates
* Use responsibly and follow website terms

---

## 💼 Use Case

This project is useful for:

* Job data collection
* Market research
* Resume/job analysis
* Automation of job scraping

---

## 📬 Contact

If you need any web scraping or automation project, feel free to reach out.

---
