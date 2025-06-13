# -*- coding: utf-8 -*-
"""
Created on Wed Jun 11 14:14:02 2025

@author: DELL
"""

from collections import defaultdict, deque

def build_de_bruijn_graph(k):
    graph = defaultdict(deque)
    nodes = set()

    for i in range(2**(k - 1)):
        prefix = format(i, f'0{k-1}b')
        for bit in ['0', '1']:
            suffix = prefix[1:] + bit
            graph[prefix].append(suffix)
            nodes.add(prefix)
            nodes.add(suffix)
    return graph

def find_eulerian_cycle(graph):
    graph_copy = {u: deque(v) for u, v in graph.items()}
    start_node = next(iter(graph))
    stack = [start_node]
    path = []

    while stack:
        current = stack[-1]
        if graph_copy.get(current):
            next_node = graph_copy[current].popleft()
            stack.append(next_node)
        else:
            path.append(stack.pop())
    return path[::-1]

def construct_circular_string(path, k):
    text = path[0]
    for node in path[1:]:
        text += node[-1]
    return text[:-(k-1)]  # Make it circular by trimming last k-1 bits

if __name__ == "__main__":
    # 🔽 Input and Output file names
    input_file = "dataset_30187_11.txt"
    output_file = "output.txt"

    with open(input_file, 'r') as f:
        k = int(f.readline().strip())

    graph = build_de_bruijn_graph(k)
    cycle = find_eulerian_cycle(graph)
    result = construct_circular_string(cycle, k)

    with open(output_file, 'w') as f:
        f.write(result)

    print("k-universal circular string written to", output_file)
