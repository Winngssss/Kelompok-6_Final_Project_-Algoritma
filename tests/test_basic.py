import unittest
from basic.euclidian import Euclid
from basic.huffman import Huffman
from basic.union_find import UnionFind

class TestBasic(unittest.TestCase):
    def setUp(self):
        self.euclid = Euclid(0, 0)
        self.union_find = UnionFind(5)
        self.huffman = Huffman()

    def test_gcd_positive(self):
        self.euclid = Euclid(48, 18)
        self.assertEqual(self.euclid.gcd(), 6)

        self.euclid = Euclid(101, 103)
        self.assertEqual(self.euclid.gcd(), 1)

    def test_union_find(self):
        uf = UnionFind(5)
        uf.union(0, 1)
        uf.union(1, 2)

        self.assertTrue(uf.connected(0, 2))
        self.assertFalse(uf.connected(0, 3))

    def test_huffman_encode_decode(self):

        text = "huffman coding"

        encoded_text, root = self.huffman.huffman_coding(text)
        self.assertIsInstance(encoded_text, str)
        self.assertGreater(len(encoded_text), 0)

        decoded_text = self.huffman.decode(encoded_text)
        self.assertEqual(decoded_text, text)

if __name__ == "__main__":
    unittest.main()