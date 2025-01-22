import streamlit as st
import pandas as pd
from create_db_connection import connect_to_db
import matplotlib.pyplot as plt
import plotly.express as px


engine = connect_to_db()

df = pd.read_sql_table('hamza_capstone',engine,'student',index_col=None)

st.title("Spotify Music Data")

def plot_top_songs():
    filtered_df = df[df['region'].isin(selected_regions)]
    #st.write(filtered_df)
    top_songs = (
        filtered_df.groupby(['track_name', 'artist_name'])
        .agg({'popularity': 'sum'})
        .reset_index()
        .sort_values(by='popularity', ascending=False)
        .head(10)
    )
    fig = px.bar(
        top_songs,
        x='popularity',
        y='track_name',
        color='artist_name',
        orientation='h',
        title=f"Top 10 Songs in Selected Region(s): {', '.join(selected_regions)}",
        labels={'popularity': 'Popularity', 'track_name': 'Song Name'},
        hover_data=['artist_name']
    )
    fig.update_layout(
        yaxis=dict(autorange="reversed"),
        height=600,
        width=800
    )
    st.plotly_chart(fig, use_container_width=True)
    #st.write(top_songs)

def plot_songs_in_most_regions():
    # Count the number of unique regions where each song is popular
    song_region_counts = (
        df.groupby(['track_name', 'artist_name'])
        .agg({'region': 'nunique'})
        .reset_index()
        .query(f'region=={selected_regions}')
        .sort_values(by='popularity', ascending=False)
        .head(10)
    )
    fig = px.bar(
        song_region_counts,
        x='region',
        y='track_name',
        color='artist_name',
        orientation='h',
        title="Songs Popular in the Most Regions",
        labels={'region': 'Number of Regions', 'track_name': 'Song Name'},
        hover_data=['artist_name']
    )
    fig.update_layout(
        yaxis=dict(autorange="reversed"),
        height=600,
        width=800
    )
    st.plotly_chart(fig, use_container_width=True)

def plot_uniquely_popular_songs():
    #Songs that are popular in ONLY the selected region
    filtered_df = df.drop_duplicates(subset='track_name',keep=False)
    filtered_df = filtered_df[filtered_df['region'] == selected_unique_region]
    #st.write(filtered_df)
    fig2 = px.bar(
        filtered_df,
        x='popularity',
        y='track_name',
        color='artist_name',
        orientation='h',
        title="Songs Popular in Only the Selected Region",
        labels={'popularity': 'Popularity', 'track_name': 'Song Name'},
        hover_data=['artist_name']        
    )
    fig2.update_layout(
        yaxis={'categoryorder':'total ascending'},
        height=600,
        width=800
    )
    st.plotly_chart(fig2)

regions = df['region'].unique()
#regions.put(5, "All")
st.write("Choose Region(s) to see the top 10 most popular songs!")
selected_regions = st.multiselect("Select Region(s):", regions, default=regions[0])

if selected_regions: 
    plot_top_songs()

selected_unique_region = st.selectbox("Select a region to see songs that are ONLY popular there", regions)
if selected_unique_region:
    plot_uniquely_popular_songs()
#st.write("Songs that are popular in the most regions:")
#plot_songs_in_most_regions()