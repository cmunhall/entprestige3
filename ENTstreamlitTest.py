import streamlit as st
import streamlit.components.v1 as components

st.title("Network Visualization of ENT Programs #1-10")

st.sidebar.title('Programs #1-10')
option=st.sidebar.selectbox('select graph',('Programs #1-10 Network Graph',"None"))

if option=='Programs #1-10 Network Graph':
  HtmlFile = open("foo2.html", 'r', encoding='utf-8')
  source_code = HtmlFile.read() 
  components.html(source_code, height = 1000,width=1000)