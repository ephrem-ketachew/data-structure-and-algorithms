class Solution:
    def sortString(self, s: str) -> str:
        arr = list(set(s))
        arr.sort()
        n = len(s)
        ans = []
        counter = Counter(s)
        while len(ans) < n:
            k = 0
            while k < len(arr) and len(ans) < n:
                if counter[arr[k]] == 0:
                    k += 1
                    continue
                counter[arr[k]] -= 1
                ans.append(arr[k])
                k += 1

            k = len(arr) - 1
            while k >= 0 and len(ans) < n:
                if counter[arr[k]] == 0:
                    k -= 1
                    continue
                counter[arr[k]] -= 1
                ans.append(arr[k])
                k -= 1

        return ''.join(ans)
