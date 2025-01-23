import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

def plot_language_diversity(selected_language, df):
    filtered_df = df[df['languages']==selected_language]
    filtered_df = filtered_df.drop_duplicates(subset="track_name",keep=False)
    regions = filtered_df['region'].unique()
    region_unique_count = {}
    for region in regions:
        region_unique_count[region] = len(filtered_df[filtered_df['region'] == region])
    fig = px.pie(values= region_unique_count.values(), names=region_unique_count.keys())
    return fig
    