def generateParentheses(n):
    open = ['*' *2 * n]
    closed = []
    while len(open) > 0:
        if open[0].count('(') < n:
            newPattern = open[0].replace('*','(', 1)
            if '*' in newPattern:
                open.append(newPattern)
            else:
                closed.append(newPattern)
        if open[0].count(')') < open[0].count('('):
            newPattern = open[0].replace('*',')', 1)
            if '*' in newPattern:
                open.append(newPattern)
            else:
                closed.append(newPattern)
        open.pop(0)
    return closed