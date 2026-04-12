class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = list()

        for i in range(len(nums)):
            temp = 1
            for j  in range(len(nums)):
                if i!=j:
                    temp *= nums[j]
            
            res.append(temp)

        return res