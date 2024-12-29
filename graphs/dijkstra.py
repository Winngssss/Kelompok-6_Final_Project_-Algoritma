import heapq

class Dijkstra:
    def run(self, graph, source):
        n = len(graph)
        dist = [float('inf')] * n
        dist[source] = 0
        pq = [(0, source)]

        while pq:
            current_dist, current_node = heapq.heappop(pq)
            if current_dist > dist[current_node]:
                continue
            for neighbor, weight in graph[current_node]:
                distance = current_dist + weight
                if distance < dist[neighbor]:
                    dist[neighbor] = distance
                    heapq.heappush(pq, (distance, neighbor))

        return dist