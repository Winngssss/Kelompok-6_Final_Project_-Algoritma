class TopologicalSort:
    def run(self, graph):
        """Topological sort using DFS."""
        visited = set()
        stack = []

        def dfs(node):
            if node in visited:
                return
            visited.add(node)
            for neighbor in graph.get(node, []):
                dfs(neighbor)
            stack.append(node)

        for node in graph:
            if node not in visited:
                dfs(node)

        return stack[::-1]