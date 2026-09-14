class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = collections.defaultdict(list)
        res = []
        for s in strs:
            sorted_word = "".join(sorted(s))
            d[sorted_word].append(s)
        
        # print(list(d.values()))

        return list(d.values())