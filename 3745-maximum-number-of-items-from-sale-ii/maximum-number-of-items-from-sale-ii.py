from collections import defaultdict
from typing import List


class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        max_factor = max(f for f, _ in items)
        min_price = min(p for _, p in items)

        freq = [0] * (max_factor + 1)
        for f, _ in items:
            freq[f] += 1

        multiples_count = [0] * (max_factor + 1)
        for f in range(1, max_factor + 1):
            if freq[f]:
                for m in range(f, max_factor + 1, f):
                    multiples_count[f] += freq[m]

        cost_to_frees = defaultdict(int)
        for f, p in items:
            if p < 2 * min_price:
                cost_to_frees[p] += multiples_count[f] - 1

        total = 0
        for p in sorted(cost_to_frees):
            if budget < p:
                break
            take = min(cost_to_frees[p], budget // p)
            total += 2 * take
            budget -= take * p

        total += budget // min_price
        return total