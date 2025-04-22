def maxDetph(root):
    if not root:
        return 0
    
    queue = [root]
    depth = 0

    while queue:
        for i in range(len(queue)):
            current = queue.pop(0)
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
        depth += 1
    
    return depth