import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import plotly.express as px
import joblib
import base64

#------MAIN CONTENT------ 
# Path to your PDF file
pdf_file = "/Users/alejandrovillanuevalledo/Documents/Important stuff/CV/Alejandro CVs 0524.pdf"

st.set_page_config(
    page_title= 'Alejandro Villanueva', 
    page_icon = 'imgs/IMG_1544.JPG',
    layout= 'wide') 

#------SIDEBAR SETUP--------------------------------
st.sidebar.image('imgs/IMG_2024-05-27-165202.png', width= 250)

# Centered and styled text
st.sidebar.markdown(
    """
    <div style='font-size:50px; font-weight:bold; line-height:1.0; color: #555555;'>
        ALEJANDRO<br>VILLANUEVA
    </div>
    """,
    unsafe_allow_html=True
)
st.sidebar.subheader('Data Scientist')
st.sidebar.markdown(' ')
st.sidebar.markdown(' ')

#-----------LINKEDIN ICON--------------------------------
# Define your LinkedIn link
linkedin_url = "https://www.linkedin.com/in/alelledo/"
# Sidebar content with icon and linked text
st.sidebar.markdown(
    f"""
    <div style='display: flex; align-items: center; font-size:15px;'>
        <img src='https://img.icons8.com/color/48/000000/linkedin.png' width='25' style='margin-right: 10px;'>
        <a href="{linkedin_url}" target="_blank" style='color: black; text-decoration: none;'>linkedin.com/in/alelledo</a>
    </div>
    """,
    unsafe_allow_html=True
)
#-----------EMAIL ICON--------------------------------
email_url = "mailto:villalledo@gmail.com"
st.sidebar.markdown(
    f"""
    <div style='display: flex; align-items: center; font-size:15px;'>
        <img src='https://static.vecteezy.com/system/resources/thumbnails/023/618/290/small_2x/email-icon-clipart-free-free-png.png' width='25' style='margin-right: 10px;'>
        <a href="{email_url}" target="_blank" style='color:black; text-decoration: none;'>villalledo@gmail.com</a>
    </div>
    """,
    unsafe_allow_html=True
)
#-----------GITHUB ICON--------------------------------
github_url = "https://github.com/alelledo"
st.sidebar.markdown(
    f"""
    <div style='display: flex; align-items: center; font-size:15px; margin-top: 0px;'>
        <img src='https://img.icons8.com/color/48/000000/github--v1.png' width='25' style='margin-right: 10px;'>
        <a href="{github_url}" target="_blank" style='color: black; text-decoration: none;'>github.com/alelledo</a>
    </div>
    """,
    unsafe_allow_html=True
)





#-----CONTENT------
tab1, tab2, tab3 = st.tabs(['Portfolio', 'Resume', 'About me'])


#----------------TAB1------------------------
with tab1:
#-----------------------------COLUMNS-------------------------    
    col1, col2 = st.columns(2) 
    
    
    #-------------------------COL 1------------------------
    with col1: 

#--------------------------------------ENERGY CHURN------------------------------
        # Define the URL to link to
        url = "https://energy-churn.streamlit.app/"
        
        #-------------------------CHURN IMAGE---------------------------
        # Path to your local image
        image_path = "imgs/Churn.png"

        # Read the image file
        with open(image_path, "rb") as image_file:
            encoded_image = base64.b64encode(image_file.read()).decode()

        # Display the image with a link
    
        st.markdown(
            f'<a href="{url}" target="_blank">'
            f'<img src="data:image/png;base64,{encoded_image}" alt="Linked Image" width="450">'
            f'</a>',
            unsafe_allow_html=True
        )
        
        #-------------------------------CHURN TITLE--------------------------
        # Underlined and styled text with a clickable link
        st.markdown(
            """
            <a href="https://energy-churn.streamlit.app/" target="_blank" style='font-size:25px; color:black; font-weight:bold; font-family:Segoe UI; text-decoration: none;'>
                Churn Prediction with Python
            </a>
            """,
            unsafe_allow_html=True
        )
        st.markdown(
                    """
                    <div style='color: #555555;'>
                    · Python<br>
                    · Streamlit<br>
                    · Predictive Modelling
                    </div>
                    """,
                    unsafe_allow_html=True
                )
        st.markdown(' ')
        st.markdown(' ')
        st.markdown(' ')

