import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
#pie chart showing regions with the most unique popular songs
def plot_unique_songs_per_region(regions, df):
    region_unique_count = {}
    for region in regions:
        if region != 'Global': 
            unique_df = df.drop_duplicates(subset="track_name",keep=False)
            unique_df = unique_df[unique_df['region'] == region]
            region_unique_count[region] = len(unique_df)
    fig4 = px.pie(values = region_unique_count.values(), names=region_unique_count.keys())
    return(fig4)
    #st.plotly_chart(fig4, key="unique_songs_per_region_pie")

def plot_unique_songs_per_language(languages, df):
    language_unique_count ={}
    for language in languages:
        unique_df = df.drop_duplicates(subset="track_name",keep=False)
        unique_df = unique_df[unique_df['languages'] == language]
        language_unique_count[language] = len(unique_df)
    fig4 = px.pie(values=language_unique_count.values(), names=language_unique_count.keys())
    return(fig4)