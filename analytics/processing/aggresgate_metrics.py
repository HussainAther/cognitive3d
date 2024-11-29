import pandas as pd

def aggregate_metrics(raw_data):
    df = pd.DataFrame(raw_data)
    summary = df.groupby('event_type').agg({'duration': 'mean', 'count': 'sum'})
    return summary

