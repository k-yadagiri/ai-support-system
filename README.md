# AI Support Ticket Analyzer

## Overview

AI Support Ticket Analyzer is a Streamlit-based application that analyzes customer support tickets using Artificial Intelligence and anomaly detection techniques.

The application allows users to:

* Load support ticket data from an Excel file
* Ask natural language questions about support tickets
* Detect anomalies in ticket handling
* Analyze ticket statistics and performance metrics
* View support ticket data through an interactive dashboard

---

## Features

### Data Ingestion

* Reads support ticket data from Excel files
* Processes ticket information using Pandas

### Natural Language Querying

Users can ask questions such as:

* How many tickets are there?
* How many open tickets?
* How many resolved tickets?
* What is the average customer rating?
* Which agent resolved the most tickets?

### Anomaly Detection

Detects:

* Tickets with unusually high resolution times
* Critical tickets that are not yet resolved

### Interactive Dashboard

Built using Streamlit with:

* KPI Cards
* Dataset Preview
* Question Answering Interface
* Anomaly Detection Reports

---

## Technologies Used

* Python
* Pandas
* Streamlit
* Groq LLM API
* OpenPyXL
* Python Dotenv

---

## Project Structure

ai-support-system/
│
├── data/
│   └── support_tickets.xlsx
│
├── .env
├── app.py
├── data_loader.py
├── query_engine.py
├── anomaly_detector.py
├── requirements.txt
├── README.md
└──  venv/

---

## Installation

### Clone Repository

```bash
git clone <repository-url>
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

## Sample Questions

* How many tickets are there?
* How many open tickets?
* How many resolved tickets?
* Which agent has the lowest average customer rating?
* What is the average resolution time?
* How many critical tickets are unresolved?

---

## Author

Yadagiri

