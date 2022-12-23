import yfinance as yf
import streamlit as st
import json
import requests
from streamlit_lottie import st_lottie
from PIL import Image

st.set_page_config(page_title="Stock Search",
                   page_icon=":trident:", layout='wide')

st.markdown('<link rel="stylesheet" type="text/css" href="styles.css">',
            unsafe_allow_html=True)

def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)

# Load Assets
lottie_buisness = load_lottiefile("/Users/ujjwalnd/Python_Projects/Animations/business-analysis.json")
img_Self_Picture = Image.open("images/ujjwal1.png")


# --- Header ---
with st.container():
    left_column, right_column = st.columns(2)
    with left_column:
        st.subheader(
        "Hello, I am Ujjwal and this is my first python project! :wave:")
        st.write("[Social Media](https://www.linkedin.com/in/ujjwal-adhikari/)")
        st.title("Stock Search")
        Stock = st.text_input("Please Input a Ticker ")
        st.write('##')
        tickerSymbol = Stock
        tickerData = yf.Ticker(tickerSymbol or 'aapl')
        info = tickerData.info
        tickerDf = tickerData.history(period='1d', start='2022-1-1', end='2022-12-13')
        st.header(Stock)
# hide and show button
        More_Info = st.button("More Info")
        text_placeholder = st.empty()
        button_placeholder = st.empty()
        if More_Info:
            text_placeholder.markdown(info['longBusinessSummary'])
    
with right_column:
    st_lottie(
    lottie_buisness,
    height=500
   
)


# --- Actual Project ---
with st.container():

   

    left_column, right_column = st.columns(2)
with left_column:
    st.header("Daily Chart")
    st.write("##")
    st.line_chart(tickerDf.Close)   
with right_column:
    st.header("Daily Volume")
    st.write("##")
    st.line_chart(tickerDf.Volume)


with st.container():
    st.write("---")
    st.header("My Other Projects")
    st.write("##")
    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image(img_Self_Picture)
    with text_column:
        st.subheader("About My Journey")
        st.write(
            """
            I was born in Nepali, grew up in North Dakota and had educational training for Software Development in Fargo. 
            I love everything surrounding the field of tech and have a deep interest in furthering my knowledge. 
            If you would like to talk about tech, a connection is more than welcome!
            """
        )
