"""
This module includes the implementation of lz77 algorithm.
"""
from typing import List


class LZ77:
    """
    This class represent LZ77 algorithm.
    """
    def __init__(self, buffer_size: int) -> None:
        """
        The constructor for a class.
        """
        self.buffer_size = buffer_size

    def encode(self, input_str: str):
        """
        This method encode string.
        """
        output = [] # list to store result's
        pos = 0 # current position
        while pos < len(input_str): # iterate the whole string
            best_len = 0
            best_offset = 0
            for offset in range(1, self.buffer_size+1): # check all offsets
                if pos - offset < 0: # breaking if have gone too far(outside the buffer)
                    break
                i = pos - offset
                j = pos
                length = 0
                while j < len(input_str) and input_str[i] == input_str[j] and length < offset:
                    length += 1
                    i += 1
                    j += 1
                if length > best_len: # checking if our current length is
                    # better than that one, which we already have
                    best_len = length
                    best_offset = offset
            if best_len > 0: # if a match, add it to the result
                #(first_param - the best offset, and the second one-how much will repeat it)
                try:
                    output.append((best_offset, best_len, input_str[pos + best_len]))
                    pos += best_len + 1 # adding best_len
                    # to position to continue loop without repeat
                except IndexError:
                    output.append((best_offset, best_len, set()))
                    pos += best_len + 1
                    continue
            else: # if we don't have a match, adding 0 as the first element
               # of the tuple and an ord representaion of the letter
                try:
                    output.append((0, 0, input_str[pos]))
                    pos += 1
                except IndexError:
                    output.append((0, 0, set()))
                    pos += 1
        return output

    def decode(self, encoded_list) -> str:
        """
        This method decodes the string.
        """
        res_str = ''
        for tup in encoded_list:
            for offset, max_len, next_item in [tup]:
                if offset == 0:
                    res_str += next_item
                else:
                    string_to_replace = res_str[len(res_str) - offset: len(res_str)]
                    for _ in range(max_len):
                        res_str += string_to_replace[offset % len(string_to_replace)]
                    res_str += next_item
        return res_str

    def compress_result(self, result: List[tuple]):
        """
        This method compress the result of the algorithm to bytearray().
        """
        compressed = bytearray()
        for offset, length, next_char in result:
            offset_bytes = offset.to_bytes(2, byteorder='big')
            length_bytes = length.to_bytes(1, byteorder='big')
            compressed += offset_bytes + length_bytes + bytes(next_char, encoding='utf-8')
        return compressed

    def write_to_file(self, path: str, result: bytearray) -> None:
        """
        This method writes compress info to file
        """
        assert isinstance(result, bytearray),\
        'Result has to be bytearray() type to write it in the file.'
        with open(path, mode='wb') as file_to_write:
            file_to_write.write(result)
