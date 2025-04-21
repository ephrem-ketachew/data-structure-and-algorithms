def romanToInt(s):
    num = 0
    i = 0
    translate = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
    while i < len(s):
        if s[i] == 'I' and i + 1 < len(s):
            if s[i + 1] == 'V':
                num += 4
                i += 1
            elif s[i + 1] == 'X':
                num += 9
                i += 1
            else:
                num += translate[s[i]]
        elif s[i] == 'X' and i + 1 < len(s):
            if s[i + 1] == 'L':
                num += 40
                i += 1
            elif s[i + 1] == 'C':
                num += 90
                i += 1
            else:
                num += translate[s[i]]
        elif s[i] == 'C' and i + 1 < len(s):
            if s[i + 1] == 'D':
                num += 400
                i += 1
            elif s[i + 1] == 'M':
                num += 900
                i += 1
            else:
                num += translate[s[i]]
        else:
            num += translate[s[i]]
        i += 1
    return num