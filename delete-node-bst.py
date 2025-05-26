# 450. Delete Node in a BST

# Given a root node reference of a BST and a key, delete the node with the given key in the BST. Return the root node reference (possibly updated) of the BST.

# Basically, the deletion can be divided into two stages:

# Search for a node to remove.
# If the node is found, delete the node.
 

# Example 1:


# Input: root = [5,3,6,2,4,null,7], key = 3
# Output: [5,4,6,2,null,null,7]
# Explanation: Given key to delete is 3. So we find the node with value 3 and delete it.
# One valid answer is [5,4,6,2,null,null,7], shown in the above BST.
# Please notice that another valid answer is [5,2,6,null,4,null,7] and it's also accepted.

# Example 2:

# Input: root = [5,3,6,2,4,null,7], key = 0
# Output: [5,3,6,2,4,null,7]
# Explanation: The tree does not contain a node with value = 0.
# Example 3:

# Input: root = [], key = 0
# Output: []

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root is None:
            return None
        if root.val == key:
            if root.left == None:
                root = root.right
            elif root.right == None:
                root = root.left
            else:
                before = root
                after = root.left
                if after.right is None:
                    root = after
                    after.right = before.right
                    before.left = before.right = None
                else:
                    while after.right:
                        before = after
                        after = after.right
                    before.right = after.left
                    root.val = after.val
                    
            return root
                
            
        parent_node = None
        direction = ''
        current_node = root
        
        while True:
            if key < current_node.val:
                if current_node.left:
                    if current_node.left.val == key:
                        parent_node = current_node
                        direction = 'left'
                        break
                    current_node = current_node.left
                else:
                    return root
            
            if key > current_node.val:
                if current_node.right:
                    if current_node.right.val == key:
                        parent_node = current_node
                        direction = 'right'
                        break
                    current_node = current_node.right
                else:
                    return root
                
        print(parent_node)  
        if direction == 'right':
            if parent_node.right.right == None:
                parent_node.right = parent_node.right.left
            elif parent_node.right.left == None:
                parent_node.right = parent_node.right.right
            else:
                before = parent_node.right
                after = parent_node.right.left
                if after.right is None:
                    parent_node.right = after
                    after.right = before.right
                    # before.left = before.right = None
                else:
                    while after.right:
                        before = after
                        after = after.right
                    before.right = after.left
                    parent_node.right.val = after.val
        
        if direction == 'left':
            if parent_node.left.right == None:
                parent_node.left = parent_node.left.left
            elif parent_node.left.left == None:
                parent_node.left = parent_node.left.right
            else:
                before = parent_node.left
                after = parent_node.left.left
                if after.right is None:
                    parent_node.left = after
                    after.right = before.right
                    # before.left = before.right = None
                else:
                    while after.right:
                        before = after
                        after = after.right
                    before.right = after.left
                    parent_node.left.val = after.val
                
        return root
 