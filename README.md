# Job Opportunity Scraper

Automated job search tool designed to reduce daily time spent browsing job boards.
Focused on Data Analyst, Operations Analyst, and related technical roles.

## Motivation
Manually checking multiple job boards every day is time-consuming.
This project automates the process of collecting new job opportunities so more time can be spent on learning and portfolio building.

## Current Features
- Scraper for Colombia's public job board (buscadordeempleo.gov.co)
- Support for multiple job profiles
- Pagination handling to retrieve all available results

## Project Structure
- config/ → search profiles configuration
- scrapers/ → job board scrapers
- core/ → data normalization and filtering logic (in progress)
- run_daily.py → main execution script

## Configuration
This project uses a configuration file to define the job profiles to search for.

1. Copy the example configuration file:
```bash
cp config/profiles.example.json config/profiles.json
```
2.Edit profiles.json and add your desired search profiles.

## How to run
To execute the job search:
```python run_daily.py```
This script will collect job postings for all configured profiles.

## Roadmap
- Normalize job data into a standard format
- Add filtering and scoring logic
- Store results locally (CSV or database)
- Implement notifications for new job opportunities

