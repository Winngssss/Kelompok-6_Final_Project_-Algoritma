import unittest
from arrays.boyer_moore import BoyerMoore
from arrays.floyd import Floyd
from arrays.kadane import Kadane
from arrays.kmp import KMP
from arrays.quick_select import QuickSelect


class TestArray(unittest.TestCase):
    def test_boyer_moore(self):
        bm = BoyerMoore()
        self.assertEqual(bm.run("hello world", "world"), 6)
        self.assertEqual(bm.run("abcdef", "gh"), -1)

    def test_floyd(self):
        graph = [
            [0, 3, float('inf'), 7],
            [8, 0, 2, float('inf')],
            [5, float('inf'), 0, 1],
            [2, float('inf'), float('inf'), 0]
        ]
        
        floyd = Floyd()
        result = floyd.run(graph)
        
        expected = [
            [0, 3, 5, 6],
            [5, 0, 2, 3],
            [3, 6, 0, 1],
            [2, 5, 7, 0]
        ]

        self.assertEqual(result, expected)

    def test_kadane(self):
        kadane = Kadane()
        self.assertEqual(kadane.run([-2, 1, -3, 4, -1, 2, 1, -5, 4]), 6)
        self.assertEqual(kadane.run([1, 2, 3, 4]), 10)

    def test_kmp(self):
        kmp = KMP()
        self.assertEqual(kmp.run("abcdabcabcd", "abc"), 0)
        self.assertEqual(kmp.run("abcdef", "gh"), -1)

    def test_quick_select(self):
        qs = QuickSelect()
        self.assertEqual(qs.run([7, 10, 4, 3, 20, 15], 4), 10)

if __name__ == "__main__":
    unittest.main()