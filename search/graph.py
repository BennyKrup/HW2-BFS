import networkx as nx

class Graph:
    """
    Class to contain a graph and your bfs function
    
    You may add any functions you deem necessary to the class
    """
    def __init__(self, filename: str):
        """
        Initialization of graph object 
        """
        self.graph = nx.read_adjlist(filename, create_using=nx.DiGraph, delimiter=";")

    def bfs(self, start, end=None):
        """
        TODO: write a method that performs a breadth first traversal and pathfinding on graph G

        * If there's no end node input, return a list nodes with the order of BFS traversal
        * If there is an end node input and a path exists, return a list of nodes with the order of the shortest path
        * If there is an end node input and a path does not exist, return None

        """
       ## edge case checks:
        if not self.graph.nodes():
            raise ValueError("Graph is empty")
        if start not in self.graph.nodes() or (end and end not in self.graph.nodes()):
            raise ValueError("Start or end node not in graph")
        if start == end:
            print("Start and end are the same")
            return [start]

        queue = [start]
        visited = set([start])
        predecessor = {start: None}

        while queue:
            node = queue.pop(0)
            if node == end:
                break

            for neighbor in self.graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)
                    visited.add(neighbor)
                    predecessor[neighbor] = node

        if end:
            if end not in visited:
                return None
            path = []
            current = end
            while current is not None:
                path.append(current)
                current = predecessor[current]
            path.reverse()
            return path

        return list(visited)

# Example usage:
# graph = Graph("filename.txt")
# print(graph.bfs("start_node", "end_node"))
