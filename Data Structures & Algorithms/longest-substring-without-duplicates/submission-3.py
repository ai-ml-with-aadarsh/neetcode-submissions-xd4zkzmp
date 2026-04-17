class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        long_sub_str = 0
        temp = ''

        for i in range(len(s)):
            while s[i] in temp:
                temp = temp[1:]

            temp = temp + s[i]
            long_sub_str = max(long_sub_str, len(temp))

        return long_sub_str