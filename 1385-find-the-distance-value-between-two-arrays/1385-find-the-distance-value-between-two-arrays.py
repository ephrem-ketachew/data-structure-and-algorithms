class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        count = 0
        arr2.sort()
        
        for num in arr1:
            index = bisect.bisect_left(arr2, num - d)
            if index < len(arr2) and arr2[index] <= num + d:
                continue
            count += 1
            
        return count