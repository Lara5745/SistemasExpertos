import networkx as nx
G=nx.Graph()
e=[('a','b',1),('b','c',2),('a','c',3),('c','d',4),('d','e',2),('b','e',1)]
G.add_weighted_edges_from(e)
print(nx.dijkstra_path(G,'a','e'))

