import pandas as pd

def load_data():
    
    df = pd.read_excel("data/support_tickets.xlsx")

    df["created_at"] = pd.to_datetime(df["created_at"])

    return df
