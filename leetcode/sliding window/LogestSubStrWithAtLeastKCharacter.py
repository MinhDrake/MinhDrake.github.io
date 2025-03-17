import collections
from typing import Counter


class Solution:
    # Nếu 1 kí tự < k lần, thì mọi chuỗi con chứa
    # kí tự này đều không thoả mãn
    def longestSubstring(self, s: str, k: int) -> int:
        if len(s) == 0 or k > len(s):
            return 0
        counter = Counter(s)
        firstSub, secondSub, is_exist = "", "", False
        for i, c in enumerate(s):
            if counter[c] < k:
                firstSub = self.longestSubstring(s[:i], k)
                secondSub = self.longestSubstring(s[i+1:], k)
                is_exist = True
                break

        if is_exist == False:
            return len(s)

        return max(firstSub, secondSub)


solution = Solution()
print(solution.longestSubstring("ababbc", 2))
