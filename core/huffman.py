from core.constants import Constants
from helpers import get_frequencies, get_encoded
from tree import PriorityQueueReq


class HuffmanNodeDirectional:
    """
    This is a TreeNode or a Huffman Node that starts with a character and frequency. Freq as counts of the letters in
    input text is also a norm.
    """

    def __init__(self, char, freq, left=None, right=None):
        self.char = char
        self.freq = freq  # data or something similar, these are probabilities
        self.left = left
        self.right = right
        self.direction = ""


class HuffmanNode:
    def __init__(self, character, freq=0, left=None, right=None):
        self.character = character
        self.freq = freq
        self.left = left
        self.right = right

    def __repr__(self):
        return f"<HuffmanNode: char_list='{self.character}', freq={self.freq}, left={self.left}, right={self.right}>"

    def __lt__(self, other):
        return self.freq < other.freq

    def __le__(self, other):
        return self.freq <= other.freq

    def __gt__(self, other):
        return self.freq > other.freq

    def __ge__(self, other):
        return self.freq >= other.freq


class HuffmanCodes:
    def __init__(self):
        self.code_dict = None
        self.head = None

    def __repr__(self):
        return "<HuffmanTree: head={}>".format(self.head)

    @staticmethod
    def get_frequencies():
        return get_frequencies(Constants.FREQUENCIES)

    @staticmethod
    def get_input_text(file):
        return get_encoded(filename=file)

    @staticmethod
    def merge_nodes(one, two):
        return HuffmanNode(one.character + two.character, one.freq + two.freq, one, two)

    #  Display Huffman code
    def print_tree(self, node, result):
        if node is None:
            return

        if node.left is None and node.right is None:
            print("\n ", node.right, " ", result, end="")
            return

        self.print_tree(node.left, result + "0")
        self.print_tree(node.right, result + "1")

    def print_code_table(self):
        """Prints a table of all characters, codes, and code lengths found in the input"""
        if self.char_dict is not None:
            for i in self.head.char_dict.items():
                length, code = self.get_code(i, self.head)
                print(f"'{i}'\t\t{code}\t\t{code:0{length}b}")

    def build_tree(self):

        queue = PriorityQueueReq()

        for letter, frequency in self.get_frequencies().items():
            root = HuffmanNode(letter, frequency)
            queue.push(root)

        left: HuffmanNode = queue.pop()
        right: HuffmanNode = queue.pop()

        while left and right:
            # loop through until necessary, combine nodes as necessary from PriorityQueue
            queue.push(self.merge_nodes(left, right))
            left = queue.pop()
            right = queue.pop()

        self.head = left

        # create a memorized cache or lru_cache so we can efficiently return results without traversing.
        self.code_dict = {}
        for c in self.head.character:
            self.code_dict[c] = self.get_code(c)

        return

    def decoder(self, encoded_text):
        current_code = ""
        decoded_text = ""

        for bit in encoded_text:
            current_code += bit
            if current_code in self.code_dict:
                character = self.code_dict[current_code]
                decoded_text += character
                current_code = ""

        return decoded_text

    def encoder(self, text):
        result = ""

        for i in text:
            if i in self.code_dict:
                result += self.get_code(i)
            # insert
        return result

    def get_code(self, s, node, code=''):
        if node.left is None and node.right is None:
            return code
        else:
            temp = ''
            if node.left is not None:
                temp = self.get_code(s, node.left, code+'0')
            if not temp and node.right is not None:
                temp = self.get_code(s, node.right, code+'1')
            return temp

    def get_coded_string(self, char, node=None, reversal=False):
        if node is None:
            node = self.head
        if node.left is not None:
            if char in node.left.char_list:
                return self.get_coded_string(char, node.left) + "0" if not reversal \
                    else "0" + self.get_coded_string(char, node.left)

        if node.right is not None:
            if char in node.right.char_list:
                return self.get_coded_string(char, node.right) + "1" if not reversal \
                    else "1" + self.get_coded_string(char, node.right)
        return ""
