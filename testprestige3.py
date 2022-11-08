from pyvis.network import Network
net = Network(height='400px', width='100%')
import pandas as pd

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

net.show_buttons(filter_=['physics', 'nodes', 'edges'])
net.show('fakegraph.html')
