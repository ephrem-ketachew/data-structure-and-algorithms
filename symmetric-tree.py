def isSymmetric(root):
    if root.left is None or root.right is None:
        return root.left is None and root.right is None
    
    p = root.left
    q = root.right

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
        queueQ.append(currentQ.right)
        queueQ.append(currentQ.left)
    
    return True