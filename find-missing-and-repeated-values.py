def findMissingAndRepeatedValues(grid):
    s = set(range(1, len(grid) ** 2 + 1))
    print(s)
    values = []
    for row in grid:
        for el in row:
            if el in s:
                s.remove(el)
            else:
                values.append(el)
    values.append(s.pop()) 
    return values