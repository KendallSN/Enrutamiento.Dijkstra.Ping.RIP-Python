import networkx as nx
import matplotlib.pyplot as plt
import heapq

# Dijkstra
def dijkstra(graph, start, target):
    # Inicializar distancias y cola de prioridad
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    priority_queue = [(0, start)]
    previous_nodes = {node: None for node in graph}

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        # Si llegamos al nodo objetivo, terminamos
        if current_node == target:
            break

        # Explorar vecinos
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_nodes[neighbor] = current_node
                heapq.heappush(priority_queue, (distance, neighbor))

    # Reconstruir la ruta más corta
    path = []
    current = target
    while current is not None:
        path.insert(0, current)
        current = previous_nodes[current]

    return path

# Crear el grafo de la red
G = nx.Graph()
edges = [
    ("A", "B", 4), ("A", "C", 2), ("B", "C", 5),
    ("B", "D", 10), ("C", "D", 3), ("D", "E", 8)
]
G.add_weighted_edges_from(edges)

# Convertir el grafo de NetworkX a un diccionario para Dijkstra
# Un listado de nodos con sus vecinos y pesos
graph_dict = {node: {} for node in G.nodes}
for u, v, data in G.edges(data=True):
    graph_dict[u][v] = data["weight"]
    graph_dict[v][u] = data["weight"]

# Calcular la ruta más corta desde "A" a "E" con NetworkX
shortest_path_networkX = nx.shortest_path(G, source="A", target="E", weight="weight")

# Calcular la ruta más corta desde "A" a "E" con Dijkstra
shortest_path_dijkstra = dijkstra(graph_dict, "A", "E")

# Imprimir la ruta más corta
print("Ruta más corta NetworkX:", " → ".join(shortest_path_networkX))
print("Ruta más corta Dijkstra:", " → ".join(shortest_path_dijkstra))

# Dibujar la red
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_color="lightblue", edge_color="gray")
edge_labels = nx.get_edge_attributes(G, "weight")
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
plt.show()
