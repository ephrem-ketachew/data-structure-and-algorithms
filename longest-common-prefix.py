def longestCommonPrefix(strs):
    prefix = ''
    for i in range(len(strs[0])):
        isCommonChar = True
        for j in range(1, len(strs)):
            if i >= len(strs[j]) or strs[0][i] != strs[j][i]:
                isCommonChar = False
        if isCommonChar:
            prefix += strs[0][i]
        else:
            break
    return prefix