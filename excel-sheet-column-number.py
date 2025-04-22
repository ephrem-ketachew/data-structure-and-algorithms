def titleToNumber(columnTitle):
    number = 0
    multiplier = 1
    for i in range(len(columnTitle) - 1, -1, -1):
        number += (ord(columnTitle[i]) - 64) * multiplier
        multiplier *= 26
    return number