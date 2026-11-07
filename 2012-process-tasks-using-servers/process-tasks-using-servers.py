import heapq

class Solution:
    def assignTasks(self, servers: list[int], tasks: list[int]) -> list[int]:
        free = [(servers[i], i) for i in range(len(servers))]
        heapq.heapify(free)
        busy = []
        
        ans = []
        curr_time = 0
        
        for i in range(len(tasks)):
            curr_time = max(curr_time, i)
            
            if not free and busy[0][0] > curr_time:
                curr_time = busy[0][0]
                
            while busy and busy[0][0] <= curr_time:
                free_time, weight, idx = heapq.heappop(busy)
                heapq.heappush(free, (weight, idx))
                
            weight, idx = heapq.heappop(free)
            ans.append(idx)
            heapq.heappush(busy, (curr_time + tasks[i], weight, idx))
            
        return ans