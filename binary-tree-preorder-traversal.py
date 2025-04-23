def preorderTraversal(root):
    output = []
    def traverse(node):
        if node:
            output.append(node.val)
            traverse(node.left)
            traverse(node.right)
    traverse(root)
    return output