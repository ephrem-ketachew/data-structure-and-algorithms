class Solution:
    def lemonadeChange(self, bills: list[int]) -> bool:
        s5 = 0
        s10 = 0
        for b in bills:
            if b == 5:
                s5 += 1
            elif b == 10:
                if s5 == 0:
                    return False
                s10 += 1
                s5 -= 1
            else:
                if not (s5 >= 3 or (s10 >= 1 and s5 >= 1)):
                    return False
                if s10 > 0:
                    s10 -= 1
                    s5 -= 1
                else:
                    s5 -= 3

        return True

