class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        subs=""
        for i in range(len(s)):
            j=i
            while j<len(s):
                if subs.count(s[j]) == 0:
                    subs+=s[j]
                else:
                    res = max(res,len(subs))
                    subs = ""
                    break
                j+=1
        res = max(res,len(subs))
        return res