class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0 
        substring = ""

        for c in s:
            while c in substring:
                substring = substring[1:]
            
            substring = substring + c
            ans = max(ans, len(substring))

        return ans 