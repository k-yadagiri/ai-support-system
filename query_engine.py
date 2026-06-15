from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


def ask_question(df, question):

    question = question.lower()

    # Total tickets
    if "how many tickets" in question:
        return f"Total Tickets: {len(df)}"

    # Open tickets
    elif "open tickets" in question:
        count = len(df[df["status"] == "Open"])
        return f"Open Tickets: {count}"

    # Resolved tickets
    elif "resolved tickets" in question:
        count = len(df[df["status"] == "Resolved"])
        return f"Resolved Tickets: {count}"

    # Escalated tickets
    elif "escalated tickets" in question:
        count = len(df[df["status"] == "Escalated"])
        return f"Escalated Tickets: {count}"

    # Lowest Rated Agent
    elif (
        "lowest average customer rating" in question
        or "lowest rated agent" in question
    ):

        agent_ratings = (
            df.groupby("agent_id")["customer_rating"]
            .mean()
            .dropna()
        )

        agent = agent_ratings.idxmin()
        rating = agent_ratings.min()

        return (
            f"{agent} has the lowest average customer "
            f"rating of {round(rating, 2)}"
        )

    # Average Customer Rating
    elif "average customer rating" in question:

        rating = round(
            df["customer_rating"].mean(),
            2
        )

        return f"Average Customer Rating: {rating}"

    # Agent Resolved Most Tickets
    elif (
        "most tickets" in question
        or "resolved the most" in question
        or "top agent" in question
    ):

        resolved_counts = (
            df[df["status"] == "Resolved"]
            .groupby("agent_id")
            .size()
            .sort_values(ascending=False)
        )

        agent = resolved_counts.index[0]
        count = resolved_counts.iloc[0]

        return f"{agent} resolved the most tickets ({count})"

    # Average Resolution Time
    elif (
        "average resolution time" in question
        or "avg resolution time" in question
    ):

        avg_time = round(
            df["resolution_time_hrs"].mean(),
            2
        )

        return f"Average Resolution Time: {avg_time} hours"

    # Critical Unresolved Tickets
    elif (
        "critical" in question
        and (
            "unresolved" in question
            or "not resolved" in question
        )
    ):

        count = len(
            df[
                (df["priority"] == "Critical")
                &
                (df["status"] != "Resolved")
            ]
        )

        return f"Unresolved Critical Tickets: {count}"

    # Priority Distribution
    elif "priority" in question:

        priority_counts = (
            df["priority"]
            .value_counts()
            .to_dict()
        )

        return str(priority_counts)

    # Fallback to Groq
    else:

        prompt = f"""
You are a support ticket analyst.

Dataset Columns:
ticket_id
created_at
category
priority
status
response_time_hrs
resolution_time_hrs
agent_id
customer_rating
issue_summary

User Question:
{question}

Answer professionally and concisely.
"""

        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return response.choices[0].message.content