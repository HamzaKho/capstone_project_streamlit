import streamlit as st
import pandas as pd
from create_db_connection import connect_to_db
import matplotlib.pyplot as plt
import plotly.express as px
from plots.top_songs import plot_top_songs
from plots.songs_in_most_regions import plot_songs_in_most_regions
from plots.uniquely_popular_songs import plot_uniquely_popular_songs
from plots.unique_songs_per_region import plot_unique_songs_per_region

engine = connect_to_db()

df = pd.read_sql_table('hamza_capstone',engine,'student',index_col=None)

st.title("Spotify Music Data")

regions = df['region'].unique()
st.write("Choose Region(s) to see the top 10 most popular songs!")
selected_regions = st.multiselect("Select Region(s):", regions, default=regions[0])
if selected_regions: 
    st.plotly_chart(plot_top_songs(selected_regions, df))

#Songs unique to selected region
selected_unique_region = st.selectbox("Select a region to see songs that are ONLY popular there", regions)
if selected_unique_region:
    st.plotly_chart(plot_uniquely_popular_songs(selected_unique_region, df))

#st.write("Songs that are popular in the most regions:")
#plot_songs_in_most_regions()

st.write("Proportion of unique songs per region")
st.plotly_chart(plot_unique_songs_per_region(regions, df))

