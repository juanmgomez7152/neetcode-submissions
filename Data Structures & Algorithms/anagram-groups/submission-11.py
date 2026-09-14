class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d={}
        for s in strs:
            sorted_word = "".join(sorted(s))
            if sorted_word in d.keys():
                d[sorted_word].append(s)
            else:
                d[sorted_word] = [s]
        
        return list(d.values())
        
            