# A. Chat room
# time limit per test1 second
# memory limit per test256 megabytes
# Vasya has recently learned to type and log on to the Internet. He immediately entered a chat room and decided to say hello to everybody. Vasya typed the word s. It is considered that Vasya managed to say hello if several letters can be deleted from the typed word so that it resulted in the word "hello". For example, if Vasya types the word "ahhellllloou", it will be considered that he said hello, and if he types "hlelo", it will be considered that Vasya got misunderstood and he didn't manage to say hello. Determine whether Vasya managed to say hello by the given word s.

# Input
# The first and only line contains the word s, which Vasya typed. This word consisits of small Latin letters, its length is no less that 1 and no more than 100 letters.

# Output
# If Vasya managed to say hello, print "YES", otherwise print "NO".

# Examples
# InputCopy
# ahhellllloou
# OutputCopy
# YES
# InputCopy
# hlelo
# OutputCopy
# NO

import sys

input = sys.stdin.readline

s = input()

# 1) WRONG ASSUMPTION

# i = 0
# made = 0
# while i < len(s):
#     if s[i] == 'h':
#         while i + 1 < len(s) and s[i + 1] == 'h':
#             i += 1
#         made = 1
#     elif s[i] == 'e' and made == 1:
#         while i + 1 < len(s) and s[i + 1] == 'e':
#             i += 1
#         made += 1
#     elif s[i] == 'l' and i + 1 < len(s) and s[i + 1] == 'l' and made == 2:
#         while i + 1 < len(s) and s[i + 1] == 'l':
#             i += 1
#         made += 1
#     elif s[i] == 'o' and made == 3:
#         made += 1
#         break
#     else:
#         made = 0
    
#     i += 1
    
# if made == 4:
#     print('YES')
# else:
#     print('NO')


# 2) BRUTE FORCE
# found = False

# for i in range(len(s)):
#     if found:
#         break
#     if s[i] == 'h':
#         for j in range(i + 1, len(s)):
#             if found:
#                 break
#             if s[j] == 'e':
#                 for k in range(j + 1, len(s)):
#                     if found:
#                         break
#                     if s[k] == 'l':
#                         for l in range(k + 1, len(s)):
#                             if found:
#                                 break
#                             if s[l] == 'l':
#                                 for m in range(l + 1, len(s)):
#                                     if s[m] == 'o':
#                                         found = True
#                                         break
                                
# if found:
#     print('YES')
# else:
#     print('NO')


# THE INTENDED WAY

hello = 'hello'
j = 0

for i in range(len(s)):
    if s[i] == hello[j]:
        j += 1
        
    if j == len(hello):
        print('YES')
        break
  
if j < len(hello):  
    print('NO')