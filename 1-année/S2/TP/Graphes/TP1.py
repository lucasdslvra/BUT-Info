import networkx as nx
import matplotlib.pyplot as plt
from numpy import *
import numpy as np
import graphviz 

G = nx.Graph()

G.add_node(1)
G.add_nodes_from([2,3,4])

G.add_edge(1,2)
G.add_edges_from([(1,3),(1,4),(2,3)])
G.add_edge(1,5)

# nx.draw(G, with_labels=True, node_color='yellow')
# plt.show()  

# print(G.nodes())

# print(G.number_of_nodes())

# print(G.degree(1))

degrees = G.degree()

# print(sum(dict(degrees).values())/ G.number_of_nodes())


A = nx.random_regular_graph(2, 10)


def regulier(G):
    degrees = G.degree()
    for i in degrees:
        if i[1] != 2:
            return False
    return True

def regulier(A):
    degrees = A.degree()
    for i in degrees:
        if i[1] != 2:
            return False
    return True

def regulier(B):
    degrees = B.degree()
    for i in degrees:
        if i[1] != 2:
            return False
    return True


# print(regulier(G))
# print(regulier(A))

# print(A)

# print(A.edges())

# print(A.number_of_edges())

# print(nx.diameter(A))


B = nx.Graph()
B.add_nodes_from([1,2,3,4,5,6])
B.add_edges_from([(1,2),(1,5),(1,4),(2,3),(2,5),(2,4),(3,6),(3,4),(3,5),(4,5),(4,6)])
# nx.draw(B, with_labels=True, node_color='yellow')
# plt.show()

def stats():
    print("Nombre de noeuds : ", B.number_of_nodes())
    print("Nombre d'arêtes : ", B.number_of_edges())
    print("Degré moyen : ", sum(dict(B.degree()).values())/ B.number_of_nodes())
    print("Diamètre : ", nx.diameter(B))
    print("Graph régulier : ",regulier(B))

# stats()

# print("=====G======")
# print(nx.adjacency_matrix(G).toarray())
# print("=====A======")
# print(nx.adjacency_matrix(A).toarray())
# print("=====B======")
# print(nx.adjacency_matrix(B).toarray())



# print(from_matrice())
# print(from_dict())

#Exemple commande SET

# s=set([1,2,3])
# s.remove(3)

# if 1 in s:
#     print(True);
# else:
#     print(False);

# s.add(5)
# print(s)

# for k in set([1, 2]):
#      print(k)

# s1 = {1, 2, 3}
# s2 = {2, 3, 4}

# print(s1.intersection(s2))
# print(s1.union(s2))


#Matrice d'adjacence, liste d'adjacence

def from_matrix(M):
    C = nx.Graph()
    for i in range(len(M)-1):
        for j in range(i,len(M)):
            if M[i,j]:
                C.add_edge(i,j)
    return C

def from_dict(dico):
    C = nx.Graph()
    for i in dico:
        for j in dico[i]:
            C.add_edge(i,j)
    return C

adj_matrix_np = np.array([[0, 1, 1, 0],
                          [1, 0, 1, 1],
                          [1, 1, 0, 1],
                          [0, 1, 1, 0]])

C = nx.Graph(adj_matrix_np)
# nx.draw(C, with_labels=True, node_color='yellow')
# plt.show()

adj_list = {0: [1, 2],
            1: [0, 2, 3],
            2: [0, 1, 3],
            3: [1, 2]}
C = nx.from_dict_of_lists(adj_list)

# nx.draw(C, with_labels=True, node_color='yellow')
# plt.show()

G = nx.DiGraph(np.array([[0, 1, 0, 1], [1, 0, 0, 1], [1, 1, 
0, 0], [1, 1, 0, 0]]))
# nx.draw(G, with_labels=True, node_color='yellow')
# plt.show()

G = nx.Graph({0: [1, 2], 1: [0, 2, 3], 2: [0, 1, 3], 3: [1, 
2]})
# nx.draw(G, with_labels=True, node_color='yellow')
# plt.show()


#Verifier le lem

# print(len([i for i in G.nodes() if G.degree(i)%2 == 1])%2 == 0)

# print(sum([B.degree(i) for i in B.nodes()]) == 2*B.number_of_edges())


node_color = ['red', 'blue', 'blue', 'blue']
# pos = nx.circular_layout(G)
pos = nx.kamada_kawai_layout(G)
# pos = nx.planar_layout(G)
# pos = nx.random_layout(G)
# pos = nx.spectral_layout(G)
# pos = nx.spring_layout(G)
# pos = nx.shell_layout(G)

# nx.draw(G, pos,node_color=node_color, with_labels=True)
# nx.draw_networkx_edge_labels(G,pos,edge_labels={(1,2):'1',(1,3):'2'})
# plt.show()


E = nx.DiGraph()
color = ['Yellow','Green','Blue','Red','Orange']
options = {
    'node_color': color,
    'node_size': 7000,
    'width': 2
}
E.add_nodes_from(["Tokyo","San Francisco","Singapour","Copenhague","Riga"])
E.add_edges_from([("Riga","San Francisco"),("Riga","Copenhague"),("Copenhague","Singapour"),("Singapour","San Francisco"),("Singapour","Tokyo"),("San Francisco","Tokyo"),("San Francisco","Singapour")])
pos = nx.circular_layout(E)
# nx.draw(E,pos, with_labels=True, **options)
# plt.show()

B = nx.Graph()
B.add_nodes_from([0,1,2,3,4,5,6,7,8,9,10,11])
B.add_edges_from([(0,1),(0,2),(1,4),(1,3),(2,5),(2,6)])



# ====== Affichage des graphes "GraphViz"

