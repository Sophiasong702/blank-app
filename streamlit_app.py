import streamlit as st
import pandas as pd
from pathlib import Path

st.title("Study Playlist Prototype")

csv_path = Path("data/raw/spotify_tracks.csv")

@st.cache_data
def load_df():
    return pd.read_csv(csv_path)

if csv_path.exists():
    df = load_df()
    st.success(f"Loaded {len(df):,} rows")
    st.dataframe(df.head(20))
else:
    st.error("CSV not found in data/raw/")

