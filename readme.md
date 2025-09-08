# E-commerce Analytics Data Pipeline

## Project Overview

This project is a **data synchronization service** for an e-commerce analytics platform. It fetches, cleans, and standardizes customer engagement data from a simulated third-party API, handling real-world challenges such as:

* Pagination
* Network failures
* Data inconsistencies

The pipeline prepares analytics-ready customer data with enriched business logic for insights.


## Features

* **API Client**: Fetches all customer data reliably with retries, rate-limit handling, and pagination.
* **Data Processor**: Transforms raw API data into structured, analytics-ready format. Adds business logic fields:

  * Engagement Level (high/medium/low)
  * Activity Status (active/inactive)
  * Acquisition Channel (website/mobile/email)
  * Market Segment (US-West/US-East/EU/APAC)
  * Customer Tier (basic/premium/enterprise)
* **Data Quality Handling**: Deduplicates records, handles missing fields, and computes data quality score.
* **Exporter**: Saves processed customer data to `sample_output.json` with metadata (total customers, quality summary).
* **Bonus Features**: Optional async API calls, caching, and environment-based configuration.


## Project Structure

```
customer_data_pipeline/
├── src/
│   ├── api_client.py
│   ├── data_processor.py
│   ├── exporter.py
│   ├── models.py
│   └── main.py
├── tests/
│   ├── test_api_client.py
│   ├── test_data_processor.py
│   └── test_integration.py
├── requirements.txt
├── README.md
└── sample_output.json      # Generated output
```


## Getting Started

### 1. Clone the repository

```bash
git clone <repo-url>
cd customer_data_pipeline
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the pipeline

```bash
python -m src.main
```

* Processed data will be saved in `sample_output.json` at the project root.
* Logs will show the number of customers fetched and processed.

### 4. Run Tests

```bash
python -m pytest tests
```

Covers:

* API retry logic
* Data transformation
* Deduplication
* Data quality scoring
* Edge case handling


## Output Format

```json
{
  "metadata": {
    "total_customers": 12,
    "export_timestamp": "2025-09-04T18:41:19Z",
    "data_quality_summary": {
      "high_quality": 8,
      "medium_quality": 3,
      "low_quality": 1
    }
  },
  "customers": [
    {
      "customer_id": 1,
      "full_name": "George Bluth",
      "email_domain": "reqres.in",
      "engagement_level": "high",
      "activity_status": "active",
      "acquisition_channel": "website",
      "market_segment": "US-West",
      "customer_tier": "premium",
      "data_quality_score": 100
    }
    // ... more customers
  ]
}
```

## Notes

* All modules in `src/` use **relative imports**, compatible with `python -m src.main`.
* `sample_output.json` is created in the **project root**.
* The project is designed for **robust error handling, modular design, and production readiness**.

##Task Report
*Please check the report for a better understanding of the project*
*Link:* https://drive.google.com/file/d/1cmQHYbwuqsdA_0KMya_y-eSl1zPFVFXN/view?usp=drivesdk
