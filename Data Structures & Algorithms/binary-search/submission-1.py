class Solution:
    def search(self, nums: List[int], target: int) -> int:
        len_nums = len(nums)
        
        if target == nums[-1]:
            return len_nums - 1
        elif target == nums[0]:
            return 0


        for i in range(len_nums):
            if target == nums[i]:
                return i

        return -1