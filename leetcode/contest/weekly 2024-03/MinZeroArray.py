from typing import List


class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        left, right = 1, len(queries)
        res = -1

        while left <= right:
            mid = left + (right - left) // 2
            if self.isValid(nums, queries[:mid]):
                answer = mid
                high = mid - 1
            else:
                low = mid + 1

        return answer

    def isValid(self, nums: List[int], queries_subset: List[List[int]]) -> bool:
        for i in range(len(nums)):
            coins = []
            for l, r, v in queries_subset:
                if l <= i <= r:
                    coins.append(v)
            if not self.format(coins, nums[i]):
                return False
        return True

    def format(self, coins: List[int], target: int) -> bool:
        dp = 1
        for coin in coins:
            dp |= dp << coin
            dp &= (1 << (target + 1)) - 1
        return (dp >> target) & 1 == 1
