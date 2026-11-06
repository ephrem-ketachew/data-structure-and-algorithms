class Solution:
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:
        logs.sort(key= lambda x:x[1])
        sorted_queries = sorted([(q, i) for i, q in enumerate(queries)])
        active_servers = set()
        server_count = defaultdict(int)
        left = right = 0
        ans = [0] * len(queries)
        
        for query, index in sorted_queries:
            while right < len(logs) and logs[right][1] <= query:
                server, time = logs[right]
                server_count[server] += 1
                active_servers.add(server)
                right += 1
                
            while left < len(logs) and logs[left][1] < query - x:
                server, time = logs[left]
                server_count[server] -= 1
                if server_count[server] == 0:
                    active_servers.discard(server)
                left += 1
                
            ans[index] = n - len(active_servers)
            
        return ans