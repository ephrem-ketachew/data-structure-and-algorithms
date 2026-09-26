class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        kv = defaultdict(str)
        for key, value in knowledge:
            kv[key] = value

        ans = []
        temp = []
        for char in s:
            if char == '(' or char == ')':
                if char == ')':
                    key = ''.join(temp)
                    temp = kv[key] if kv[key] else ['?']
                ans.extend(temp)
                temp = []
            else:
                temp.append(char)

        ans.extend(temp)

        return ''.join(ans)
