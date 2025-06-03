# 147. Insertion Sort List

# Given the head of a singly linked list, sort the list using insertion sort, and return the sorted list's head.

# The steps of the insertion sort algorithm:

# Insertion sort iterates, consuming one input element each repetition and growing a sorted output list.
# At each iteration, insertion sort removes one element from the input data, finds the location it belongs within the sorted list and inserts it there.
# It repeats until no input elements remain.
# The following is a graphical example of the insertion sort algorithm. The partially sorted list (black) initially contains only the first element in the list. One element (red) is removed from the input data and inserted in-place into the sorted list with each iteration.

# Example 1:

# Input: head = [4,2,1,3]
# Output: [1,2,3,4]
# Example 2:


# Input: head = [-1,5,3,4,0]
# Output: [-1,0,3,4,5]
 
# Constraints:

# The number of nodes in the list is in the range [1, 5000].
# -5000 <= Node.val <= 5000

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # This is My coding problem solving journey.... believe it or not I wasted about 150 mins solving this question the right way, I mean I solved it and got accepted early but it turns out the question wasn't meant to be solved the way I solved... then I tried my hard to come up with a solution(2 approaches codes below the main solution), both of them exceeded the time limit and ....I finally gave up and saw the solution ...and indeed I was close enough but missed one point which is I don't need to unlink and link the connection between the current node and the previous node..... I mean the list is built independently on the dummy_node chain.... was my suffering worth ...dunno
        
        
        # This code wroks but it is not the way the problem is meant to be solved, I mean I only swap the values in place
        # current = head
        # while current:
        #     cur = head
        #     while cur.val < current.val:
        #         cur = cur.next
        #     if cur != current:
        #         temp = cur.val
        #         cur.val = current.val
        #         cur = cur.next
        #         while cur != current:
        #             cur.val, temp = temp, cur.val
        #             cur = cur.next
        #         current.val = temp
        #     current = current.next
            
        # return head
        
        dummy_node = ListNode(float('-inf'))
        current = head
        
        while current:
            next_node = current.next
            prev = dummy_node
            while prev.next and prev.next.val < current.val:
                prev = prev.next
            
            current.next = prev.next
            prev.next = current
            
            current = next_node

        return dummy_node.next
    
        # The following codes are here only to show my sufferings and time wastage in solving this problem both of them exceed time limit....
        
        # # current = head
        # # while current:
        # #     prev = cur = head
        # #     while cur.val < current.val:
        # #         prev = cur
        # #         cur = cur.next
        # #     if cur != current:
        # #         current_previous = head
        # #         while current_previous.next != current:
        # #             current_previous = current_previous.next
                
        # #         if cur == prev:
        # #             head = current
        # #         else:
        # #             prev.next = current
                    
        # #         current_previous.next = current.next
        # #         current.next = cur
        # #         current = current_previous
        # #     current = current.next
        
        # # return head
        
        # def prev_node(head, node):
        #     if head == node:
        #         return None
        #     current = head
        #     while current.next != node:
        #         current = current.next
        #     return current
        
        # current = head
        # while current:
        #     current_prev = prev = prev_node(head, current)
        #     while prev and prev.val > current.val:
        #         prev = prev_node(head, prev)
               
        #     if prev:
        #         current_prev.next = current.next
        #         temp = prev.next 
        #         prev.next = current
        #         current.next = temp
                
        #         current = current_prev
        #     elif current_prev:
        #         current_prev.next = current.next
        #         current.next = head
        #         head = current
                
        #         current = current_prev
            
        #     current = current.next
            
        # return head