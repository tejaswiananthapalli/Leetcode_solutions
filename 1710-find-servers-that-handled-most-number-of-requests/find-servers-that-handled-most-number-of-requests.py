import heapq
from sortedcontainers import SortedList

class Solution:
    def busiestServers(self, k: int, arrival: list[int], load: list[int]) -> list[int]:
        count = [0] * k
        available = SortedList(range(k))
        busy = []
        
        for i, (start, duration) in enumerate(zip(arrival, load)):
            while busy and busy[0][0] <= start:
                _, server_id = heapq.heappop(busy)
                available.add(server_id)
            
            if not available:
                continue
            
            target = i % k
            idx = available.bisect_left(target)
            
            if idx == len(available):
                idx = 0
                
            server_id = available[idx]
            
            count[server_id] += 1
            available.remove(server_id)
            heapq.heappush(busy, (start + duration, server_id))
            
        max_requests = max(count)
        return [i for i, cnt in enumerate(count) if cnt == max_requests]