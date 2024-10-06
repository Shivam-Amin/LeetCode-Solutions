# https://leetcode.com/problems/truncate-sentence/

class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        l = s.split(" ")[:k]

        return " ".join(l)

        # first approch:
        # res = ""
        # for word in l:
        #   res = res + word + " "
        
        # return res[:-1]
