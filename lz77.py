"""
This module includes the implementation of lz77 algorithm.
"""
class LZ77:
    """
    This class represent LZ77 algorithm.
    """
    def __init__(self, buffer_size):
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
                output.append((best_offset, best_len))
                pos += best_len # adding best_len to position to continue loop without repeat
            else: # if we don't have a match, adding 0 as the first element
               # of the tuple and an ord representaion of the letter
                output.append((0, ord(input_str[pos])))
                pos += 1
        return output

    def decode(self, encoded_list) -> str:
        """
        This method decodes the string.
        """
        res_str = ''
        for tup in encoded_list:
            for i, j in [tup]:
                if i == 0:
                    res_str += chr(j)
                else:
                    string_to_replace = res_str[len(res_str) - i: len(res_str)]
                    for i in range(j):
                        res_str += string_to_replace[i % len(string_to_replace)]
        return res_str


def read_file(name):
    """
    Reads file
    """
    with open(name, "r", encoding="utf-8") as fff:
        lines = fff.readlines()
    lines = "".join(lines)
    return lines


import sys
code = LZ77(100)
strr = read_file("text.txt")
code = code.encode(strr)
# print(code)
print(f"text size: {sys.getsizeof(strr)/1000000} mb")
print(f"coded size: {sys.getsizeof(code)/1000000} mb")