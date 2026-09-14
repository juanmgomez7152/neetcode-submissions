class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res=0
        
        for i in range(len(s)):
            j=i
            d={}
            
            while j < len(s):
                if s[j] in d:
                    res = max(res,len(d))
                    break
                d[s[j]]=1

                j+=1
            res = max(res,len(d))

        return res