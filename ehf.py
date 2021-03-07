import heapq
from collections import Counter


def k_smallest(array):
    """ Returns a dataset of uniform vectors. Each vector is reduced to the min length vector
       - this is necessary if you are passing the feature set to a classification algorithm """
    for k in array:
        del k[min(map(len, array)):]
    return array


def binaryToDecimal(n):
    """convert the binary codeword to an int"""
    return int(n, 2)


def ehf_vector(huff, frequency):
    """combine the symbols, frequencies and codewords as single features"""
    feats = []
    for i in huff:
        feature = i[0] + frequency[i[0]] + binaryToDecimal(i[1])
        feats.append(feature)
    return feats


def encode(data):
    """input: any data sequence, including files
       output: numpy array of Huffman codewords"""

    # get the frequencies of each symbol
    frequency = Counter(data)

    # create a heap with the weight, symbol and an empty string for the codeword
    heap = [[weight, [symbol, '']] for symbol, weight in frequency.items()]
    heapq.heapify(heap)
    while len(heap) > 1:
        leftchild = heapq.heappop(heap)
        rightchild = heapq.heappop(heap)
        for value in leftchild[1:]:
            value[1] = '0' + value[1]
        for value in rightchild[1:]:
            value[1] = '1' + value[1]
        heapq.heappush(heap, [leftchild[0] + rightchild[0]] + leftchild[1:] + rightchild[1:])

    # construct the eHf feature set from the symbols, frequencies and codewords
    codes = sorted(heapq.heappop(heap)[1:], key=lambda p: (len(p[-1]), p))
    return ehf_vector(codes, frequency)
