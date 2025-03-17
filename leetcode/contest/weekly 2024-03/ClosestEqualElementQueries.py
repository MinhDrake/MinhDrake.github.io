import enum
from typing import List
import bisect


class Solution:
    def min_circular_queries(self, n: int, i: int, j: int) -> int:
        return min(abs(i-j), n - abs(i-j))

    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        n = len(nums)
        indices = {}
        for i, num in enumerate(nums):
            if num not in indices:
                indices[num] = []
            indices[num].append(i)

        res = []
        for query in queries:
            val = nums[query]
            pos_list = indices[val]
            if len(pos_list) == 1:
                res.append(-1)
                continue
            pos = bisect.bisect_left(pos_list, query)

            candidates = []
            if pos < len(pos_list) - 1:
                candidates.append(pos_list[pos+1])
            if pos > 0:
                candidates.append(pos_list[pos-1])

            # Also consider
            candidates.append(pos_list[0])
            candidates.append(pos_list[-1])

            best_distance = float('inf')
            for j in candidates:
                if query != j:
                    distance = self.min_circular_queries(n, query, j)
                    best_distance = min(best_distance, distance)
            res.append(best_distance)
        return res


solution = Solution()
print(solution.solveQueries([1, 3, 1, 4, 1, 3, 2], [0, 3, 5]))
