from pyvis.network import Network
import networkx as NX

g = NX.MultiDiGraph()
g.add_node("MEEI (n = 135)", size = 135, )
g.add_node("JHU (n = 49)", size = 49)
g.add_node("Michigan (n = 40)", size=40)
g.add_node("Vanderbilt (n = 43)", size=43)
g.add_node("MUSC (n = 19)", size = 19)
g.add_node("Stanford (n = 44)", size = 44)
g.add_node("UCSF (n = 36)", size = 36)
g.add_node("Ohio State (n = 25)", size = 25)
g.add_node("Iowa (n = 18)", size = 18)
g.add_node("Penn (n = 28)", size = 28)

g.add_edge("MEEI (n = 135)","MEEI (n = 135)", value=    44, title = "44")
g.add_edge("JHU (n = 49)","MEEI (n = 135)", value=    3, title ="3")
g.add_edge("Michigan (n = 40)", "MEEI (n = 135)", value=    1, title="1")
g.add_edge("MUSC (n = 19)", "MEEI (n = 135)", value=    1, title="1")
g.add_edge("Stanford (n = 44)", "MEEI (n = 135)", value=    1, title="1")
g.add_edge("UCSF (n = 36)", "MEEI (n = 135)", value=   4, title ="4")
g.add_edge("Iowa (n = 18)", "MEEI (n = 135)", value=   3, title="3")
g.add_edge("Penn (n = 28)", "MEEI (n = 135)", value=   1, title = "1")
g.add_edge("MEEI (n = 135)" ,"JHU (n = 49)", value = 4, title = "4")
g.add_edge("JHU (n = 49)"   ,   "JHU (n = 49)"  , value =  20 , title = "20" )
g.add_edge("Penn (n = 28)"  ,   "JHU (n = 49)"  , value =  2  , title = "2" )
g.add_edge("MEEI (n = 135)" ,   "Michigan (n = 40)" , value =  2 , title = "2" )
g.add_edge("JHU (n = 49)"   ,   "Michigan (n = 40)" , value =  1 , title ="1"  )
g.add_edge("Michigan (n = 40)"  ,   "Michigan (n = 40)" , value =  16 ,title="16" )
g.add_edge("Stanford (n = 44)"  ,   "Michigan (n = 40)" , value =  1  , title="1" )
g.add_edge("Iowa (n = 18)"  ,   "Michigan (n = 40)" , value =  1 , title = "1"  )
g.add_edge("Penn (n = 28)"  ,   "Michigan (n = 40)" , value =  1 , title = "1"  )
g.add_edge("MEEI (n = 135)" ,   "Vanderbilt (n = 43)"   , value =  1, title = "1"   )
g.add_edge("JHU (n = 49)"   ,   "Vanderbilt (n = 43)"   , value =  2, title = "2")
g.add_edge("Michigan (n = 40)"  ,   "Vanderbilt (n = 43)"   , value =  1, title = "1")
g.add_edge("Vanderbilt (n = 43)"    ,   "Vanderbilt (n = 43)"   , value =  9, title = "9")
g.add_edge("Ohio State (n = 25)"    ,   "Vanderbilt (n = 43)"   , value =  1, title = "1")
g.add_edge("Vanderbilt (n = 43)"    ,   "MUSC (n = 19)" , value =  1, title = "1")
g.add_edge("MUSC (n = 19)"  ,   "MUSC (n = 19)" , value =  2, title = "2")
g.add_edge("Penn (n = 28)"  ,   "MUSC (n = 19)" , value =  1, title = "1")
g.add_edge("MEEI (n = 135)" ,   "Stanford (n = 44)" , value =  1, title ="1")
g.add_edge("Michigan (n = 40)"  ,   "Stanford (n = 44)" , value =  2 , title = "2")
g.add_edge("Stanford (n = 44)"  ,   "Stanford (n = 44)" , value =  9, title = "9")
g.add_edge("UCSF (n = 36)"  ,   "Stanford (n = 44)" , value =  4 , title = "4")
g.add_edge("Iowa (n = 18)"  ,   "Stanford (n = 44)" , value =  1, title = "1")
g.add_edge("Penn (n = 28)"  ,   "Stanford (n = 44)" , value =  1, title = "1")
g.add_edge("MEEI (n = 135)" ,   "UCSF (n = 36)" , value =  1  , title = "1")
g.add_edge("JHU (n = 49)"   ,   "UCSF (n = 36)" , value =  2  , title = "2")
g.add_edge("Michigan (n = 40)"  ,   "UCSF (n = 36)" , value =  1, title = "1")
g.add_edge("Stanford (n = 44)"  ,   "UCSF (n = 36)" , value =  3 , title = "3")
g.add_edge("UCSF (n = 36)"  ,   "UCSF (n = 36)" , value =  9 , title = "9")
g.add_edge("Iowa (n = 18)"  ,   "UCSF (n = 36)" , value =  1, title = "1")
g.add_edge("MEEI (n = 135)" ,   "Ohio State (n = 25)"   , value =  1, title = "1")
g.add_edge("JHU (n = 49)"   ,   "Ohio State (n = 25)"   , value =  1, title = "1")
g.add_edge("Michigan (n = 40)"  ,   "Ohio State (n = 25)"   , value =  4, title = "4")
g.add_edge("Ohio State (n = 25)"    ,   "Ohio State (n = 25)"   , value =  9 , title = "9")
g.add_edge("Michigan (n = 40)"  ,   "Iowa (n = 18)" , value =  1 , title = "1")
g.add_edge("Iowa (n = 18)"  ,   "Iowa (n = 18)" , value =   9, title = "9")
g.add_edge("JHU (n = 49)"   ,   "Penn (n = 28)" , value =   2, title = "2")
g.add_edge("Iowa (n = 18)"  ,   "Penn (n = 28)" , value =   1, title = "1")
g.add_edge("Penn (n = 28)"  ,   "Penn (n = 28)" , value =   7, title = "7")

net = Network(height='600px', width='100%', notebook=True, directed=True)
net.from_nx(g, show_edge_weights=True)
net.set_edge_smooth("Dynamic")

net.toggle_physics(False)

net.set_options("""
var options = {
    "nodes": {
    "color": {
    "borderWidth": null,
    "borderWidthSelected": null,
    "opacity": null,
    "font": {
      "size": 16,
      "strokeWidth": 5
    },
    "size": null
  },
  "edges": {
    "color": {
      "inherit": true
    },
    "scaling": {
      "min": 1,
      "max": 20
    },
    "selfReferenceSize": 22,
    "selfReference": {
      "size": 22,
      "angle": 0.7853981633974483,
      "renderBehindTheNode": true
    },
    "smooth": {
      "type": "Dynamic",
      "forceDirection": "none"
    }
  },
  "physics": {
    "enabled": false,
    "minVelocity": 0.75
  }
}
""")
net.show('foo2.html')