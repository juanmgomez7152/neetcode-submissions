class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        candidate = ""
        ans = 0
        for c in s:
            while candidate.find(c)>=0:
                candidate = candidate[1:]
            candidate+=c
            ans = max(ans,len(candidate))

        return ans