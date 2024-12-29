import unittest
from searching.binary import BinarySearch
from searching.breadth_first import BreadthFirst
from searching.depth_first import DepthFirst
from searching.linear import LinearSearch

class TestBinarySearch(unittest.TestCase):
    def setUp(self):
        self.binary_search = BinarySearch()

    def test_binary_search_found(self):
        arr = [1, 3, 5, 7, 9]
        result = self.binary_search.search(arr, 5)
        self.assertEqual(result, 2)

    def test_binary_search_not_found(self):
        arr = [1, 3, 5, 7, 9]
        result = self.binary_search.search(arr, 6)
        self.assertEqual(result, -1)

    def test_binary_search_empty_array(self):
        arr = []
        result = self.binary_search.search(arr, 1)
        self.assertEqual(result, -1)

class TestBreadthFirst(unittest.TestCase):
    def setUp(self):
        self.bfs = BreadthFirst()

    def test_bfs_simple_graph(self):
        graph = {1: [2, 3], 2: [4], 3: [4], 4: []}
        result = self.bfs.search(graph, 1)
        self.assertEqual(result, [1, 2, 3, 4])

    def test_bfs_disconnected_graph(self):
        graph = {1: [2], 2: [], 3: [4], 4: []}
        result = self.bfs.search(graph, 1)
        self.assertEqual(result, [1, 2])

    def test_bfs_single_node(self):
        graph = {1: []}
        result = self.bfs.search(graph, 1)
        self.assertEqual(result, [1])

class TestDepthFirst(unittest.TestCase):
    def setUp(self):
        self.dfs = DepthFirst()

    def test_dfs_simple_graph(self):
        graph = {1: [2, 3], 2: [4], 3: [4], 4: []}
        result = self.dfs.search(graph, 1)
        self.assertEqual(result, [1, 3, 4, 2])

    def test_dfs_disconnected_graph(self):
        graph = {1: [2], 2: [], 3: [4], 4: []}
        result = self.dfs.search(graph, 1)
        self.assertEqual(result, [1, 2])

    def test_dfs_single_node(self):
        graph = {1: []}
        result = self.dfs.search(graph, 1)
        self.assertEqual(result, [1])

class TestLinearSearch(unittest.TestCase):
    def setUp(self):
        self.linear_search = LinearSearch()

    def test_linear_search_found(self):
        arr = [10, 20, 30, 40, 50]
        result = self.linear_search.search(arr, 30)
        self.assertEqual(result, 2)

    def test_linear_search_not_found(self):
        arr = [10, 20, 30, 40, 50]
        result = self.linear_search.search(arr, 25)
        self.assertEqual(result, -1)

    def test_linear_search_empty_array(self):
        arr = []
        result = self.linear_search.search(arr, 10)
        self.assertEqual(result, -1)

if __name__ == "__main__":
    unittest.main()