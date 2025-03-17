from typing import List

class Solution:
  def findRepeatedDnaSequences(self, s: str) -> List[str]:
    return self.findRepeatedLenN(s, 10)
  def findRepeatedLenN(self, s: str, n: int) -> List[str]:
    seen = set()
    duplicated = set()
    
    for i in range(len(s) - n + 1):
      sub = s[i: i + n]
      if sub in seen:
        duplicated.add(sub)
      else:
        seen.add(sub)
        
    return list(duplicated)
      
solution = Solution()
print(solution.findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"))
    