import pytest
from src.edmonds_karp import edmonds_karp

def test_simple_graph():
    """Test a simple graph with a clear maximum flow path."""
    graph = {
        0: {1: 10, 2: 10},
        1: {2: 2, 3: 4, 4: 8},
        2: {4: 9},
        3: {5: 10},
        4: {3: 6, 5: 10},
        5: {}
    }
    assert edmonds_karp(graph, 0, 5) == 10

def test_no_flow_graph():
    """Test a graph with no possible flow."""
    graph = {
        0: {},
        1: {}
    }
    assert edmonds_karp(graph, 0, 1) == 0

def test_single_path_graph():
    """Test a graph with a single path."""
    graph = {
        0: {1: 5},
        1: {}
    }
    assert edmonds_karp(graph, 0, 1) == 5

def test_multiple_path_graph():
    """Test a graph with multiple possible paths."""
    graph = {
        0: {1: 10, 2: 10},
        1: {2: 2, 3: 4, 4: 8},
        2: {4: 9},
        3: {5: 10},
        4: {3: 6, 5: 10},
        5: {}
    }
    assert edmonds_karp(graph, 0, 5) == 10

def test_invalid_graph_type():
    """Test that a non-dictionary graph raises a TypeError."""
    with pytest.raises(TypeError):
        edmonds_karp([], 0, 1)

def test_invalid_source_sink():
    """Test that non-existent source or sink nodes raise a ValueError."""
    graph = {0: {1: 5}, 1: {}}
    
    with pytest.raises(ValueError):
        edmonds_karp(graph, 2, 1)
    
    with pytest.raises(ValueError):
        edmonds_karp(graph, 0, 2)

def test_cycle_graph():
    """Test a graph with a cycle."""
    graph = {
        0: {1: 10},
        1: {2: 10},
        2: {0: 10},
    }
    assert edmonds_karp(graph, 0, 2) == 10

def test_graph_with_multiple_edges():
    """Test a graph with multiple edges between same nodes."""
    graph = {
        0: {1: 10, 2: 5},
        1: {2: 15, 3: 20},
        2: {3: 10},
        3: {}
    }
    assert edmonds_karp(graph, 0, 3) == 25