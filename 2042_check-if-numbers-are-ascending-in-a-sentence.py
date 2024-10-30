# https://leetcode.com/problems/check-if-numbers-are-ascending-in-a-sentence/

class Solution:
    def areNumbersAscending(self, s: str) -> bool:
      s = s.split(" ")

      min_num = -1
      for i in s:
        if i.isdigit():
          if int(i) > min_num:
            min_num = int(i)
          else:
            return False
      
      return True
