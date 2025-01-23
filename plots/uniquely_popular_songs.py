import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

def plot_uniquely_popular_songs(selected_unique_region, df):
    #Songs that are popular in ONLY the selected region
    filtered_df = df.drop_duplicates(subset='track_name',keep=False)
    filtered_df = filtered_df[filtered_df['region'] == selected_unique_region]
    #st.write(filtered_df)
    fig3 = px.bar(
        filtered_df,
        x='popularity',
        y='track_name',
        color='artist_name',
        orientation='h',
        title="Songs Popular in Only the Selected Region",
        labels={'popularity': 'Popularity', 'track_name': 'Song Name'},
        hover_data=['artist_name']        
    )
    fig3.update_layout(
        yaxis={'categoryorder':'total ascending'},
        height=600,
        width=800
    )
    return(fig3)
    #st.plotly_chart(fig3, key="unique_popular_songs_chart")