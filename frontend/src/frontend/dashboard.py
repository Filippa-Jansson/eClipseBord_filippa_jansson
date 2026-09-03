import streamlit as st
import httpx
import pandas as pd

BASE_URL = "http://127.0.0.1:8000"

def main():
    st.markdown("# Dashboard")

    lunar_response = httpx.get(f"{BASE_URL}/lunar/data")
    solar_response = httpx.get(f"{BASE_URL}/solar/data")

    lunar_df = pd.DataFrame(lunar_response.json())
    solar_df = pd.DataFrame(solar_response.json())

    st.markdown("## Lunar data")
    st.dataframe(lunar_df)

    st.markdown("## Solar data")
    st.dataframe(solar_df)

if __name__ == "__main__":
    main()