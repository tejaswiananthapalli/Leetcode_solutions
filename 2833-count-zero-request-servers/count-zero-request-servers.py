from collections import defaultdict
from typing import List

class Solution:
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:
        logs.sort(key=lambda log: log[1])
        
        sorted_queries = sorted(enumerate(queries), key=lambda item: item[1])
        
        ans = [0] * len(queries)
        active_servers = defaultdict(int)
        active_count = 0
        
        left = 0
        right = 0
        m = len(logs)
        
        for original_idx, q_time in sorted_queries:
            window_start = q_time - x
            
            while right < m and logs[right][1] <= q_time:
                server_id = logs[right][0]
                if active_servers[server_id] == 0:
                    active_count += 1
                active_servers[server_id] += 1
                right += 1
            
            while left < m and logs[left][1] < window_start:
                server_id = logs[left][0]
                active_servers[server_id] -= 1
                if active_servers[server_id] == 0:
                    active_count -= 1
                left += 1
            
            ans[original_idx] = n - active_count
            
        return ans