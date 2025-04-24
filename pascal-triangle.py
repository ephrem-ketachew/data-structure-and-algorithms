def generate(numRows):
    def getNewRow(n, previousRow):
        newRow = [1]
        for i in range(1, n -1):
            newRow.append(previousRow[i-1] + previousRow[i])
        newRow.append(1)
        return newRow
    
    output = []
    row = [1]
    output.append(row)
    for i in range(2, numRows + 1):
        row = getNewRow(i, row)
        output.append(row)
    
    return output