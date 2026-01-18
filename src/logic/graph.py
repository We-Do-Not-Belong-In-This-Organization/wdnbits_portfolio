from collections import deque

class Graph:
    def __init__(self):
        self.adj_list = {} 

    def add_vertex(self, value):
        """Adds a vertex to the graph."""
        if value not in self.adj_list:
            self.adj_list[value] = []
            return True
        return False

    def add_edge(self, v1, v2):
        """Adds an undirected edge between v1 and v2."""
        if v1 not in self.adj_list or v2 not in self.adj_list:
            return False
        
        # Avoid duplicate edges
        if v2 not in self.adj_list[v1]:
            self.adj_list[v1].append(v2)
        if v1 not in self.adj_list[v2]:
            self.adj_list[v2].append(v1)
        return True

    def remove_vertex(self, value):
        """Removes a vertex and all connected edges."""
        if value in self.adj_list:
            for neighbor in self.adj_list[value]:
                self.adj_list[neighbor].remove(value)
            del self.adj_list[value]
            return True
        return False

    def remove_edge(self, v1, v2):
        """Removes an edge between v1 and v2."""
        if v1 in self.adj_list and v2 in self.adj_list:
            if v2 in self.adj_list[v1]:
                self.adj_list[v1].remove(v2)
            if v1 in self.adj_list[v2]:
                self.adj_list[v2].remove(v1)
            return True
        return False

    def bfs(self, start_node):
        """Breadth-First Search traversal."""
        if start_node not in self.adj_list:
            return []
        
        visited = set()
        queue = deque([start_node])
        visited.add(start_node)
        result = []

        while queue:
            vertex = queue.popleft()
            result.append(vertex)

            for neighbor in sorted(self.adj_list[vertex]): 
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        return result

    def dfs(self, start_node):
        """Depth-First Search traversal."""
        if start_node not in self.adj_list:
            return []

        visited = set()
        result = []

        def _dfs_recursive(vertex):
            visited.add(vertex)
            result.append(vertex)
            for neighbor in sorted(self.adj_list[vertex]):
                if neighbor not in visited:
                    _dfs_recursive(neighbor)

        _dfs_recursive(start_node)
        return result
    
    def get_shortest_path(self, start_node, end_node):
        """Finds the shortest path (min edges) between two nodes."""
        if start_node not in self.adj_list or end_node not in self.adj_list:
            return None
        
        queue = deque([start_node])
        # Dictionary to track parent: {child: parent}
        # This lets us backtrack from End -> Start
        visited = {start_node: None}

        while queue:
            current = queue.popleft()

            if current == end_node:
                # Path found! Reconstruct it.
                path = []
                while current is not None:
                    path.append(current)
                    current = visited[current]
                return path[::-1] # Reverse to get Start -> End

            for neighbor in self.adj_list[current]:
                if neighbor not in visited:
                    visited[neighbor] = current
                    queue.append(neighbor)
        return None

    def get_data(self):
        """Returns the raw adjacency list."""
        return self.adj_list