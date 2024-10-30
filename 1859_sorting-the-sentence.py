# https://leetcode.com/problems/sorting-the-sentence/

class Solution:
    def sortSentence(self, s: str) -> str:
      s = s.split(" ")
      res = [''] * len(s)

      for i in range(len(s)):
        res[int(s[i][-1]) - 1] = s[i][:-1]
      
      return " ".join(res)
