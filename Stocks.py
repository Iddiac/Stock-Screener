import yfinance as yf
import streamlit as st
import json
import requests
from streamlit_lottie import st_lottie
from PIL import Image

# use Local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style> {f.read()}</style>", unsafe_allow_html=True)

st.set_page_config(page_title="Stock Search",
                   page_icon=":trident:", layout='wide')
local_css("styles.css")

st.markdown('<link rel="stylesheet" type="text/css" href="styles.css">',
            unsafe_allow_html=True)

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Load Assets
lottie_hello = load_lottieurl("https://assets9.lottiefiles.com/packages/lf20_M9p23l.json")
image = "https://media.licdn.com/dms/image/C5603AQGaD256jfoP7w/profile-displayphoto-shrink_800_800/0/1651877185940?e=1677715200&v=beta&t=La_yb77ZOkayHklRzbfZPagftatCxn1FFkIyQDUxEkI"





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
        st.header(Stock or "AAPL")
    
with right_column:
    st_lottie(
    lottie_hello,
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
    image_column, text_column = st.columns((1,2))
    with image_column:
       st.image(image, width=250)
    with text_column:
        st.subheader("About My Journey")
        st.write(
            """
            I was born in Nepali, grew up in North Dakota and had educational training for Software Development in Fargo. 
            I love everything surrounding the field of tech and have a deep interest in furthering my knowledge. 
            If you would like to talk about tech, a connection is more than welcome!
            """
        )

with st.container():
    st.write("---")
    st.header("Get In Touch With Me")
    st.write("##")

    contact_form = """
    <form action="https://formsubmit.co/ujjwaladhikari.code@gmail.com" method="POST">
    <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder="Your Name" required>
     <input type="email" name="email" placeholder= "Your Email" required>
     <textarea type="text" name="Message" placeholder="Your message here!"  required> </textarea>
     <button type="submit">Send</button>
    </form>
    """
    left_column,right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()


    # comment so it
