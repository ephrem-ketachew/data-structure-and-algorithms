def convertToTitle(columnNumber):
    result = ''
    while columnNumber > 0:
        quotient = columnNumber % 26
        columnNumber //= 26
        if quotient == 0:
            quotient = 26
            columnNumber -= 1
        result = chr(quotient + 64) + result
    return result
