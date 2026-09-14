class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        d = {}
        for s in strs:
            sorted_strs = "".join(sorted(s))
            if sorted_strs in d:
                d[sorted_strs].append(s)
            else:
                d[sorted_strs] = [s]
        
        res = list(d.values())

        return res