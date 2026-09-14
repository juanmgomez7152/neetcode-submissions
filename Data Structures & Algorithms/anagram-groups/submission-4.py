class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        d={}

        for i in range(len(strs)):
            w = "".join(sorted(strs[i]))

            if w in d:
                d[w].append(strs[i])
            else:
                d[w]=[strs[i]] 

        res = list(d.values())

        return res