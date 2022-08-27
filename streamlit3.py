import streamlit as st
import streamlit.components.v1 as components
import networkx as nx
import matplotlib.pyplot as plt
from pyvis.network import Network
import entprestige3

st.title("Network Visualization of ENT Programs #1-10")

st.sidebar.title('Programs #1-10 Network Graph')
option=st.sidebar.selectbox('select graph',('Programs #1-10 Network Graph'))
physics=st.sidebar.checkbox('add physics interactivity?')
entprestige3.simple_func(physics)

if option=='Programs #1-10 Network Graph':
  HtmlFile = open("testentgraph.html", 'r', encoding='utf-8')
  source_code = HtmlFile.read() 
  components.html(source_code, height = 900,width=900)