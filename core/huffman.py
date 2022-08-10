from core.constants import Constants
from helpers import get_frequencies, get_encoded

import heapq


class HuffmanNode:
    def __init__(self, freq, char, left=None, right=None):
        self.freq = freq # data or something similar, these are probabilities
        self.char = char
        self.left = left
        self.right = right

        self.direction = ""


frequencies = get_frequencies(Constants.FREQUENCIES)
input_text = get_encoded(Constants.INPUT_TEXT)

for idx, sentence in enumerate(input_text):

    for character in sentence:
        print(character)

    if idx == 0:
        break


class HuffmanTree:

    def __init__(self):
        self.root = None

    @staticmethod
    def is_leaf(root: HuffmanNode):
        return root.left is None and root.right is None

    def encode(self, root: HuffmanNode, inp_str, huffman_code: dict):
        if root is None:
            return

        if self.is_leaf(root):
            # what the heck is huffman_code?
            huffman_code.put(root.char, inp_str if len(inp_str) > 0 else "1")

        self.encode(root.left, inp_str + "0", huffman_code)
        self.encode(root.right, inp_str + "1", huffman_code)

    def decode(self, root, index):

        if root is None:
            return index

        if self.is_leaf(root):
            print(root.char)
            return index

        index += 1
        root = root.left if root.char[index] == '0' else root.right
        index = self.decode(root, index)
        return index

    def build_tree(self, text):
        """
        Base function to build the Huffman Tree, decoding the given input text, etc.
        Args:
            text:

        Returns:

        """
        if text is None or len(text) == 0: # base case
            return

    def build_tree_from_frequencies(self):
        minheap = list()
        frequencies = get_frequencies(Constants.FREQUENCIES)

        for k, v in frequencies.items():
            heapq.heappush(minheap, HuffmanNode(v, k))


        while len(minheap) > 1:
            left = heapq.heappop(minheap)











