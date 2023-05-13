import random
import csv



n = 5



for i in range(1, 5):
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
        csv_writer.writerow(["Node1, Node2, Cost"])
        csv_writer.writerows(graph)
        
    n = n+1