import unittest
from graphs.bellman_ford import BellmanFord
from graphs.dijkstra import Dijkstra
from graphs.kruskal import Kruskal
from graphs.flood_fill import FloodFill
from graphs.lee import Lee
from graphs.topological_sort import TopologicalSort

class TestGraphAlgorithms(unittest.TestCase):
    def test_bellman_ford(self):
        graph = [
            (0, 1, 1),
            (0, 2, 4),
            (1, 2, 2)
        ]
        bf = BellmanFord()
        distances = bf.run(graph, 0)
        expected = [0, 1, 3]
        self.assertEqual(distances, expected)

    def test_dijkstra(self):
        graph = {
            0: [(1, 1), (2, 4)],
            1: [(2, 2)],
            2: []
        }
        dijkstra = Dijkstra()
        distances = dijkstra.run(graph, 0)
        print("Dijkstra distances:", distances)
        expected = [0, 1, 3]
        self.assertEqual(distances, expected)

    def test_kruskal(self):
        edges = [
            (0, 1, 1),
            (1, 2, 2),
            (0, 2, 3)
        ]
        kruskal = Kruskal()
        mst = kruskal.run(edges, 3)
        expected = [(0, 1, 1), (1, 2, 2)]
        self.assertEqual(mst, expected)

    def test_flood_fill(self):
        image = [
            [1, 1, 1],
            [1, 0, 1],
            [1, 1, 1]
        ]
        ff = FloodFill()
        result = ff.run(image, 1, 1, 2)
        expected = [
            [1, 1, 1],
            [1, 2, 1],
            [1, 1, 1]
        ]
        self.assertEqual(result, expected)

    def test_lee(self):
        grid = [
            [0, 0],
            [0, 0]
        ]
        start = (0, 0)
        end = (1, 1)
        lee = Lee()
        result = lee.run(grid, start, end)
        expected = 2
        self.assertEqual(result, expected)

    def test_topological_sort(self):
        graph = {
            'A': ['B'],
            'B': ['C'],
            'C': []
        }
        ts = TopologicalSort()
        result = ts.run(graph)
        expected = ['A', 'B', 'C']
        self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()