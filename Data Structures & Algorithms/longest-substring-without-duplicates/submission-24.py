class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0 
        temp = ""
        if len(s)==0 or len(s) == 1:
            return len(s)

        for c in s:
            while c in temp:
                temp = temp[1:]
            temp+=c
            ans = max(len(temp),ans)
        
        ans = max(len(temp),ans)
        return ans