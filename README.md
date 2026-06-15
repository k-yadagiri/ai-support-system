# AI Support Ticket Analyzer

## Overview

AI Support Ticket Analyzer is a Streamlit-based application that analyzes customer support tickets using Artificial Intelligence and anomaly detection techniques.

The application allows users to:

- Load support ticket data from an Excel file
- Ask natural language questions about support tickets
- Detect anomalies in ticket handling
- Analyze ticket statistics and performance metrics
- View support ticket data through an interactive dashboard

---

## Features

### Data Ingestion

- Reads support ticket data from Excel files
- Processes ticket information using Pandas
- Makes ticket data queryable for analytics

### Natural Language Querying

Users can ask questions such as:

- How many tickets are there?
- How many open tickets?
- How many resolved tickets?
- How many escalated tickets?
- What is the average customer rating?
- Which agent has the lowest average customer rating?
- Which agent resolved the most tickets?
- What is the average resolution time?
- How many critical tickets are unresolved?

### Anomaly Detection

The system detects:

- Tickets with unusually high resolution times
- Critical tickets that are not yet resolved

### Interactive Dashboard

Built using Streamlit with:

- KPI Cards
- Dataset Preview
- Question Answering Interface
- Anomaly Detection Reports

---

## Architecture

```text
Support Tickets Dataset (Excel)
            │
            ▼
      Pandas Loader
            │
            ▼
      Query Engine
            │
            ├── Rule-Based Analytics
            │
            └── Groq LLM (Llama 3.3 70B)
            │
            ▼
    Anomaly Detection Module
            │
            ▼
      Streamlit Dashboard
```

---

## Technologies Used

- Python
- Pandas
- Streamlit
- Groq API
- Llama 3.3 70B Versatile
- OpenPyXL
- Python Dotenv

---

## Project Structure

```text
ai-support-system/

├── data/
│   └── support_tickets.xlsx
│
├── app.py
├── data_loader.py
├── query_engine.py
├── anomaly_detector.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Installation

### Clone Repository

```bash
git clone https://github.com/k-yadagiri/ai-support-system.git
cd ai-support-system
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Configure Environment Variables

Create a `.env` file:

```env
GROQ_API_KEY=your_groq_api_key
```

### Run Application

```bash
streamlit run app.py
```

---

## Example Queries & Outputs

### Query

```text
How many tickets are there?
```

### Output

```text
Total Tickets: 500
```

### Query

```text
How many open tickets?
```

### Output

```text
Open Tickets: 111
```

### Query

```text
Which agent resolved the most tickets?
```

### Output

```text
AGT-09 resolved the most tickets (37)
```

### Query

```text
How many critical tickets are unresolved?
```

### Output

```text
Unresolved Critical Tickets: 31
```

---

## Anomaly Detection

The application identifies:

1. Tickets with unusually long resolution times.
2. Critical tickets that remain unresolved.

These anomalies are displayed directly in the dashboard with detailed records.

---

## Known Limitations

- Query engine currently supports a predefined set of business questions.
- Complex analytical queries may require additional query rules.
- Groq API key must be configured locally using a `.env` file.
- The application currently uses a local Excel dataset and does not connect to a live ticketing system.

---

## Future Improvements

- Support dynamic query generation using LLM-driven dataframe analysis.
- Add visual analytics and charts.
- Deploy the application on Streamlit Cloud.
- Connect to real-time ticketing systems and databases.
- Add REST API endpoints using FastAPI.

---

## Author

**Yadagiri**

B.Tech – Computer Science Engineering (AI & DS)

Skills: Python, SQL, Machine Learning, Deep Learning, LLM, RAG, GenAI, Streamlit