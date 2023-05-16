import random
import csv
import os
import networkx as nx


n = len(os.listdir("./graphs"))
num_nodes = random.randint(20, 40)


def generateRandom():
    n = len(os.listdir("./graphs"))

    for _ in range(1, 5):
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


def generateErdos():
    probability = random.random()
    G = nx.erdos_renyi_graph(num_nodes, probability)
    writeGraph(G)


def writeGraph(G: nx.Graph):
    for u, v in G.edges:
        G[u][v]['cost'] = random.randint(1, 10)
    with open(f"./graphs/graph{n+1}.csv", 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['node1', 'node2', 'cost'])  # Write header row
        for u, v, attr in G.edges(data=True):
            writer.writerow([u, v, attr['cost']])

if __name__ == "__main__":
    while True:
        try:
            type = int(input("Select which type of graph do you want to generate: \n \
                1. Random\n \
                2. Random using networkx\n \
                3. The Watts-Strogatz graph\n \
                4. The Barabasi-Albert graph\n \
                5. Erdos Reny graph \n \
                Use CTRL-C to break\n\nInput: "))
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
            print("<< Created !! >>\n\n")
        except:
            print("Type an INTEGER !!!!")