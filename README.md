# Near Real-Time Data Processing Pipeline

## Overview

This project demonstrates a near real-time data pipeline using:

- PySpark Structured Streaming
- Delta Lake
- Bronze-Silver Architecture
- Streamlit Dashboard

## Architecture

Raw Events
↓
Bronze Layer
↓
Silver Layer
↓
Dashboard

## Tech Stack

- Python
- PySpark
- Delta Lake
- Streamlit
- GitHub

## Run

### Generate Events

```bash
python event_generator.py
```

### Bronze Layer

```bash
python spark_bronze.py
```

### Silver Layer

```bash
python spark_silver.py
```

### Dashboard

```bash
streamlit run dashboard.py
```