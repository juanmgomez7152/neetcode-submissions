class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_words = {}
        for s in strs:
            srted = "".join(sorted(s))
            if srted in sorted_words.keys():
                sorted_words[srted].append(s)
            else:
                sorted_words[srted] = [s]
        return (list(sorted_words.values()))