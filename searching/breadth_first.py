class BreadthFirst:
    def search(self, graph, start):
        visited = []
        queue = [start]

        while queue:
            node = queue.pop(0)
            if node not in visited:
                visited.append(node)
                queue.extend([n for n in graph.get(node, []) if n not in visited])

        return visited