from enum import unique
from typing import List


class Solution:
    def maxSum(self, nums: List[int]) -> int:
        if not nums:
            return 0
        unique_positives = set()
        for num in nums:
            if num > 0:
                unique_positives.add(num)

        if unique_positives:
            return sum(unique_positives)
        else:
            return max(nums)  # return least negative


solution = Solution()
print(solution.maxSum([1, 2, 3, 4, 5]))  # 15
print(solution.maxSum([1, 1, 0, 1, 1]))
print(solution.maxSum([]))
print(solution.maxSum([1, 2, -1, -2, 1, 0, -1]))
