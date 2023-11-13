import networkx as nx
import matplotlib.pyplot as plt

# Creando un sistema simple
simple_graph = nx.Graph()
simple_graph.add_edge('Nodo1', 'Nodo2')

# Creando un sistema ordenado con hipergrafos
ordered_graph = nx.Graph()
# Agregando nodos y aristas para el primer subconjunto
ordered_graph.add_edges_from([('A1', 'A2'), ('A2', 'A3'), ('A3', 'A1')])
# Agregando nodos y aristas para el segundo subconjunto
ordered_graph.add_edges_from([('B1', 'B2'), ('B2', 'B3'), ('B3', 'B1')])
# Conexión mínima entre los subconjuntos
ordered_graph.add_edge('A1', 'B1')

# Creando un sistema desordenado con el modelo Barabási-Albert
disordered_graph = nx.barabasi_albert_graph(10, 2)  # 10 nodos, cada nuevo nodo se adjunta a 2 nodos existentes

# Dibujando los grafos
plt.figure(figsize=(15, 5))

# Graficando el sistema simple
plt.subplot(131)
nx.draw(simple_graph, with_labels=True, node_color='lightblue', node_size=800)
plt.title("Sistema Simple")

# Graficando el sistema ordenado
plt.subplot(132)
nx.draw(ordered_graph, with_labels=True, node_color='lightgreen', node_size=800)
plt.title("Sistema Ordenado")

# Graficando el sistema desordenado (reajustado)
plt.subplot(133)
nx.draw(disordered_graph, with_labels=True, node_color='salmon', node_size=800)
plt.title("Sistema Desordenado")

plt.show()
