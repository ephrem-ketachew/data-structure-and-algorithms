class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while len(s) > k:
            new_s = ''
            for i in range(0, len(s), k):
                sub_k = s[i:i+k]
                print(sub_k, s)
                temp = 0
                for d in sub_k:
                    temp += int(d)
                new_s += str(temp)
            s = new_s

        return s
