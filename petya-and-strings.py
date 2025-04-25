# A. Petya and Strings
# time limit per test2 seconds
# memory limit per test256 megabytes
# Little Petya loves presents. His mum bought him two strings of the same size for his birthday. The strings consist of uppercase and lowercase Latin letters. Now Petya wants to compare those two strings lexicographically. The letters' case does not matter, that is an uppercase letter is considered equivalent to the corresponding lowercase letter. Help Petya perform the comparison.

# Input
# Each of the first two lines contains a bought string. The strings' lengths range from 1 to 100 inclusive. It is guaranteed that the strings are of the same length and also consist of uppercase and lowercase Latin letters.

# Output
# If the first string is less than the second one, print "-1". If the second string is less than the first one, print "1". If the strings are equal, print "0". Note that the letters' case is not taken into consideration when the strings are compared.

# Examples
# Input
# aaaa
# aaaA
# Output
# 0
# Input
# abs
# Abz
# Output
# -1
# Input
# abcdefg
# AbCdEfF
# Output

first_string = input().lower()
second_string = input().lower()

for i in range(len(first_string)):
    if first_string[i] != second_string[i]:
        print(1 if ord(first_string[i]) - ord(second_string[i]) > 0 else -1)
        break
else:
    print(0)