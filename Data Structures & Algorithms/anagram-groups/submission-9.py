class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        d={}
        for s in strs:
            sorted_w = "".join(sorted(s))

            if sorted_w in d.keys():
                d[sorted_w].append(s)
            else:
                d[sorted_w] = [s]

        res = list(d.values())


        return res