class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        nums.sort()
        n = len(nums)
        
        for i in range(n - 2):
            if nums[i] > 0:
                break

            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            for j in range(i + 1, n - 1):
                if nums[i] + nums[j] > 0 and nums[j] > 0:
                    break
                
                for k in range(j + 1, n):
                    t_sum = nums[i] + nums[j] + nums[k]
                    if t_sum == 0:
                        res.add((nums[i], nums[j], nums[k]))
                    elif t_sum > 0: 
                        break

        return [list(t) for t in res]