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

st.title("Spotify Music Data")

regions = df['region'].unique()
languages = df['languages'].unique()

st.subheader("Top 10 songs")
radio = st.radio("See top 10 songs by Language or Region?",["Region","Language"] )
#st.write("Choose Region(s) to see the top 10 most popular songs!")
if radio == "Region":
    selected_regions = st.multiselect("Select Region(s):", regions, default=regions[0])
    if selected_regions: 
        st.plotly_chart(plot_top_songs(selected_regions, df))
else:
    selected_languages = st.multiselect("Select Language(s):",languages,default=languages[0])
    if selected_languages:
        st.plotly_chart(plot_top_songs_language(selected_languages, df))


#Songs unique to selected region
st.subheader("Select a region to see songs that are ONLY popular there")
selected_unique_region = st.selectbox("",regions)
if selected_unique_region:
    st.plotly_chart(plot_uniquely_popular_songs(selected_unique_region, df))

#st.write("Songs that are popular in the most regions:")
#st.plotly_chart(plot_songs_in_most_regions(df))

# radio2 = st.radio("Group by language or by region?",["Region","Language"] )
# if radio2 == "Region":
#     st.plotly_chart(plot_unique_songs_per_region(regions, df))
# else:
#    st.plotly_chart(plot_unique_songs_per_language(languages, df))

st.subheader("Proportion of unique songs in each region")
st.plotly_chart(plot_unique_songs_per_region(regions, df))

st.subheader("Diversity of songs in each region by language")
selected_language = st.selectbox('Select a language to see the diversity of each region.', languages)
if selected_language:
    st.plotly_chart(plot_language_diversity(selected_language, df))