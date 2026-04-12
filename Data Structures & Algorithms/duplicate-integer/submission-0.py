class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        res = False
        
        if len(nums) != len(set(nums)):
            return True

        return res