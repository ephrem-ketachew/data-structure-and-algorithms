# 641. Design Circular Deque
# Medium

# Design your implementation of the circular double-ended queue (deque).

# Implement the MyCircularDeque class:

# MyCircularDeque(int k) Initializes the deque with a maximum size of k.
# boolean insertFront() Adds an item at the front of Deque. Returns true if the operation is successful, or false otherwise.
# boolean insertLast() Adds an item at the rear of Deque. Returns true if the operation is successful, or false otherwise.
# boolean deleteFront() Deletes an item from the front of Deque. Returns true if the operation is successful, or false otherwise.
# boolean deleteLast() Deletes an item from the rear of Deque. Returns true if the operation is successful, or false otherwise.
# int getFront() Returns the front item from the Deque. Returns -1 if the deque is empty.
# int getRear() Returns the last item from Deque. Returns -1 if the deque is empty.
# boolean isEmpty() Returns true if the deque is empty, or false otherwise.
# boolean isFull() Returns true if the deque is full, or false otherwise.

# Example 1:

# Input
# ["MyCircularDeque", "insertLast", "insertLast", "insertFront", "insertFront", "getRear", "isFull", "deleteLast", "insertFront", "getFront"]
# [[3], [1], [2], [3], [4], [], [], [], [4], []]
# Output
# [null, true, true, true, false, 2, true, true, true, 4]

# Explanation
# MyCircularDeque myCircularDeque = new MyCircularDeque(3);
# myCircularDeque.insertLast(1);  // return True
# myCircularDeque.insertLast(2);  // return True
# myCircularDeque.insertFront(3); // return True
# myCircularDeque.insertFront(4); // return False, the queue is full.
# myCircularDeque.getRear();      // return 2
# myCircularDeque.isFull();       // return True
# myCircularDeque.deleteLast();   // return True
# myCircularDeque.insertFront(4); // return True
# myCircularDeque.getFront();     // return 4

# Constraints:

# 1 <= k <= 1000
# 0 <= value <= 1000
# At most 2000 calls will be made to insertFront, insertLast, deleteFront, deleteLast, getFront, getRear, isEmpty, isFull.

from collections import deque

class ListNode:
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = None
        self.prev = None

class MyCircularDeque:

    # def __init__(self, k: int):
    #     self.queue = deque()
    #     self.max_size = k
        
    # def insertFront(self, value: int) -> bool:
    #     if len(self.queue) < self.max_size:
    #         self.queue.appendleft(value)
    #         return True
    #     return False

    # def insertLast(self, value: int) -> bool:
    #     if len(self.queue) < self.max_size:
    #         self.queue.append(value)
    #         return True
    #     return False

    # def deleteFront(self) -> bool:
    #     if self.queue:
    #         self.queue.popleft()
    #         return True
    #     return False

    # def deleteLast(self) -> bool:
    #     if self.queue:
    #         self.queue.pop()
    #         return True
    #     return False

    # def getFront(self) -> int:
    #     if self.queue:
    #         return self.queue[0]
    #     return -1

    # def getRear(self) -> int:
    #     if self.queue:
    #         return self.queue[-1]
    #     return -1

    # def isEmpty(self) -> bool:
    #     return len(self.queue) == 0

    # def isFull(self) -> bool:
    #     return len(self.queue) == self.max_size

    def __init__(self, k: int):
        self.head = ListNode()
        self.tail = ListNode()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.max_size = k
        self.cur_size = 0
        
    def insertFront(self, value: int) -> bool:
        if self.cur_size < self.max_size:
            node = ListNode(value)
            node.next = self.head.next
            node.prev = self.head
            self.head.next.prev = node
            self.head.next = node
            self.cur_size += 1
            return True
        return False

    def insertLast(self, value: int) -> bool:
        if self.cur_size < self.max_size:
            node = ListNode(value)
            node.next = self.tail
            node.prev = self.tail.prev
            self.tail.prev.next = node
            self.tail.prev = node
            self.cur_size += 1
            return True
        return False

    def deleteFront(self) -> bool:
        if self.cur_size > 0:
            self.head.next.next.prev = self.head
            self.head.next = self.head.next.next
            self.cur_size -= 1
            return True
        return False

    def deleteLast(self) -> bool:
        if self.cur_size > 0:
            self.tail.prev.prev.next = self.tail
            self.tail.prev = self.tail.prev.prev
            self.cur_size -= 1
            return True
        return False

    def getFront(self) -> int:
        if self.cur_size > 0:
            return self.head.next.val
        return -1

    def getRear(self) -> int:
        if self.cur_size > 0:
            return self.tail.prev.val
        return -1

    def isEmpty(self) -> bool:
        return self.cur_size == 0

    def isFull(self) -> bool:
        return self.cur_size == self.max_size

# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()