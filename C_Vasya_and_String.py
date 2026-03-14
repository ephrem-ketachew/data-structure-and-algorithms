# C. Vasya and String
# time limit per test1 second
# memory limit per test256 megabytes
# High school student Vasya got a string of length n as a birthday present. This string consists of letters 'a' and 'b' only. Vasya denotes beauty of the string as the maximum length of a substring (consecutive subsequence) consisting of equal letters.

# Vasya can change no more than k characters of the original string. What is the maximum beauty of the string he can achieve?

# Input
# The first line of the input contains two integers n and k (1 ≤ n ≤ 100 000, 0 ≤ k ≤ n) — the length of the string and the maximum number of characters to change.

# The second line contains the string, consisting of letters 'a' and 'b' only.

# Output
# Print the only integer — the maximum beauty of the string Vasya can achieve by changing no more than k characters.

# Examples
# InputCopy
# 4 2
# abba
# OutputCopy
# 4
# InputCopy
# 8 1
# aabaabaa
# OutputCopy
# 5
# Note
# In the first sample, Vasya can obtain both strings "aaaa" and "bbbb".

# In the second sample, the optimal answer is obtained with the string "aaaaabaa" or with the string "aabaaaaa".

from collections import Counter

n, k = map(int, input().split())
s = input().strip()

counter = Counter()
left = 0
max_freq = 0
max_len = 0
for right in range(n):
    counter[s[right]] += 1
    max_freq = max(max_freq, counter[s[right]])
    
    while (right - left + 1) - max_freq > k:
        counter[s[left]] -= 1
        left += 1
        
    max_len = max(max_len, right - left + 1)
    
print(max_len)