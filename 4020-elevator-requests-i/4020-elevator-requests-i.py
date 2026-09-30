class Solution:
    def elevatorRequests(self, n: int, requests: list[int]) -> int:
        time = 0
        prev = 0
        for num in requests:
            time += abs(num - prev)
            prev = num

        return time