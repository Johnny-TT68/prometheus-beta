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
    
    # Initialize the residual graph
    residual_graph = {}
    for u in graph:
        residual_graph[u] = {}
        for v, capacity in graph[u].items():
            # Add forward and backward edges
            residual_graph[u][v] = capacity
            if v not in residual_graph:
                residual_graph[v] = {}
            if u not in residual_graph[v]:
                residual_graph[v][u] = 0
    
    # Total flow tracking
    max_flow = 0
    
    # While there is an augmenting path
    while True:
        # BFS to find the shortest augmenting path
        parent = {}
        flow_to_node = {}
        visited = set()
        queue = deque([source])
        
        # Initialize
        flow_to_node[source] = float('inf')
        visited.add(source)
        
        # BFS to find augmenting path
        found_path = False
        while queue:
            u = queue.popleft()
            
            # Explore neighbors
            for v, capacity in residual_graph[u].items():
                if capacity > 0 and v not in visited:
                    # Update flow
                    flow_to_node[v] = min(flow_to_node.get(u, float('inf')), capacity)
                    parent[v] = u
                    
                    # Path found to sink
                    if v == sink:
                        found_path = True
                        break
                    
                    # Add to queue and mark visited
                    queue.append(v)
                    visited.add(v)
            
            if found_path:
                break
        
        # If no path found, we are done
        if not found_path:
            break
        
        # Trace the path and update residual graph
        v = sink
        path_flow = flow_to_node[sink]
        
        # Trace back and update residual graph
        while v != source:
            u = parent[v]
            residual_graph[u][v] -= path_flow
            residual_graph[v][u] += path_flow
            v = u
        
        # Update max flow
        max_flow += path_flow
    
    return max_flow