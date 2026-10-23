# Olympic Games Data Analysis

## Project Overview

This project explores historical Olympic Games data to identify patterns in Olympic editions, sports and events, athlete demographics, medal records, and regional participation.

The workflow combines SQL analysis in PostgreSQL, Python-based database access, Pandas DataFrames, Excel analysis outputs, and a five-page Power BI report.

## Project Objectives

- Explore the number and frequency of Olympic editions over time.
- Compare sports and event counts across Olympic editions.
- Examine athlete participation and demographic patterns.
- Analyze medal-related records by sport, edition, and National Olympic Committee (NOC) or region.
- Present the analysis in an organized Excel workbook and Power BI dashboard.

## Tools and Technologies

- **PostgreSQL** — relational database and SQL queries.
- **Python** — analysis workflow and database access.
- **SQLAlchemy** — connection between Python and PostgreSQL.
- **Pandas** — receiving SQL query results as DataFrames for inspection and handling.
- **Microsoft Excel** — organization of 18 exploratory data analysis (EDA) result sheets and supporting sheets.
- **Microsoft Power BI Desktop** — data model and interactive dashboard.

## Repository Structure

```text
olympics-data-analysis/
├── 01_Documentation/
│   ├── ER_Diagram.png
│   ├── olympics_db_description.txt
│   ├── Olympics_Project_Documentation.docx
│   └── Olympics_Project_Documentation.pdf
├── 02_SQL_Analysis_Using_SQLAlchemy_Python/
│   └── olympics_project.ipynb
├── 03_Excel_Analysis/
│   └── olympics_eda_complete.xlsx
├── 04_PowerBI/
│   ├── SportsAnalytics.pbix
│   └── SportsAnalyticsPowerBI_Report.pdf
├── 05_Presentations/
│   ├── Olympics_Rough_Presentation.pdf
│   ├── Olympics_Final_Presentation.pdf
├── 06_Video_Presentation/
│   └── README.md
├── .gitignore
└── README.md
```

The tree above describes the intended layout. File names or optional files may differ slightly depending on the final contents committed to the repository.

## Analysis Coverage

The EDA workbook contains 18 query-result sheets covering questions about:

1. Olympic editions and historical trends.
2. Sports, events, and event categories.
3. Athlete participation and demographics.
4. Medal-related records and performance.
5. Regional representation and participation.

## Power BI Dashboard

The Power BI report is organized into five pages:

1. **Olympic Overview** — editions by season, host city, and decade.
2. **Sports & Events** — sports, event counts, event categories, and trends.
3. **Athlete Demographics** — participation by region and gender, and average age.
4. **Medal Analysis** — medal-related records by edition, NOC, and sport.
5. **Regional Participation** — regional representation and medal categories over time.

## Running the Notebook

The notebook was developed against a local PostgreSQL database named `olympics_db`.

The original local connection helper file is intentionally excluded because it contains local database configuration. To reproduce the notebook, configure your own PostgreSQL connection and define the required connection/query helper functions. Do not commit passwords, tokens, or other credentials.

## Interpretation and Limitations

- The analysis is descriptive and identifies patterns in the supplied dataset; it does not establish causal explanations.
- Participation entries are not necessarily the same as unique athletes.
- Competitor-event medal records are not always equivalent to counts of unique physical medals, particularly for team events.
- Historical NOC and region labels may change over time.
- Height and weight fields can contain placeholder values; these should be handled carefully in demographic analysis.
- The dataset described for this project covers Summer Games through 2016 and Winter Games through 2014.

## Project Deliverables

The repository is intended to include the project report and ER diagram, Jupyter notebook, EDA Excel workbook, Power BI report, rough and final presentations, and a link to the video presentation where appropriate.

## Author

Panduranga Katti
