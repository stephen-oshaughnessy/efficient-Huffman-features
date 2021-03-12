from eHf import encode

# note: plain strings require the binary b prefix
s = b"AAABBBBBCCCDDDEEEEEEEEEEEE12345"

# prints the ehf features for the input string
print(encode(s))