class Huffman:
    def __init__(self):
        self.codes = {}
        self.reverse_mapping = {}

    class Node:
        def __init__(self, char, freq):
            self.char = char
            self.freq = freq
            self.left = None
            self.right = None

    def build_frequency_table(self, text):
        frequency = {}
        for char in text:
            if char in frequency:
                frequency[char] += 1
            else:
                frequency[char] = 1
        return frequency

    def build_huffman_tree(self, frequency):
        nodes = []
        for char, freq in frequency.items():
            nodes.append(self.Node(char, freq))

        while len(nodes) > 1:
            nodes.sort(key=lambda node: node.freq)

            left = nodes.pop(0)
            right = nodes.pop(0)

            merged = self.Node(None, left.freq + right.freq)
            merged.left = left
            merged.right = right

            nodes.append(merged)

        return nodes[0] if nodes else None

    def build_codes(self, root, current_code=""):

        if not root:
            return

        if root.char is not None:
            self.codes[root.char] = current_code
            self.reverse_mapping[current_code] = root.char
            return

        self.build_codes(root.left, current_code + "0")
        self.build_codes(root.right, current_code + "1")

    def encode(self, text):

        encoded_text = ""
        for char in text:
            encoded_text += self.codes.get(char, "")
        return encoded_text

    def decode(self, encoded_text):

        current_code = ""
        decoded_text = ""

        for bit in encoded_text:
            current_code += bit
            if current_code in self.reverse_mapping:
                decoded_text += self.reverse_mapping[current_code]
                current_code = ""

        return decoded_text

    def huffman_coding(self, text):

        frequency = self.build_frequency_table(text)
        root = self.build_huffman_tree(frequency)
        self.build_codes(root)

        encoded_text = self.encode(text)
        return encoded_text, root