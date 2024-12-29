class Kruskal:
    def run(self, edges, n):
        parent = list(range(n))
        rank = [0] * n

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            root_x = find(x)
            root_y = find(y)
            if root_x != root_y:
                if rank[root_x] > rank[root_y]:
                    parent[root_y] = root_x
                elif rank[root_x] < rank[root_y]:
                    parent[root_x] = root_y
                else:
                    parent[root_y] = root_x
                    rank[root_x] += 1

        mst = []
        edges.sort(key=lambda x: x[2])
        for u, v, weight in edges:
            if find(u) != find(v):
                union(u, v)
                mst.append((u, v, weight))

        return mst