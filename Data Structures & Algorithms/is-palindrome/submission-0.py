class Solution:
    def isPalindrome(self, s: str) -> bool:
        res = False
        w_str = s.replace(" ", "")
        w_str = re.sub(r'[^a-zA-Z0-9]', '', w_str).lower()
        
        if w_str == w_str[::-1]:
            return True

        return res