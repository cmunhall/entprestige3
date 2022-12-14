from pyvis.network import Network
net = Network(height='650px', width='100%', directed=True)
net.set_edge_smooth("dynamic")
import pandas as pd
import networkx as NX

data = pd.read_csv("~/Desktop/entprestige3-1/testdata.csv")

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

    net.add_node(src, src, value = asize, color="#7EADE6", title=src)
    net.add_node(dst, dst, value = asize, color="#7EADE6", title=dst)
    net.add_edge(src, dst, color="#7EADE6", value=w, title=w)
    net.add_edge(dst, src, color="#7EADE6", value=w, title=w)

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
    "navigationButtons": true
  },
  "physics": {
    "enabled": false,
    "barnesHut": {
      "theta": 0.45,
      "gravitationalConstant": -6500,
      "centralGravity": 0,
      "springLength": 315,
      "springConstant": 0.17,
      "damping": 0.74,
      "avoidOverlap": 0.2
    },
    "maxVelocity": 51,
    "minVelocity": 10,
    "timestep": 0.49
  }
}
""")


net.show('fakegraph.html')