import random
import csv
import time
import os
import networkx as nx


num_nodes = random.randint(30, 60)


def generateRandom():
    n = len(os.listdir("./graphs")) + 1
    nodes = random.randint(10, 25)
    edges = random.randint(nodes, nodes + 30)
    edg_graph = set()
    graph = []
    iteration = 0
    while iteration < edges:
        cost = random.randint(1, 15)
        n1 = random.randint(0, nodes+1)
        n2 = random.randint(0, nodes+1)
        if not edg_graph.__contains__((n1, n2)):
            graph.append((n1, n2, cost))
            iteration += 1


    with open(f"./graphs/graph{n}.csv", "w") as f:
        csv_writer = csv.writer(f)
        csv_writer.writerows(graph)
        
    n = n+1

def generateRandomNet():
    probability = 0.7
    # Generate a random graph
    G = nx.gnp_random_graph(num_nodes, probability)
    writeGraph(G)


def generateStrongTZ():
    num_neighbors = random.randint(4, 8)
    probability_rewiring = random.random()

    # Generate a Watts-Strogatz graph
    G = nx.watts_strogatz_graph(num_nodes, num_neighbors, probability_rewiring)
    writeGraph(G)

def generateBarabasi():
    # Set the number of nodes and the number of edges to attach from a new node to existing nodes
    num_edges_to_attach = random.randint(4, 8)
    # Generate a Barabasi-Albert graph
    G = nx.barabasi_albert_graph(num_nodes, num_edges_to_attach)
    writeGraph(G)


def generateErdos():
    probability = random.random()
    G = nx.erdos_renyi_graph(num_nodes, probability)
    writeGraph(G)


def writeGraph(G: nx.Graph):
    n = len(os.listdir("./graphs")) + 1
    for u, v in G.edges:
        G[u][v]['cost'] = random.randint(1, 10)
    with open(f"./graphs/graph{n}.csv", 'w', newline='') as file:
        writer = csv.writer(file)
        for u, v, attr in G.edges(data=True):
            writer.writerow([u, v, attr['cost']])
    
    
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == "__main__":
    while True:
        clear_screen()
        try:
            type = int(input("Select which type of graph do you want to generate: \n \
                0. EXIT \n \
                1. Random\n \
                2. Random using networkx\n \
                3. The Watts-Strogatz graph\n \
                4. The Barabasi-Albert graph\n \
                5. Erdos Reny graph \n"))
            if type == 1:
                generateRandom()
            elif type == 2:
                generateRandomNet()
            elif type == 3: 
                generateStrongTZ()
            elif type == 4:
                generateBarabasi()
            elif type == 5:
                generateErdos()
            elif type == 0:
                break
            print("<< Created !! >>\n\n")
            time.sleep(1)
        except:
            print("Type an INTEGER !!!!")