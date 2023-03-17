# Coding_Theory

## Division of labor
Savorona Kodtyantin - LZ77 encoding, decoding; LZ77 tests; Huffman encoding; README.md.
Oleksandr Ivaniuk - LZW encoding, decoding; LZW, Huffman tests; Huffman decoding.

## Testing
Algorithm testing is in the corresponding files along with graphs and compression ratio.

## Shortly about algorithms
### LZ77
Algorithm LZ77 best works with repeated fragments of data. It's effective to compress text files, as computer code or documents. However, it works best with small files, but as the file size increases, the efficiency of lz77 decreases

### LZW
Algorithm LZW usually works better with big files, which has a lot of unique elements, for example, screenshots, images. Its advantage is that LZW compress files without data loss, in other words, without losing quality of file.

### Huffman
Huffman's algorithm is effective for compression files with a lot of repeated elements, as text files or logs files. It works better with small files. Huffman data compression is usually used when compressing images and video.

## General cinclusion
Overall, LZ77 nowadays is rarely used, because there are better algorithms. The main advantage of the LZW algorithm is its ability to efficiently compress large files with many unique characters. The main advantage of Huffman encoding is that it can compress data quickly and efficiently, especially for files with a large number of repeated characters.
