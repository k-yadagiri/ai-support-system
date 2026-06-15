# AI Support Ticket Analyzer

## Overview

AI Support Ticket Analyzer is a Streamlit-based application that analyzes customer support tickets using Artificial Intelligence and anomaly detection techniques.

The application enables users to:

- Load support ticket data from an Excel dataset
- Ask natural language questions about support tickets
- Detect anomalies in ticket handling
- Analyze ticket statistics and performance metrics
- View support ticket insights through an interactive dashboard

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
- Critical tickets that remain unresolved

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
      Pandas Data Loader
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

Open the application in your browser:

```text
http://localhost:8501
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

Detected anomalies are displayed directly in the dashboard along with the corresponding ticket records.

---

## Known Limitations

- Query engine currently supports a predefined set of business questions.
- Complex analytical queries may require additional query rules.
- Groq API key must be configured locally using a `.env` file.
- The application currently uses a local Excel dataset and does not connect to a live ticketing platform.

---

## Future Improvements

- Dynamic dataframe analysis using LLM-generated queries
- Advanced visualizations and charts
- Streamlit Cloud deployment
- Real-time database integration
- FastAPI REST API support
- Enhanced anomaly detection techniques

---
## Application Screenshots

- **Dashboard** → [View Image](screenshots/AI%20Support%20Ticket%20Analyzer%20Dashbord.png)

- **Query and Answer** → [View Image](screenshots/Query%20and%20Answer.png)

- **Anomaly Detection** → [View Image](screenshots/Anomaly%20Detection.png)

---

## Author

**Yadagiri**

B.Tech – Computer Science Engineering (AI & DS)

Skills: Python, SQL, Machine Learning, Deep Learning, Power BI, GenAI, Streamlit
