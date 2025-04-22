def inorderTraversal(root):
    output = []

    def traverse(root):
        if root:
            traverse(root.left)
            output.append(root.val)
            traverse(root.right)

    traverse(root)

    return output