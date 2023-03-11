"""
LZW coding
"""
import pickle

class LZW:
    """
    class for coding and uncoding
    """
    def encode(self, text) -> str:
        """
        Encoding the text by LZW
        """
        letters = sorted(list(set(text)))
        code_dict = []      #there is the list where code of elm is it's index
        for letter in letters:
            code_dict.append(letter)
        ret_dict = code_dict
        coded = bytearray()
        # coded = []
        line = text[0]
        for ind in range(len(text)):
            if ind != len(text) - 1:
                next = text[ind + 1]
            line += next
            if line not in code_dict:
                if len(code_dict) < 255:
                    code_dict.append(line)
                coded.append(code_dict.index(line[:-1]))
                line = next
                continue
            else:
                continue
        return coded, ret_dict

    def decode(self, coded, dct: list) -> str:
        decoded = ""
        thresh = 0
        for elm in coded:
            if (len(dct) - 1) >= int(elm):
                decoded += dct[int(elm)]
            else:
                flag = True
                for ind in range(thresh, len(decoded)-2):
                    if flag:
                        line = decoded[ind:ind + 2]
                    if line not in dct:
                        dct.append(line)
                        flag = True
                    else:
                        line += decoded[ind + 2]
                        flag = False
                if (len(dct) - 1) >= int(elm):
                    decoded += dct[int(elm)]
                else:
                    print("wrong code")
                    return None
                thresh = len(decoded) - 1 - len(line) - 1
        return decoded


def read_file(name):
    """
    Reads file
    """
    with open(name, "r", encoding="utf-8") as fff:
        lines = fff.readlines()
    lines = "".join(lines)
    return lines

def write_file(name, text):
    """
    Reads file
    """
    # text = [str(elm) for elm in text]
    # text = " ".join(text)
    # print(len(text))
    with open(name, "wb") as fff:
        fff.write(text)
    return None

import sys
import os
code = LZW()
# strr = read_file("text.txt")
# print(len(strr))
# coded = code.encode(strr)
# decoded = code.decode(coded)
# print(coded[1])
# print(coded)
strr = "ababahalamaha"
cod, dct = code.encode(strr)
print(code.decode(cod, dct))
# write_file("code.txt", coded)
# text_stats = os.stat("text.txt")
# code_stats = os.stat("code.txt")
# print(f"text size: {text_stats} mb")
# print(f"code size: {code_stats} mb")
# print(f"text size: {len(strr)}")
# print(f"coded size: {len(coded)}")

# print(f"coded size: {sys.getsizeof(coded)/1000000} mb")
# print(f"decoded size: {sys.getsizeof(decoded)/1000000} mb")