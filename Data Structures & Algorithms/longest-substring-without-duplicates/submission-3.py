class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2:
            return len(s)
        res = 0
        sub = ""
        for i,a in enumerate(s):
            l=i
            while l < len(s):
                if sub.count(s[l]) == 0:
                    sub+=s[l]
                    l+=1
                else:
                    res = max(len(sub),res)
                    sub=""
                    break
        return res