#-----------------------------SENTIMENT ANALYSIS------------------------------------
        # Path to your local image
        image_path = "/Users/alejandrovillanuevalledo/Documents/Important stuff/CV/streamlit CV /imgs/Conceptual Model.jpeg"

        # Read the image file
        with open(image_path, "rb") as image_file:
            encoded_image = base64.b64encode(image_file.read()).decode()

        # URL for the link
        url = "https://github.com/alelledo/Sentiment-Analysis"

        # Display the image with a link
        st.markdown(' ')
        st.markdown(
            f'<a href="{url}" target="_blank">'
            f'<img src="data:image/png;base64,{encoded_image}" alt="Linked Image" width="450">'
            f'</a>',
            unsafe_allow_html=True
        )

        #-------------------------------SENTIMENT TITLE -------------------------------
        # Display styled text
        st.markdown(
    """
    <a href="https://github.com/alelledo/Sentiment-Analysis" target="_blank" style='font-size:25px; color:black; font-weight:bold; font-family:Segoe UI; text-decoration: none;'>
        Twitter and OpenSea scrapping - NFT Sentiment Analysis
    </a>
    """,
    unsafe_allow_html=True
)
        st.markdown(
                    """
                    <div style='color: #555555;'>
                    · Python<br>
                    · R<br>
                    · Web Scrapping<br>
                    · Statistical Modelling
                    </div>
                    """,
                    unsafe_allow_html=True
                )
    #-------------------------------COL 2-------------------------------    
    with col2:
        st.markdown(' ')
        
        #------------------------------AIRBNB--------------------------------
# Path to your local image
        image_path = "/Users/alejandrovillanuevalledo/Documents/Important stuff/CV/streamlit CV /imgs/Screenshot 2024-05-27 at 16.15.08.png"

        # Read the image file
        with open(image_path, "rb") as image_file:
            encoded_image = base64.b64encode(image_file.read()).decode()

        # URL for the link
        url = "https://hong-kongproject-airbnb.streamlit.app/"

        # Display the image with a link
        st.markdown(' ')
        st.markdown(
            f'<a href="{url}" target="_blank">'
            f'<img src="data:image/png;base64,{encoded_image}" alt="Linked Image" width="450" height="250">'
            f'</a>',
            unsafe_allow_html=True
        )
        st.markdown(' ')
        st.markdown(' ')
        st.markdown(' ')
        
        
        #----------------------------AIRBNB TITLE----------------
        st.markdown(
        """
        <a href="https://hong-kongproject-airbnb.streamlit.app/" target="_blank" style='font-size:25px; color:black; font-weight:bold; font-family:Segoe UI; text-decoration: none;'>
            Airbnb Hong Kong - Data Analysis
        </a>
        """,
        unsafe_allow_html=True
        )
        st.markdown(
                    """
                    <div style='color: #555555;'>
                    · Python<br>
                    · PowerBI<br>
                    · EDA
                    </div>
                    """,
                    unsafe_allow_html=True
                )
        st.markdown(' ')
        st.markdown(' ')
        st.markdown(' ')
        st.markdown(' ')
        st.markdown(' ')
        
        
        #-------------------------YELP PROJECT------------------------------------------------
        url = 'https://github.com/alelledo/yelp_project'
        # Use Markdown to display the image with a link
        st.markdown(f'<a href="{url}" target="_blank"><img src="https://static.vecteezy.com/system/resources/previews/027/127/559/non_2x/yelp-logo-yelp-icon-transparent-free-png.png" alt="Placeholder Image" width="350"></a>', unsafe_allow_html=True)
        st.markdown(' ')
        
        #-------------------------YELP TITLE---------------------------
        st.markdown(
    """
    <a href='https://github.com/alelledo/yelp_project' target="_blank" style='font-size:25px; color:black; font-weight:bold; font-family:Segoe UI; text-decoration: none;'>
        Customer Models - An Analysis on Restaurant Choices
    </a>
    """,
    unsafe_allow_html=True
)
        st.markdown( """
    <div style='color: #555555;'>
        · R<br>
        · Data Cleanup<br>
        · Logit models
    </div>
    """,
                        unsafe_allow_html=True
                    )

    # Custom styled text with centered alignment
    st.markdown(' ')
    st.markdown(' ')
    st.markdown(' ')
    st.markdown(' ')
    st.markdown(' ')
    st.markdown(' ')
    
    st.markdown( 
        """
        <div style='font-size:30px; color:grey; font-weight:bold; font-family:Didot; text-align:center;'>
            More projects to come! 
        </div>
        """,
        unsafe_allow_html=True
    )
