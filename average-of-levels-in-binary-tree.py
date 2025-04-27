# 637. Average of Levels in Binary Tree
# Easy
# Given the root of a binary tree, return the average value of the nodes on each level in the form of an array.
 

# Example 1:
# Input: root = [3,9,20,null,null,15,7]
# Output: [3.00000,14.50000,11.00000]
# Explanation: The average value of nodes on level 0 is 3, on level 1 is 14.5, and on level 2 is 11.
# Hence return [3, 14.5, 11].

# Example 2:
# Input: root = [3,9,20,15,7]
# Output: [3.00000,14.50000,11.00000]

def averageOfLevels(root):
   queue = [root]
   averages = []
   
   while queue:
       row = []
       row_length = len(queue)
       for i in range(row_length):
           node = queue.pop(0)
           if node:
               row.append(node.val)
               queue.append(node.left)
               queue.append(node.right)
       if row:
           averages.append(sum(row) / len(row))
    
   return averages