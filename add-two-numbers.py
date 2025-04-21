# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def createLinkedList(l):
            head = ListNode(l[0])
            i = 1
            currentNode = head
            while i < len(l):
                newNode = ListNode(l[i])
                currentNode.next = newNode
                currentNode = newNode
                i += 1
            return head
        num1 = ''
        num2 = ''
        while l1:
            num1 += str(l1.val)
            l1 = l1.next
        while l2:
            num2 += str(l2.val)
            l2 = l2.next
        num1 = int(num1[::-1])
        num2 = int(num2[::-1])
        num3 = num1 + num2 
        num3 = str(num3)
        num3 = num3[::-1]
        newList = []
        for char in num3:
            newList.append(int(char))
        l3 = createLinkedList(newList)
        return l3