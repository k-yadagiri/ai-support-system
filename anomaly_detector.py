def detect_anomalies(df):

    anomalies = []

    # Long Resolution Time
    long_resolution = df[
        df["resolution_time_hrs"]
        >
        df["resolution_time_hrs"].mean()
        +
        (2 * df["resolution_time_hrs"].std())
    ]

    if not long_resolution.empty:

        anomalies.append(
            {
                "type": "Long Resolution Time",
                "count": len(long_resolution),
                "data": long_resolution
            }
        )

    # Unresolved Critical Tickets
    unresolved_critical = df[
        (df["priority"] == "Critical")
        &
        (df["status"] != "Resolved")
    ]

    if not unresolved_critical.empty:

        anomalies.append(
            {
                "type": "Unresolved Critical Tickets",
                "count": len(unresolved_critical),
                "data": unresolved_critical
            }
        )

    return anomalies