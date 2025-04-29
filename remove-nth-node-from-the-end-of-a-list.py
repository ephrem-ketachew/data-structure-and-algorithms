# 19. Remove Nth Node From End of List

# Given the head of a linked list, remove the nth node from the end of the list and return its head.

 

# Example 1:


# Input: head = [1,2,3,4,5], n = 2
# Output: [1,2,3,5]
# Example 2:

# Input: head = [1], n = 1
# Output: []
# Example 3:

# Input: head = [1,2], n = 1
# Output: [1]
 
def removeNthFromEnd(head, n):
    current = head
    length = 1
    
    if not current.next:
        return None
    
    while current.next:
        length += 1
        current = current.next
        
    removed_index = length - n + 1
    index = 1
    
    current = head
    while index < removed_index - 1:
        current = current.next
        index += 1
        
    if index == removed_index:
        return head.next
       
    removed_node = current.next
    if removed_node.next is not None:    
        current.next = removed_node.next
        removed_node.next = None
    else:
        current.next = None
    del removed_node
    
    return head