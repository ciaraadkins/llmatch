# Final version of the Streamlit app with hardcoded leaderboard data
!pip install streamlit

import streamlit as st
import pandas as pd

# Sample data for the leaderboard
def create_sample_leaderboard():
    data = {
        "Name": ["Model A", "Model B", "Model C", "Model D"],
        "Score": [88.5, 92.7, 85.3, 90.1],
        "Rank": [3, 1, 4, 2]
    }
    df = pd.DataFrame(data)
    return df

# Main app
def main():
    st.title("LLMatch.ai")
    st.subheader("A Customizable LLM Leaderboard")
    
    # Create sample data
    df = create_sample_leaderboard()
    
    # Display data
    st.table(df)

# Uncomment the following line when you run this script
if __name__ == "__main__":
    main()
