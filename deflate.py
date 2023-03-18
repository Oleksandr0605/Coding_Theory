"""
This class represent an instance of Deflate algorithm
"""
import huffman
import lz77


class Deflate(lz77.LZ77, huffman.Huffman):
    """
    This class represent Deflate algorithm.
    """
    def __init__(self, buffer_size) -> None:
        """
        The constructor of a class.
        """
        lz77.LZ77.__init__(self, buffer_size)
        huffman.Huffman.__init__(self)

    def encode(self, text):
        """
        This method represent encoding.
        """
        encoded_by_lz77 = lz77.LZ77(self.buffer_size).encode(text)
        have_to_be_encoded = [tuple(elem) for elem in encoded_by_lz77]
        return huffman.Huffman().encode(have_to_be_encoded)
