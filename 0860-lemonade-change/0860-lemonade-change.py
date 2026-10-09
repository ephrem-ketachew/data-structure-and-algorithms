class Solution:
    def lemonadeChange(self, bills: list[int]) -> bool:
        bill_5 = bill_10 = 0
        for bill in bills:
            if bill == 5:
                bill_5 += 1
            elif bill == 10:
                if bill_5 == 0:
                    return False
                bill_10 += 1
                bill_5 -= 1
            else:
                if not (bill_5 >= 3 or (bill_10 >= 1 and bill_5 >= 1)):
                    return False
                if bill_10 > 0:
                    bill_10 -= 1
                    bill_5 -= 1
                else:
                    bill_5 -= 3

        return True

