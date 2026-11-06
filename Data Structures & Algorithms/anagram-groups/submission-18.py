class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        anagram_dict = {}

        for word in strs:
            srtd_wrd="".join(sorted(word))
            
            if srtd_wrd in anagram_dict:
                anagram_dict[srtd_wrd].append(word)
            else:
                anagram_dict[srtd_wrd] = [word]
   
        res = list(anagram_dict.values())
 
        return res