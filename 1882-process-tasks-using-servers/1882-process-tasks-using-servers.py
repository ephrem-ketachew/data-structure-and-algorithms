class Solution:
    def assignTasks(self, servers: list[int], tasks: list[int]) -> list[int]:
        avail = []
        unavail = []
        for i, server in enumerate(servers):
            heapq.heappush(avail, (server, i))

        ans = []
        elapsed = 0
        for i, time in enumerate(tasks):
            if elapsed < i:
                elapsed = i
            while unavail and unavail[0][0] <= elapsed:
                t, ser, k = heapq.heappop(unavail)
                heapq.heappush(avail, (ser, k))
            if not avail:
                t, ser, k = heapq.heappop(unavail)
                heapq.heappush(avail, (ser, k))
                elapsed = t

            server, idx = heapq.heappop(avail)
            ans.append(idx)
            heapq.heappush(unavail, (elapsed + time, server, idx))

        return ans
