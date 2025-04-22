def isSameTree(p, q):
    queueP = [p]
    queueQ = [q]
    while queueP or queueQ:
        if len(queueP) != len(queueQ):
            return False
        if len(queueP) == len(queueQ) == 0:
            return True
        
        currentP = queueP.pop(0)
        currentQ = queueQ.pop(0)

        if currentP is None or currentQ is None:
            if currentP is None and currentQ is None:
                continue
            return False
        
        if currentP.val != currentQ.val:
            return False
        queueP.append(currentP.left)
        queueP.append(currentP.right)
        queueQ.append(currentQ.left)
        queueQ.append(currentQ.right)
    
    return True