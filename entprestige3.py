from optparse import Values
from pyvis.network import Network
from pyvis.network import Network
net = Network(height='80%', width='80%')
import pandas as pd
import networkx as nx
import streamlit as st
import streamlit.components.v1 as components

st.title("Network Visualization of Top 10 ENT Programs")

data = pd.read_csv('~/Users/coopermunhall/Desktop/prestigedata.csv')

sources = data['source']
targets = data['target']
weights = data['weight']
size = data['audience.size']
label = data['label']

edge_data = zip(sources, targets, weights, size)

for e in edge_data:
    src = e[0]
    dst = e [1] 
    w = e[2]
    asize = e[3]

    net.add_node(src, src, value=asize, title=src)
    net.add_node(dst, dst, value=asize, title=dst)
    net.add_edge(src, dst, value=w)


net.show_buttons(filter_=True)
net.show('testentgraph.html')
