class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}

        for s in strs:
            w = "".join(sorted(s))
            if w in d:
                d[w].append(s)
            else:
                d[w] = [s]
            
        return list(d.values())