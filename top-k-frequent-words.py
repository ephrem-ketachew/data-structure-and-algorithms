# 692. Top K Frequent Words
# Medium
# Given an array of strings words and an integer k, return the k most frequent strings.

# Return the answer sorted by the frequency from highest to lowest. Sort the words with the same frequency by their lexicographical order.

# Example 1:

# Input: words = ["i","love","leetcode","i","love","coding"], k = 2
# Output: ["i","love"]
# Explanation: "i" and "love" are the two most frequent words.
# Note that "i" comes before "love" due to a lower alphabetical order.
# Example 2:

# Input: words = ["the","day","is","sunny","the","the","the","sunny","is","is"], k = 4
# Output: ["the","is","sunny","day"]
# Explanation: "the", "is", "sunny" and "day" are the four most frequent words, with the number of occurrence being 4, 3, 2 and 1 respectively.

# Constraints:

# 1 <= words.length <= 500
# 1 <= words[i].length <= 10
# words[i] consists of lowercase English letters.
# k is in the range [1, The number of unique words[i]]
 

# Follow-up: Could you solve it in O(n log(k)) time and O(n) extra space?

from typing import List
from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        counter = Counter(words)
        # return sorted(counter.keys(), key=lambda word:(-counter[word], word))[:k]
        
        # max_freq = max(counter.values())
        # buckets = [[] for i in range(max_freq + 1)]
        
        # ans = []
        # for word, freq in counter.items():
        #     buckets[freq].append(word)
            
        # for freq in range(len(buckets) - 1, 0, -1):
        #     res = []
        #     for word in buckets[freq]:
        #         res.append(word)
        #     res.sort()
        #     for word in res:
        #         ans.append(word)
        #         if len(ans) == k:
        #             break
        #     if len(ans) == k:
        #         break
            
        # return ans
        
        # res = []
        # for word, freq in counter.items():
        #     heapq.heappush(res, (-freq, word))
                
        # ans = []
        # for i in range(k):
        #     word = heapq.heappop(res)[1]
        #     ans.append(word)
            
        # return ans
        
        class HeapItem:
            def __init__(self, word: str, freq: int) -> None:
                self.word = word
                self.freq = freq
                
            def __lt__(self, item: 'HeapItem') -> bool:
                if item.freq != self.freq:
                    return self.freq < item.freq
                
                return self.word > item.word
            
        res = []
        for word, freq in counter.items():
            heapq.heappush(res, HeapItem(word, freq))
            if len(res) > k:
                heapq.heappop(res)
                
        ans = []
        while res:
            heapItem = heapq.heappop(res)
            ans.append(heapItem.word)
            
        return ans[::-1]