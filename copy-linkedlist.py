from typing import Optional
from collections import defaultdict


# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        idx_map = defaultdict(int)
        node = head
        i = 0
        while node:
            random_node = node.random
            if random_node == None:
                idx_map[i] = -1
                i += 1
                node = node.next
                continue
            
            j = 0
            temp = head
            while temp != random_node:
                temp = temp.next
                j += 1
                
            idx_map[i] = j
            
            node = node.next
            i += 1
            
        node1 = head
        node2 = dummy_head = Node(0)
        while node1:
            new_node = Node(node1.val)
            node2.next = new_node
            
            node2 = node2.next
            node1 = node1.next
            
        new_head = dummy_head.next
        i = 0
        node = new_head
        while node:
            j = idx_map[i]
            if j == -1:
                i += 1
                node = node.next
                continue
            
            temp = new_head
            for _ in range(j):
                temp = temp.next
                
            node.random = temp
            
            i += 1
            node = node.next
            
        return new_head