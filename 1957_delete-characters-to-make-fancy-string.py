# https://leetcode.com/problems/delete-characters-to-make-fancy-string

class Solution:
    def makeFancyString(self, s: str) -> str:
        res = s[0]
        count = 1

        for i in range(1, len(s)):
            current = s[i]

            if current != res[-1]:
                res += current
                count = 1

            elif count < 2:
                res += current
                count += 1
        
        return res
