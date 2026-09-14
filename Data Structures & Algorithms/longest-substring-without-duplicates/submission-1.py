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
                else:
                    res = max(len(sub),res)
                    sub=""
                l+=1
        # for c in s:
        #     if sub.count(c) == 0:
        #         sub+=c
        #     else:
        #         res = max(len(sub), res)
        #         sub=""
        return res