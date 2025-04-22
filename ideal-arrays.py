def idealArrays(n, maxValue):
    open = []
    numberOfIdealArrays = 0
    for i in range(1, maxValue + 1):
        open.append([i])
    while len(open) > 0:
        endIndex = len(open[0]) - 1
        lastElement = open[0][endIndex]
        for i in range(lastElement, maxValue + 1):
            if i % lastElement == 0:
                newList = open[0][:]
                newList.append(i)
                if len(newList) == n:
                    numberOfIdealArrays += 1
                else:
                    open.append(newList)
        open.remove(open[0])
        
    return numberOfIdealArrays