from typing import List
from collections import deque
class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        queue = deque((t, i) for i, t in enumerate(tickets))
        time = 0
        while True:
            t, idx = queue.popleft()
            t -= 1
            time += 1
            if t == 0 and idx == k:
                return time
            queue.append((t, idx))