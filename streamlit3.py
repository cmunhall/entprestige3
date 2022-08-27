import streamlit as st
import streamlit.components.v1 as components
import networkx as nx
from pyvis.network import Network
import entprestige3

st.title("Network Visualization of ENT Programs #1-10")

st.sidebar.title('Programs #1-10 Network Graph')
option=st.sidebar.selectbox('select graph',('Programs #1-10 Network Graph',"nothing"))

if option=='Programs #1-10 Network Graph':
  HtmlFile = open("testentgraph.html", 'r', encoding='utf-8')
  source_code = HtmlFile.read() 
  components.html(source_code, height = 1500,width=1500)