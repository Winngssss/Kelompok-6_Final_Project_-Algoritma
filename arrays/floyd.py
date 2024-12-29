class Floyd:
    def run(self, graph):
        n = len(graph)
        dist = [row[:] for row in graph]
        
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if dist[i][j] > dist[i][k] + dist[k][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]

            print(f"Setelah memproses node {k}:")
            for row in dist:
                print(row)
        
        return dist