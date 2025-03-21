# Deep Seek Crawler

This project is a web crawler built with Python that extracts mentors data from a website using asynchronous programming with Crawl4AI. It utilizes a language model-based extraction strategy and saves the collected data to a CSV file.

## Features

- Asynchronous web crawling using [Crawl4AI](https://pypi.org/project/Crawl4AI/)
- Data extraction powered by a language model (LLM)
- CSV export of extracted mentor information
- Modular and easy-to-follow code structure ideal for beginners

## Project Structure
```
.
├── main.py # Main entry point for the crawler
├── config.py # Contains configuration constants (Base URL, CSS selectors, etc.)
├── models
│ └── mentor.py # Defines the mentors data model using Pydantic
├── utils
│ ├── init.py # (Empty) Package marker for utils
│ ├── data_utils.py # Utility functions for processing and saving data
│ └── scraper_utils.py # Utility functions for configuring and running the crawler
├── requirements.txt # Python package dependencies
├── .gitignore # Git ignore file (e.g., excludes .env and CSV files)
└── README.MD # This file
```

## Installation

1. **Create and Activate a Conda Environment**

   ```bash
   conda create -n deep-seek-crawler python=3.12 -y
   conda activate deep-seek-crawler
   ```

2. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

3. **Set Up Your Environment Variables**

   Create a `.env` file in the root directory with content similar to:

   ```env
   GROQ_API_KEY=your_groq_api_key_here
   ```

   *(Note: The `.env` file is in your .gitignore, so it won’t be pushed to version control.)*

## Usage

To start the crawler, run:

```bash
python main.py
```

The script will crawl the specified website, extract data page by page, and save the complete mentors to a `all_mentors.csv` file in the project directory. Additionally, usage statistics for the LLM strategy will be displayed after crawling.


Include license information if applicable.
