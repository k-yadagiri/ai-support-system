import streamlit as st

from data_loader import load_data
from query_engine import ask_question
from anomaly_detector import detect_anomalies


st.set_page_config(
    page_title="AI Support Ticket Analyzer",
    page_icon="🎫",
    layout="wide"
)

# Load Data
df = load_data()

# Header
st.title("🎫 AI Support Ticket Analyzer")
st.markdown("Analyze support tickets using AI and anomaly detection.")

# KPI Section
total_tickets = len(df)
open_tickets = len(df[df["status"] == "Open"])
resolved_tickets = len(df[df["status"] == "Resolved"])
escalated_tickets = len(df[df["status"] == "Escalated"])

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Total Tickets", total_tickets)

with col2:
    st.metric("Open Tickets", open_tickets)

with col3:
    st.metric("Resolved Tickets", resolved_tickets)

with col4:
    st.metric("Escalated Tickets", escalated_tickets)

st.divider()

# Dataset Preview
st.subheader("📊 Dataset Preview")

st.dataframe(
    df.head(10),
    use_container_width=True
)

st.divider()

# Question Answering
st.subheader("🤖 Ask Questions")

question = st.text_input(
    "Ask a question about support tickets"
)

if st.button("Get Answer"):

    if question:

        with st.spinner("Analyzing..."):

            answer = ask_question(
                df,
                question
            )

            st.success(answer)

st.divider()

# Anomaly Detection
st.subheader("🚨 Anomaly Detection")

if st.button("Detect Anomalies"):

    anomalies = detect_anomalies(df)

    if anomalies:

        for anomaly in anomalies:

            st.warning(
                f"{anomaly['type']} : {anomaly['count']}"
            )

            st.dataframe(
                anomaly["data"],
                use_container_width=True
            )

    else:

        st.success("No anomalies found")

st.divider()

# Footer
st.caption(
    "Built using Pandas, Groq LLM, and Streamlit"
)