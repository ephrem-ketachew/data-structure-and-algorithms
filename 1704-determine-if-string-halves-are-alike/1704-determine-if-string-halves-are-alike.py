class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = 'aeiou'
        s = s.lower()
        first = second = 0
        for i, ch in enumerate(s):
            if ch in vowels:
                if i < len(s) // 2:
                    first += 1
                else:
                    second += 1
        
        return first == second