class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        res = False
        
        if sorted(s) == sorted(t):
            return True

        return res