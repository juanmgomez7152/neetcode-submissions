class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res=0
        temp =""
        if len(s)==0 or len(s) == 1:
            return len(s)
        
        for c in s:
            while c in temp:
                temp = temp[1:]
            temp+=c
            res = max(len(temp),res)
        
        res = max(len(temp), res)
        return res