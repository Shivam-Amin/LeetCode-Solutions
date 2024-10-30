# https://leetcode.com/problems/minimum-time-to-make-rope-colorful/

class Solution:
    def minCost(self, c: str, neededTime: List[int]) -> int:
      l = res = 0

      for r in range(1, len(c)):
        if c[l] == c[r]:
          if neededTime[l] < neededTime[r]:
            res += neededTime[l]
            l = r
          else:
            res += neededTime[r]
        else:
          l = r

      return res
