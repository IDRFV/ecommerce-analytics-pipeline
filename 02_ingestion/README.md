# Stage 2: Ingestion

## Approach
Data is downloaded programmatically via Kaggle API directly into Databricks Volume.
No manual downloads. No local storage.

## What Was Tried
| Approach | Result |
|----------|--------|
| os.makedirs to /dbfs/ | Failed — DBFS root disabled in Community Edition |
| dbutils.fs.cp from /tmp/ | Failed — local filesystem access denied |
| subprocess download to /tmp/ + shutil.copy to Volume | Success |
| Databricks Secrets via CLI | Failed — Community Edition limitation |
| dotenv from local .env file | Failed — Databricks runs in cloud, no access to local files |
| Databricks Widget | Success — secure token input at runtime |

## Final Solution
1. Install kaggle library in notebook: %pip install kaggle python-dotenv
2. Set KAGGLE_TOKEN securely via Databricks Widget at runtime
3. Download dataset to /tmp/ via kaggle CLI
4. Copy files from /tmp/ to Volume via shutil

## Token Security
Kaggle API token is passed via Databricks Widget at runtime.
Token is never stored in code or committed to GitHub.
Widget appears as input field at top of notebook before each run.

## Storage Location
/Volumes/workspace/default/ecommerce_raw/

## Files Ingested
| File | Size |
|------|------|
| 2019-Oct.csv | 5.6 GB |
| 2019-Nov.csv | 9.0 GB |
| **Total** | **14.6 GB** |

## Row Count Confirmed
| File | Rows |
|------|------|
| 2019-Oct.csv | 42,448,764 |
| 2019-Nov.csv | 67,501,979 |
| **Total** | **109,950,743** |

## Open Questions Answered
- Q: What does Kaggle API link return?
  A: Same 2 files — 2019-Oct.csv and 2019-Nov.csv

## Confirmed From Stage 1
- category_code contains NULL values — confirmed in first 5 rows
- brand contains NULL values — confirmed in first 5 rows
- category_code has varying hierarchy levels — confirmed (2 and 3 levels observed)

## Open Questions Remaining
1. How many category_code values have 2 levels vs 3 levels?
2. How many distinct values of product_id length exist?
3. Does remove_from_cart appear in event_type column?
4. Are there additional months available beyond Oct-Nov 2019?