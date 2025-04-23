def minimumRecolors(blocks,k):
    minRecolor = float('inf')
    i = 0
    while i < len(blocks) + 1 - k:
        block = blocks[i:i + k]
        if block.count('W') < minRecolor:
            minRecolor = block.count('W')
        i += 1

    return minRecolor