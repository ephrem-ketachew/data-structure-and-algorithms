# 297. Serialize and Deserialize Binary Tree
# Hard

# Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

# Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.

# Clarification: The input/output format is the same as how LeetCode serializes a binary tree. You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.

# Example 1:

# Input: root = [1,2,3,null,null,4,5]
# Output: [1,2,3,null,null,4,5]
# Example 2:

# Input: root = []
# Output: []

# Constraints:

# The number of nodes in the tree is in the range [0, 104].
# -1000 <= Node.val <= 1000

from collections import deque

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ''
        
        encoded = []
        queue = deque([root])
        while queue:
            node = queue.popleft()
            if node:
                encoded.append(str(node.val))
                
                queue.append(node.left)
                queue.append(node.right)
            else:
                encoded.append('n')
            
        return ','.join(encoded)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        
        encoded = data.split(',')
        root_val = int(encoded[0])
        i, levels = 1, len(encoded)
        root = TreeNode(root_val)
        queue = deque([root])
        
        while i < levels and queue:
            node = queue.popleft()
            if encoded[i] != 'n':
                node.left = TreeNode(int(encoded[i]))
                queue.append(node.left)
            i += 1
            
            if encoded[i] != 'n':
                node.right = TreeNode(int(encoded[i]))
                queue.append(node.right)     
            i += 1  
         
        
        return root
    

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))