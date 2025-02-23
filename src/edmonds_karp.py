from typing import Dict, List, Optional
from collections import deque

def edmonds_karp(graph: Dict[int, Dict[int, int]], source: int, sink: int) -> int:
    """
    Implement the Edmonds-Karp algorithm to find maximum flow in a graph.
    
    Args:
        graph (Dict[int, Dict[int, int]]): Adjacency list representation of the graph 
            where graph[u][v] represents the capacity from node u to node v.
        source (int): The source node.
        sink (int): The sink node.
    
    Returns:
        int: The maximum flow from source to sink.
    
    Raises:
        ValueError: If source or sink nodes are not in the graph.
        TypeError: If graph is not a valid adjacency list.
    """
    # Validate input
    if not isinstance(graph, dict):
        raise TypeError("Graph must be a dictionary")
    
    if source not in graph or sink not in graph:
        raise ValueError("Source or sink node not in graph")
    
    # Create a residual graph (deep copy of the original graph)
    residual_graph = {}
    for u in graph:
        residual_graph[u] = graph[u].copy()
        for v in graph[u]:
            if v not in residual_graph:
                residual_graph[v] = {}
            if u not in residual_graph[v]:
                residual_graph[v][u] = 0
    
    # Initialize max flow
    max_flow = 0
    
    # Find augmenting paths using BFS
    while True:
        # Perform BFS to find an augmenting path
        parent = {}
        visited = set()
        queue = deque([source])
        visited.add(source)
        
        # Find an augmenting path
        while queue:
            u = queue.popleft()
            
            # Check all neighbors
            for v, capacity in residual_graph[u].items():
                if v not in visited and capacity > 0:
                    parent[v] = u
                    visited.add(v)
                    queue.append(v)
                    
                    # If we've reached the sink, we found a path
                    if v == sink:
                        break
            
            # Early exit if sink is found
            if sink in visited:
                break
        
        # If no path to sink is found, we're done
        if sink not in visited:
            break
        
        # Find the minimum residual capacity along the path
        path_flow = float('inf')
        v = sink
        while v != source:
            u = parent[v]
            path_flow = min(path_flow, residual_graph[u][v])
            v = u
        
        # Update residual capacities
        v = sink
        while v != source:
            u = parent[v]
            residual_graph[u][v] -= path_flow
            residual_graph[v][u] += path_flow
            v = u
        
        # Add path flow to max flow
        max_flow += path_flow
    
    return max_flow