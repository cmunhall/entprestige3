from pyvis.network import Network
from pyvis.network import Network
net = Network(height='600px', width='100%')
import pandas as pd
import networkx as nx
import streamlit as st
import streamlit.components.v1 as components

data = pd.read_csv("https://raw.githubusercontent.com/cmunhall/entprestige3/master/prestigedata.csv")

print(data)

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

    net.add_node(src, src, value=asize, color="#7EADE6", title=src)
    net.add_node(dst, dst, value=asize, color="#7EADE6", title=dst)
    net.add_edge(src, dst, color="#7EADE6", value=w)

net.set_options("""
const options = {
  "nodes": {
    "borderWidth": null,
    "borderWidthSelected": null,
    "opacity": null,
    "font": {
      "strokeWidth": 3
    },
    "size": null
  },
  "edges": {
    "arrows": {
      "to": {
        "enabled": true,
        "scaleFactor": 0.35
      }
    },
    "color": {
      "inherit": true
    },
    "selfReferenceSize": 17,
    "selfReference": {
      "size": 15,
      "angle": 0.7853981633974483
    },
    "smooth": {
      "forceDirection": "none"
    }
  },
  "interaction": {
    "dragNodes": false,
    "navigationButtons": true
  },
  "physics": {
    "barnesHut": {
      "gravitationalConstant": -6400,
      "avoidOverlap": 0.2
    },
    "minVelocity": 0.75
  }
}
""")

net.show('testentgraph.html')