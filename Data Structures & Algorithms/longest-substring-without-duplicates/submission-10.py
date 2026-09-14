class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        res = 0 
        for i in range(len(s)):
            j=i
            candidate = []
            c=0
            while j <len(s):
                if s[j] in candidate:
                    res = max(res,c)
                    break
                c+=1
                candidate.append(s[j])
                j+=1
            res = max(res,c)

        return res