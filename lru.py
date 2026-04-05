class ListNode:
    def __init__(self, key=0, val=0):
        self.val = val
        self.key = key
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        
        self.head = ListNode(-1, -1)
        self.tail = ListNode(-1, -1)
        
        self.head.next = self.tail
        self.tail.prev = self.head
        
    def _remove(self, node: ListNode) -> None:
        prev_node = node.prev
        prev_node.next = node.next
        node.next.prev = prev_node
        
    def _add_at_head(self, node: ListNode) -> None:
        next_node = self.head.next
        
        node.next = next_node
        next_node.prev = node
        
        self.head.next = node
        node.prev = self.head
        
       
    def get(self, key: int) -> int:
        if not key in self.cache:
            return -1
        
        node = self.cache[key]
        self._remove(node)
        self._add_at_head(node)
        
        return node.val
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)
            node.val = value
            self._add_at_head(node)
        else:
            node = ListNode(key, value)
            self.cache[key] = node
            self._add_at_head(node)
            
            if len(self.cache) > self.capacity:
                lru = self.tail.prev
                self._remove(lru)
                del self.cache[lru.key]
        

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)