## Overview
A Python-based automation tool designed to extract, process and summarize live cryptocurrency market data from Centralized Exchanges. 

Instead of manually checking trading platforms, this application programmatically fetches real-time ticker prices directly from the Website's API, filters for a targeted portfolio of multiple currencies (e.g., BTC, ETH, SOL, BNB), and formats the output. It then feeds this live data into a Large Language Model (Google Gemini) to generate a concise executive summary and exports the raw data to a timestamped spreadsheet for further research.

## Key Features
* **Live Binance Integration:** Efficiently pulls real-time market data across the entire exchange in a single network request to respect API rate limits.
* **Multi-Currency Tracking:** Dynamically filters and tracks specific high-cap assets simultaneously.
* **AI-Powered Market Summaries:** Uses the Google GenAI SDK to process raw numbers into a readable, two-sentence executive market report.
* **Automated CSV Export:** Generates timestamped `.csv` files locally for daily record-keeping and data science workflows.
* **Modular Architecture:** Code is split across dedicated services using standard OOP principles for high maintainability.

## Project Structure
```text
cex-scout/
│
├── main.py            # The main entry point that orchestrates the workflow
├── models.py          # Data blueprints for the Token objects
├── scraper.py         # Network logic, headers, and Binance API interactions
├── storage.py         # Logic for exporting data to timestamped CSV files
├── .env               # Hidden environment variables
├── .gitignore         
└── README.md
```
## Prerequisites
* Python 3.8+

## How to run
* Clone the repo
  ```bash
     git clone https://github.com/naham6/cex-scout.git
     cd cex-scout
* Put your api in .env file
* Run
  ```bash
     python main.py
  ```
  
