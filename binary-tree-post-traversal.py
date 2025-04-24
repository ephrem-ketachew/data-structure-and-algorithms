def postorderTraversal(root):
    output = []
    def traverse(node):
        if node:
            traverse(node.left)
            traverse(node.right)
            output.append(node.val)

    traverse(root)
    
    return output