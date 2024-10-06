class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        s = sentence.split(" ")

        # check for first and last word's ch. match,
        # it'll work if senetece is of one word
        if s[0][0] != s[len(s)-1][-1]:
          return False

        # loop from first word and check conditions
        i = 0
        while i < len(s)-1 and s[i][-1] == s[i+1][0]:
          i += 1
        
        return i >= len(s)-1
