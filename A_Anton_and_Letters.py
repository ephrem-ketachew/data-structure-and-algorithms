# A. Anton and Letters
# time limit per test2 seconds
# memory limit per test256 megabytes
# Recently, Anton has found a set. The set consists of small English letters. Anton carefully wrote out all the letters from the set in one line, separated by a comma. He also added an opening curved bracket at the beginning of the line and a closing curved bracket at the end of the line.

# Unfortunately, from time to time Anton would forget writing some letter and write it again. He asks you to count the total number of distinct letters in his set.

# Input
# The first and the single line contains the set of letters. The length of the line doesn't exceed 1000. It is guaranteed that the line starts from an opening curved bracket and ends with a closing curved bracket. Between them, small English letters are listed, separated by a comma. Each comma is followed by a space.

# Output
# Print a single number — the number of distinct letters in Anton's set.

# Examples
# InputCopy
# {a, b, c}
# OutputCopy
# 3
# InputCopy
# {b, a, b, a}
# OutputCopy
# 2
# InputCopy
# {}
# OutputCopy
# 0

import sys

input = sys.stdin.readline

my_input = input()[1:-2].split(',')

chars = [ch.strip() for ch in my_input]
unique_chars = set(chars)

if '' in unique_chars:
    unique_chars.remove('')
    
print(len(unique_chars))