# pip install streamlit
# streamlit run main.py
# pip install --upgrade streamlit 
import streamlit as st

st.title("Streamlit demo application")

st.header("This is a heading for my streamlit app")

st.text("This is a demo text")

st.success("Its a success")

st.warning("This is final warning")

st.info("here's a info")

st.error("Error")

if st.checkbox("Select/Unselect"):
    st.success("You have selected the checkbox")

else:
    st.warning("Checkbox is not selected")

input_radio = st.radio("What is your favorite color ?",
                       ("Red","Blue","Green"))

st.text(f"You have selected {input_radio}")

occupation = st.selectbox("what do you do?",
                          ("Student","Data Scientist","Vlogger","Mentor","Manager"))

multi_select = st.multiselect("what do you do? - Multi Select",
                          ("Student","Data Scientist","Vlogger","Mentor","Manager"))

def welcome():
    return "This is the output form function"

if st.button("Submit"):
    st.text(welcome())

st.sidebar.header("Heading of sidebar")