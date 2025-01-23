import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

def plot_top_songs(selected_regions, df):
    filtered_df = df[df['region'].isin(selected_regions)]
    #st.write(filtered_df)
    top_songs = (
        filtered_df.groupby(['track_name', 'artist_name','region'])
        .agg({'popularity': 'sum'})
        .reset_index()
        .sort_values(by='popularity', ascending=False)
        .head(10)
    )
    colour = 'artist_name'
    if len(selected_regions) > 1:
        colour = 'region'
    fig = px.bar(
        top_songs,
        x='popularity',
        y='track_name',
        color=colour,
        color_discrete_sequence=px.colors.qualitative.Plotly,
        orientation='h',
        title=f"Top 10 Songs in Selected Region(s): {', '.join(selected_regions)}",
        labels={'popularity': 'Popularity', 'track_name': 'Song Name'},
        hover_data=['artist_name']
    )
    fig.update_layout(
        yaxis={'categoryorder':'total ascending'},
        height=600,
        width=800
    )
    return(fig)

def plot_top_songs_language(selected_languages, df):
    filtered_df = df[df['languages'].isin(selected_languages)]
    
    top_songs = (
        filtered_df.groupby(['track_name', 'region','languages','artist_name'])
        .agg({'popularity': 'sum'})
        .reset_index()
        .sort_values(by='popularity', ascending=False)
        .head(10)
    )
    colour = "region"
    if len(selected_languages)>1:
        colour = "languages"
    fig = px.bar(
        top_songs,
        x="popularity",
        y="track_name",
        color=colour,
        orientation="h",
        title=f"Top 10 Songs in Selected Language(s): {', '.join(selected_languages)}",
        labels={'popularity': 'Popularity', 'track_name': 'Song Name'},
        hover_data=['artist_name']
    )
    fig.update_layout(
        yaxis={'categoryorder':'total ascending'},
        height=600,
        width=800
    )
    return(fig)