class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        kv = defaultdict(str)
        for key, value in knowledge:
            kv[key] = value

        ans = []
        i = 0
        while i < len(s):
            if s[i] == '(':
                j = s.find(')', i + 1)
                key = s[i+1:j]
                if kv[key]:
                    ans.append(kv[key])
                else:
                    ans.append('?')
                i = j + 1
            else:
                ans.append(s[i])
                i += 1

        return ''.join(ans)
