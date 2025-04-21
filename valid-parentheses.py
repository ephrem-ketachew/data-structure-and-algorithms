def isValid(str):
    closing = { '(':')', '[':']', '{':'}'}
    while len(str) > 0:
        i = 0
        while i < len(str):
            if(i + 1 < len(str) and str[i] in closing and closing[str[i]] == str[i + 1]):
                str = str[:i] + str[i + 2:]
                i = -1
            i += 1
        else:
            break
    return len(str) == 0