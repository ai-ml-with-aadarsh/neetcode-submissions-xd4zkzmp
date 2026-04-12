class Solution:
    def isPalindrome(self, s: str) -> bool:
        res = False
        w_str = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        
        if w_str == w_str[::-1]:
            return True

        return res