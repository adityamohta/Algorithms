"""
    ---------- Depth First Traversal or BFS for a Graph ----------
"""
from collections import defaultdict


class Graph:
    # Constructor
    def __init__(self):
        # default dictionary to store graph
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def _dfs(self, v, visited):
        visited[v] = True
        print v
        # Recur for all the vertices adjacent to this vertex
        for i in self.graph[v]:
            if not visited[i]:
                self._dfs(i, visited)

    def dfs(self, s):
        visited = [False] * len(self.graph)
        # DFS Traversal
        self._dfs(s, visited)


if __name__ == '__main__':
    g = Graph()
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(2, 0)
    g.add_edge(2, 3)
    g.add_edge(3, 3)

    print "Following is DFS from (starting from vertex 2)"
    g.dfs(2)
