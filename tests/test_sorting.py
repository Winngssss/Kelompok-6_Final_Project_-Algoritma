import unittest
from sorting.insertion_sort import insertion_sort
from sorting.selection_sort import selection_sort
from sorting.merge_sort import merge_sort
from sorting.quick_sort import quick_sort
from sorting.heap_sort import heap_sort
from sorting.counting_sort import counting_sort

class TestSortingAlgorithms(unittest.TestCase):
    def test_insertion_sort(self):
        self.assertEqual(insertion_sort([5, 2, 9, 1, 5, 6]), [1, 2, 5, 5, 6, 9])

    def test_selection_sort(self):
        self.assertEqual(selection_sort([5, 2, 9, 1, 5, 6]), [1, 2, 5, 5, 6, 9])

    def test_merge_sort(self):
        self.assertEqual(merge_sort([5, 2, 9, 1, 5, 6]), [1, 2, 5, 5, 6, 9])

    def test_quick_sort(self):
        arr = [5, 2, 9, 1, 5, 6]
        quick_sort(arr, 0, len(arr) - 1)
        self.assertEqual(arr, [1, 2, 5, 5, 6, 9])

    def test_heap_sort(self):
        self.assertEqual(heap_sort([5, 2, 9, 1, 5, 6]), [1, 2, 5, 5, 6, 9])

    def test_counting_sort(self):
        self.assertEqual(counting_sort([5, 2, 9, 1, 5, 6]), [1, 2, 5, 5, 6, 9])

if __name__ == "_main_":
    unittest.main()
if __name__ == "_main_":
    unittest.main()