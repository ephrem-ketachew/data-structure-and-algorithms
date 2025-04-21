# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(list1, list2):
    head = ListNode()
    currentNode = head
    while list1 and list2:
        if list1.val <= list2.val:
            currentNode.next = list1
            currentNode = currentNode.next
            list1 = list1.next
        else:
            currentNode.next = list2
            currentNode = currentNode.next
            list2 = list2.next

    while list1:
        currentNode.next = list1
        currentNode = currentNode.next
        list1 = list1.next
    while list2:
        currentNode.next = list2
        currentNode = currentNode.next
        list2 = list2.next

    return head.next