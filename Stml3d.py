# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 12:16:34 2025

@author: user
"""

import streamlit as st
import pandas as pd
import numpy as np

# Set page title
st.set_page_config(page_title="Researcher Profile", layout="wide")

# Sidebar Menu
st.sidebar.title("Navigation")
menu = st.sidebar.radio(
    "Go to:",
    ["Researcher Profile", "Publications", "Career Profile", "Contact"],
)


name = "Dr. V A Uzor"

# Sections based on menu selection
if menu == "Researcher Profile":
    st.title("Researcher Profile")
    st.sidebar.header("Profile Options")

    # Collect basic information
    field = "Mathematics"
    institution = "University of KwaZulu-Natal"
   
    # Display basic profile information
    st.write(f"**Name:** {name}")
    st.write(f"**Field of Research:** {field}")
    st.write(f"**Institution:** {institution}")

    st.image('download.png', width=200)

elif menu == "Publications":
    st.title("Publications")
    st.sidebar.header("Upload and Filter")

    # Upload publications file
    uploaded_file = st.file_uploader("Upload List of Publications",  type=["pdf", "png", "jpg", "jpeg", "docx", "csv"])
    if uploaded_file:
        publications = pd.read_csv(uploaded_file)
        st.dataframe(publications)

        # Add filtering for year or keyword
        keyword = st.text_input("Filter by keyword", "")
        if keyword:
            filtered = publications[
                publications.apply(lambda row: keyword.lower() in row.astype(str).str.lower().values, axis=1)
            ]
            st.write(f"Filtered Results for '{keyword}':")
            st.dataframe(filtered)
        else:
            st.write("Showing all publications")

        # Publication trends
        if "Year" in publications.columns:
            st.subheader("Publication Trends")
            year_counts = publications["Year"].value_counts().sort_index()
            st.bar_chart(year_counts)
        else:
            st.write("The CSV does not have a 'Year' column to visualize trends.")

elif menu == "Career Profile":
    st.title("Career Profile")
    st.sidebar.header("Choose Category")

    # Tabbed view for Career Profile
    data_option = st.sidebar.selectbox(
        "Choose a category to explore", 
        ["Education History", "Job History", "Awards & Honours"]
    )

    if data_option == "Education History":
        st.write("### Education History")

    elif data_option == "Job History":
        st.write("### Job History")

    elif data_option == "Awards & Honours":
        st.write("Award & Honours")
        
elif menu == "Contact":
    # Add a contact section
    st.header("Contact Information")
    email = "uvictor.maths@gmail.com"
    st.write(f"You can reach {name} at {email}, Thank You!")