#------------------------------TAB 2------------------------------
with tab2:
    # Read the PDF file
    with open(pdf_file, "rb") as f:
        pdf_data = f.read()

    # Embed PDF file
    base64_pdf = base64.b64encode(pdf_data).decode('utf-8')

    # CSS to make the iframe responsive
    st.markdown(
        """
        <style>
        .pdf-container {
            width: 100%;
            height: 0;
            padding-bottom: 80%;
            position: relative;
        }
        .pdf-container iframe {
            position: absolute;
            width: 100%;
            height: 100%;
            border: none;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    # HTML to display the iframe
    pdf_display = f'<div class="pdf-container"><iframe src="data:application/pdf;base64,{base64_pdf}" type="application/pdf"></iframe></div>'

    # Display PDF
    st.markdown(pdf_display, unsafe_allow_html=True)

#------------------------------TAB 3------------------------------
with tab3:
    st.markdown('''MSc graduate in Marketing Analytics and Data Science, with a focus in data analysis, modelling and forecasting, using R, Python and SQL,
            as a basis for research-based marketing decisions. My curious nature has taken me traveling quite often, having traveled through Australia, Europe, South East Asia and South America.
            Currently, I am working on a new skill, the Dutch language, simultaneously I am also working a part-time job while I continue
            the search for my dream job.''')
    st.markdown(' ')
    st.markdown(' ')
    #-----------LINKEDIN ICON--------------------------------
    # Define your LinkedIn link
    linkedin_url = "https://www.linkedin.com/in/alelledo/"
    # Sidebar content with icon and linked text
    st.markdown(
        f"""
        <div style='display: flex; align-items: center; font-size:15px;'>
            <img src='https://img.icons8.com/color/48/000000/linkedin.png' width='30' style='margin-right: 10px;'>
            <a href="{linkedin_url}" target="_blank" style='color: black; text-decoration: none;'>linkedin.com/in/alelledo</a>
        </div>
        """,
        unsafe_allow_html=True
    )
    #-----------EMAIL ICON--------------------------------
    email_url = "mailto:villalledo@gmail.com"
    st.markdown(
        f"""
        <div style='display: flex; align-items: center; font-size:15px;'>
            <img src='https://static.vecteezy.com/system/resources/thumbnails/023/618/290/small_2x/email-icon-clipart-free-free-png.png' width='30' style='margin-right: 10px;'>
            <a href="{email_url}" target="_blank" style='color:black; text-decoration: none;'>villalledo@gmail.com</a>
        </div>
        """,
        unsafe_allow_html=True
    )
    #-----------GITHUB ICON--------------------------------
    github_url = "https://github.com/alelledo"
    st.markdown(
        f"""
        <div style='display: flex; align-items: center; font-size:15px; margin-top: 0px;'>
            <img src='https://img.icons8.com/color/48/000000/github--v1.png' width='30' style='margin-right: 10px;'>
            <a href="{github_url}" target="_blank" style='color: black; text-decoration: none;'>github.com/alelledo</a>
        </div>
        """,
        unsafe_allow_html=True
    )