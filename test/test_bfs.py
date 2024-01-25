# write tests for bfs
import pytest
from search.graph import Graph
import networkx as nx

def test_bfs_traversal():
    """
    TODO: Write your unit test for a breadth-first
    traversal here. Create an instance of your Graph class 
    using the 'tiny_network.adjlist' file and assert 
    that all nodes are being traversed (ie. returns 
    the right number of nodes, in the right order, etc.)
    """
    graph = Graph("data/tiny_network.adjlist")
    start_node = list(graph.graph.nodes())[0]
    result = graph.bfs(start_node)
    
    # Check that all nodes are visited
    assert len(result) == len(graph.graph.nodes()), "Not all nodes are visited"

    # Compare the order of nodes with NetworkX's bfs order
    expected_order = list(nx.bfs_tree(graph.graph, source=start_node))
    assert result == expected_order, "BFS traversal order is incorrect"

    #compare the amount of nodes and edges with NetworkX's bfs order
    expected_nodes = len(nx.bfs_tree(graph.graph, source=start_node).nodes())
    expected_edges = len(nx.bfs_tree(graph.graph, source=start_node).edges())
    assert len(result) == expected_nodes, "same amount of nodes"
    assert len(result) -1 == expected_edges, "First node has no edge"



def test_bfs():
    """
    TODO: Write your unit test for your breadth-first 
    search here. You should generate an instance of a Graph
    class using the 'citation_network.adjlist' file 
    and assert that nodes that are connected return 
    a (shortest) path between them.
    
    Include an additional test for nodes that are not connected 
    which should return None. 
    """
    citation_network = Graph("data/citation_network.adjlist")

    # Choose a start node that has at least one connection
    for node in citation_network.graph.nodes():
        if citation_network.graph.out_degree(node) > 0:  
            start_node = node
            break
    bfs_tree = nx.bfs_tree(citation_network.graph, start_node)
    bfs_nodes = set(bfs_tree.nodes())
    all_nodes = set(citation_network.graph.nodes())

    # Ensure there are unconnected nodes in the graph
    if len(all_nodes) <= len(bfs_nodes):
        raise ValueError("The graph is fully connected, no unconnected nodes to test")

    # Find a connected node (other than start node)
    connected_node = next(iter(bfs_nodes - {start_node}))

    # Find an unconnected node
    unconnected_node = next(iter(all_nodes - bfs_nodes))

    # Test BFS for a connected node
    bfs_path = citation_network.bfs(start_node, connected_node)
    assert bfs_path is not None, f"BFS did not find a path for connected nodes: {start_node} -> {connected_node}"

    # Test BFS for an unconnected node
    bfs_path_none = citation_network.bfs(start_node, unconnected_node)
    assert bfs_path_none is None, f"BFS should return None for unconnected nodes: {start_node} -> {unconnected_node}"

def test_bfs_empty_graph():
    """
    Unit test for an empty graph.
    """
    with pytest.raises(ValueError) as excinfo:
        empty_graph = Graph("data/empty_graph.adjlist")
        empty_graph.bfs("any_node") # A node name will raise an error since the graph is empty
    assert "Graph is empty" in str(excinfo.value)
