import streamlit as st
import pandas as pd
from create_db_connection import connect_to_db
import matplotlib.pyplot as plt
import plotly.express as px
from plots.top_songs import plot_top_songs, plot_top_songs_language
from plots.songs_in_most_regions import plot_songs_in_most_regions
from plots.uniquely_popular_songs import plot_uniquely_popular_songs
from plots.unique_songs_per_region import plot_unique_songs_per_region, plot_unique_songs_per_language
from plots.language_diversity import plot_language_diversity

#TODO: IMPROVE LAYOUTING https://docs.streamlit.io/develop/api-reference/layout

engine = connect_to_db()

df = pd.read_sql_table('hamza_capstone',engine,'student',index_col=None)

#st.title("Spotify Music Data")
st.markdown(
    """
    <div style="display: flex; align-items: center; gap: 10px;">
        <img src="https://storage.googleapis.com/pr-newsroom-wp/1/2023/05/Spotify_Primary_Logo_RGB_Green.png" alt="Spotify Logo" style="width: 50px;">
        <h1 style="margin: 0;">Spotify Music Data</h1>
    </div>
    """,
    unsafe_allow_html=True
)

with st.sidebar:
    st.header("Navigation")
    section = st.radio("Display section:", ["Top 10 Songs", "Unique Songs", "Proportions", "Diversity"])

regions = df['region'].unique()
languages = df['languages'].unique()

#Top 10 songs
if section == "Top 10 Songs":
    with st.container():
        st.subheader("Top 10 Songs")
        radio = st.radio("See top 10 songs by Language or Region?", ["Region", "Language"])
        if radio == "Region":
            selected_regions = st.multiselect("Select Region(s):", regions, default=regions[0])
            if selected_regions:
                st.plotly_chart(plot_top_songs(selected_regions, df))
        else:
            selected_languages = st.multiselect("Select Language(s):", languages, default=languages[0])
            if selected_languages:
                st.plotly_chart(plot_top_songs_language(selected_languages, df))

#Songs unique to a region
elif section == "Unique Songs":
    with st.container():
        st.subheader("Songs Unique to Selected Region")
        selected_unique_region = st.selectbox("Select a region to see songs that are ONLY popular there", regions)
        if selected_unique_region:
            st.plotly_chart(plot_uniquely_popular_songs(selected_unique_region, df))

#Proportion of unique songs in each region
elif section == "Proportions":
    with st.container():
        st.subheader("Proportion of Unique Songs in Each Region")
        st.plotly_chart(plot_unique_songs_per_region(regions, df))

#Diversity of songs in each region by language
elif section == "Diversity":
    with st.container():
        st.subheader("Diversity of Songs in Each Region by Language")
        selected_language = st.selectbox('Select a language to see the diversity of each region.', languages)
        if selected_language:
            st.plotly_chart(plot_language_diversity(selected_language, df))
