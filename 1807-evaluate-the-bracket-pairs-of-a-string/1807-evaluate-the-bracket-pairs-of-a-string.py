class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        kv = defaultdict(str)
        for key, value in knowledge:
            kv[key] = value

        ans = temp = ''
        for char in s:
            if char == '(' or char == ')':
                if char == ')':
                    temp = kv[temp] if kv[temp] else '?'
                ans += temp
                temp = ''
            else:
                temp += char

        ans += temp

        return ans
