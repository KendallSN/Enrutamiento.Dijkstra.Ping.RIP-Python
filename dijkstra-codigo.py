import networkx as nx
import matplotlib.pyplot as plt

# Crear el grafo de la red
G = nx.Graph()
edges = [
    ("A", "B", 4), ("A", "C", 2), ("B", "C", 5),
    ("B", "D", 10), ("C", "D", 3), ("D", "E", 8)
]
G.add_weighted_edges_from(edges)

# Calcular la ruta más corta desde "A" a "E"
shortest_path = nx.shortest_path(G, source="A", target="E", weight="weight")

# Dibujar la red
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_color="lightblue", edge_color="gray")
edge_labels = nx.get_edge_attributes(G, "weight")
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
plt.show()

print("Ruta más corta:", " → ".join(shortest_path))
