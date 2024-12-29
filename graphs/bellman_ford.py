class BellmanFord:
    def run(self, graph, source):
        n = len(graph)
        dist = [float('inf')] * n
        dist[source] = 0

        for _ in range(n - 1):
            for u, v, w in graph:
                if dist[u] != float('inf') and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w

        for u, v, w in graph:
            if dist[u] != float('inf') and dist[u] + w < dist[v]:
                return "Negative weight cycle detected!"

        return dist