class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = list()
        target = k

        temp = dict.fromkeys(set(nums),0)
        for i in temp:
            for j in nums:
                if i == j:
                    temp[i] += 1

        temp2 = {k: v for k, v in sorted(temp.items(), key=lambda item: item[1], reverse=True)}
        
        for i in range(target):
            res.append(list(temp2.keys())[i])

        return res