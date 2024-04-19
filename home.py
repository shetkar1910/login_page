import pyrebase
import streamlit as st
from datetime import datetime

from streamlit_lottie import st_lottie
import requests

firebaseConfig = {
  'apiKey': "AIzaSyCy-P-EOmkf3jC3F27dDV9Hy9El_oiMccQ",
  'authDomain': "mscproj-69276.firebaseapp.com",
  'projectId': "mscproj-69276",
  'databaseURL':"https://mscproj-69276-default-rtdb.firebaseio.com/",
  'storageBucket': "mscproj-69276.appspot.com",
  'messagingSenderId': "151553242033",
  'appId': "1:151553242033:web:beada06204cfe96db38390",
  'measurementId': "G-V2YY28GSNC"
}

# firebase authenticaton
firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()

# database
db = firebase.database()
storage = firebase.auth()

# home page

# page config

st.set_page_config(page_title="DataMindML", page_icon=":bar_chart:")

def load_lottieurl(url):
     r = requests.get(url)
     if r.status_code != 200:
          return None
     return r.json()

# lottie files

lottie_coding = "https://lottie.host/8029ec34-1b23-4cb8-9b03-687428140794/COOgRbXSWX.json"

lottie_login = "https://lottie.host/384d529f-d3a1-4326-a536-e3fbd95aa57e/snPPAt16yx.json"

st.subheader("DataMindML 📊📈📉")
st.write("Unlock the Power of Your Data ...")
st.write("---")
st.info("DataMindML is your ultimate companion for data analysis, visualization, and prediction. ")
st.info("Whether you're a data enthusiast, a business analyst, or a machine learning enthusiast, DataMindML empowers you to explore ⚡, analyze 📊, and derive insights 👁‍🗨 from your data like never before.")

st.write("---")

# Set the background color to light green
# st.markdown(
#     """
#     <style>
#     .horizontal-card {
#         background-color: #d4f2d4; /* Light green */
#         padding: 20px;
#         border-radius: 10px;
#         box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
#     }
#     </style>
#     """,
#     unsafe_allow_html=True
# )

# Define your app description
# app_description = """
# 📊📉 Unlock the Power of Your Data ...
# <br><br>
# DataMindML is your ultimate companion for data analysis, visualization, and prediction. 
# <br><br>
# Whether you're a data enthusiast, a business analyst, or a machine learning enthusiast, DataMindML empowers you to explore ⚡, analyze 📊, and derive insights 👁‍🗨 from your data like never before.

# """

# # Display the horizontal card with your app description
# st.markdown(
#     f'<div class="horizontal-card">{app_description}</div>',
#     unsafe_allow_html=True
# )


# ---------------------------------------side bar--------------------------------------------
with st.sidebar:
    with st.container():
        st_lottie(lottie_login, height= 180)

# st.sidebar.title("Welcome...")

# authentication

choice = st.sidebar.selectbox('login/Signup',['Login','Sign Up'])

email = st.sidebar.text_input('Enter email')
password = st.sidebar.text_input('Enter Password', type='password')


if choice == 'Sign Up':
    handle = st.sidebar.text_input("Please enter your app handle name", value='Default')
    submit = st.sidebar.button('Create my Account')

    if submit:
        user = auth.create_user_with_email_and_password(email,password)
        st.success('Your account is Created Successfully!')
        # st.balloons()

        #Sign In
        user = auth.sign_in_with_email_and_password(email,password)
        db.child(user['localId']).child("Handle").set(handle)
        db.child(user['localId']).child("ID").set(user['localId'])
        st.title('Welcome' + handle)
        st.info('Login via login dropdown')

if choice == "Login":
    login = st.sidebar.button('Login')
    if login:
        user = auth.sign_in_with_email_and_password(email,password)

        # st.balloons()
        
        with st.container():
                left_column, right_column = st.columns(2)
                with left_column:
                    
                    st.subheader(" A Generalized Machine Learning Application")

                    # st.write("Start Anlyzing Your Data...")
                    st.info('''
                        1. Add your Dataset that you want to Analyze.
                        2. Apply Data Preprocessing.
                        3. Build Charts and graphs.
                        4. Build Machine Learning Model.''')

                    st.link_button("Start", "https://datamindml-bkqznfku7viakrsfzjuc8d.streamlit.app/")

                with right_column:
                     st_lottie(lottie_coding, height=300, key="coding")
                     



        
        

        

        



