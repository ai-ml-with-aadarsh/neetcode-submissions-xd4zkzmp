class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        len_nums = len(nums)
        
        if not len_nums:
            return 0

        if len_nums == 1:
            return 1

        s_nums = sorted(list(set(nums)))
        len_s_nums = len(s_nums)

        if len_s_nums == 2:
            if (s_nums[1] - s_nums[0] in [-1, 1]):
                return 2
            else:
                return 1
        
        
        res = 1
        exc = 0
        mx = max(s_nums)
        reserved = 0
        for i in range(len(s_nums)):
            j = i+1
            if j < len(s_nums):
                # return s_nums
                # [-4, -3, -2, -1, 1, 2, 3, 4, 6, 7, 8, 9]

                if s_nums[j] - s_nums[i] in [-1, 1]:
                    res +=1
                else:
                    if res >= reserved:
                        reserved = res
                        res = 1
                        exc +=1

                # if res == 4:
                #     return ['call here', res, reserved, exc, s_nums[j], s_nums[i]]

        if res < reserved:
            res = reserved

        return res
