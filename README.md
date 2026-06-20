# Near Real-Time Data Processing Pipeline

## Overview

This project demonstrates a near real-time data pipeline using:

- PySpark Structured Streaming
- Delta Lake
- Bronze-Silver Architecture
- Streamlit Dashboard

## Folder Structure

Near-Real-Time-Pipeline/

│
├── data/
│   ├── raw_events/
│   ├── bronze/
│   ├── silver/
│   └── checkpoints/
│
├── event_generator.py
├── spark_bronze.py
├── spark_silver.py
├── dashboard.py
│
├── requirements.txt
└── README.md
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
