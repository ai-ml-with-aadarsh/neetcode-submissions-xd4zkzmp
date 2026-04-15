class Solution:
    def search(self, nums: List[int], target: int) -> int:
        len_nums = len(nums)
        for i in range(len_nums):
            if target == nums[i]:
                return i

        
        return -1
        