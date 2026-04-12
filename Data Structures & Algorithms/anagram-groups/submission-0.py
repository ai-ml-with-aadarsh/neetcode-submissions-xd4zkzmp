class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = list()

        temp = dict()
        for each_str in strs:
            ana_key = "".join(sorted(each_str))
            if ana_key in temp:
                temp[ana_key].append(each_str)
            else:
                temp[ana_key] = [each_str]

        for k, v in temp.items():
            res.append(v)

        return res