"""
This class represent an instance of class Huffman, with encoding and decoding methods.
"""
from queue import PriorityQueue
from collections import Counter

class Node:
    """
    This code represent one node for the Huffman tree.
    """
    def __init__(self, frequency, character=None) -> None:
        """
        The constructor for a class.
        """
        self.frequency = frequency
        self.character = character
        self.left = None
        self.right = None

    def __lt__(self, other) -> bool:
        """
        This method compare two nodes by their frequencies.
        """
        return self.frequency < other.frequency


class Huffman:
    """
    This class represent Huffman algorithm.
    """
    def __init__(self) -> None:
        """
        The constructor for a class.
        """
        self.codes = {}

    def encode(self, text):
        """
        This method implement Huffman encoding.
        """
        frequency_dict = Counter(text)
        queue = PriorityQueue() # initializing the priority queue
        for char, freq in frequency_dict.items():
            queue.put(Node(freq, char))

        while queue.qsize() > 1: # iterating through the whole queue
            node1, node2 = queue.get(), queue.get() # getting two elements that occur most rarely
            merged_node = Node(node1.frequency + node2.frequency) # creating new node by adding them
            merged_node.right, merged_node.left = node1, node2 # setting
    # the node with higher frequency to the right according to the new node, and lower to the left.
            queue.put(merged_node) # adding new node to the queue.

        root = queue.get() # the last node in the queue is the root node of the Huffman tree
        stack = [(root, "")] # setting the stack

        while stack:
            node, code = stack.pop()
            if node.character: # checking if the node has it's character
                self.codes[node.character] = code
            else:
                stack.append((node.left, code + "0"))
                stack.append((node.right, code + "1"))
        coded = [self.codes[elem] for elem in text]
        ret_dct = {}
        for ind in range(len(text)):
            ret_dct[coded[ind]] = text[ind]
        return coded, ret_dct

    def decode(self, code, dct) -> str:
        """
        Decoding by huffman
        """
        text = ""
        for cod in code:
            try:
                text += dct[cod]
            except:
                return "Wrong input"
        return text


def read_file(name):
    """
    Reads file
    """
    with open(name, "r", encoding="utf-8") as fff:
        lines = fff.readlines()
    lines = "".join(lines)
    return lines


import time

alg = Huffman()
strr = read_file("text.txt")

start_time = time.time()  # record the start time
code, dct = alg.encode(strr)
end_time = time.time()  # record the end time

print("Time taken to encode:", end_time - start_time, "seconds")

decoded_str = alg.decode(code, dct)
# print(decoded_str)