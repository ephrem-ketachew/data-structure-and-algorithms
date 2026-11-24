class Solution:
    def maxLength(self, nums: List[int]) -> int:        
        max_len = 1
        for i in range(len(nums)):
            prod = gcd = lcm = nums[i]
            for j in range(i - 1, -1, -1):
                prod *= nums[j]
                gcd = math.gcd(gcd, nums[j])
                lcm = math.lcm(lcm, nums[j])
                if prod == lcm * gcd:
                    max_len = max(max_len, i - j + 1)
                    
        return max_len