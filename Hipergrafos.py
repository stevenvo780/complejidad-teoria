import hypernetx as hnx
import networkx as nx
import matplotlib.pyplot as plt

# Creando un sistema simple con NetworkX
simple_graph = nx.Graph()
simple_graph.add_edge('Nodo1', 'Nodo2')
simple_graph.add_edge('Nodo2', 'Nodo3')
simple_graph.add_edge('Nodo3', 'Nodo1')

# Creando un sistema ordenado como un hipergrafo con HypernetX
edges = {
    'H1': {'A1', 'A2', 'A3'},
    'H2': {'B1', 'B2', 'B3'},
    'H3': {'C1', 'C2', 'C3', 'A2', 'B2'},  # H3 ahora comparte nodos con H1 y H2
    'H12': {'A1', 'B1'}
}
ordered_hypergraph = hnx.Hypergraph(edges)

# Creando un sistema desordenado como un grafo más complejo con NetworkX
disordered_graph = nx.barabasi_albert_graph(20, 2)  # 20 nodos

# Dibujando los grafos
plt.figure(figsize=(18, 6))

# Graficando el sistema simple
plt.subplot(131)
nx.draw(simple_graph, with_labels=True, node_color='lightblue', node_size=800)
plt.title("Sistema Simple")

# Graficando el sistema ordenado como hipergrafo
plt.subplot(132)
hnx.draw(ordered_hypergraph, with_node_labels=True)
plt.title("Sistema Ordenado (Hipergrafo)")

# Graficando el sistema desordenado
plt.subplot(133)
nx.draw(disordered_graph, with_labels=True, node_color='salmon', node_size=800)
plt.title("Sistema Desordenado")

plt.tight_layout()
plt.show()
