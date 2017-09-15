"""
    ---------- Breadth First Traversal or BFS for a Graph ----------
"""
from collections import defaultdict


class Graph:
    # Constructor
    def __init__(self):
        # default dictionary to store graph
        self.graph = defaultdict(list)

    # function to add an edge to graph.
    def add_edge(self, u, v):
        self.graph[u].append(v)

    # function to print BFS of graph. here s is source node.
    def BFS(self, s):

        # Mark all vertices as not visited
        visited = [False] * len(self.graph)
        # Create a queue for BFS
        queue = [s]
        # Mark the source node as visited and enqueue it
        visited[s] = True

        while queue:
            # de-queue a vertex and print it
            s = queue.pop(0)
            print s

            # Get all adjacent vertices of the de-queued
            # vertex s. If a adjacent has not been visited,
            # then mark it visited and enqueue it
            for i in self.graph[s]:
                if not visited[i]:
                    queue.append(i)
                    visited[i] = True


if __name__ == '__main__':
    g = Graph()
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(2, 0)
    g.add_edge(2, 3)
    g.add_edge(3, 4)
    g.add_edge(4, 4)

    print "Following is Breadth First Traversal (starting from vertex 2)"
    g.BFS(2)
