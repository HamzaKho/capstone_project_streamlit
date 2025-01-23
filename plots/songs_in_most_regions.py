import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

def plot_songs_in_most_regions(df):
    # Count the number of unique regions where each song is popular
    song_region_counts = (
        df.groupby(['track_name', 'artist_name', 'popularity','features'])
        .agg({'region': 'nunique'})
        .reset_index()
        .sort_values(by='popularity', ascending=False)
        .head(10)
    )
    fig2 = px.bar(
        song_region_counts,
        x='region',
        y='track_name',
        color='artist_name',
        orientation='h',
        title="Songs Popular in the Most Regions",
        labels={'region': 'Number of Regions', 'track_name': 'Song Name'},
        hover_data=['artist_name', 'features']
    )
    fig2.update_layout(
        yaxis={'categoryorder':'total ascending'},
        height=600,
        width=800
    )
    return(fig2)
    #st.plotly_chart(fig2, use_container_width=True, key="songs_in_most_regions_chart")