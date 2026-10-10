def get_ai_insights(df):
    insights = []

    insights.append(f"Total rows: {df.shape[0]}")
    insights.append(f"Total columns: {df.shape[1]}")

    insights.append("\nColumn names:")
    insights.append(", ".join(df.columns))

    insights.append("\nBasic statistics:")
    insights.append(str(df.describe()))

    return "\n".join(insights)
