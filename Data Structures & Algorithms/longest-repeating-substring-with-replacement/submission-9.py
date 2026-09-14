class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char_c= {}
        l_ptr = 0
        res = 0

        for r_ptr in range(len(s)):
            char_c[s[r_ptr]] = 1+char_c.get(s[r_ptr],0)
            while r_ptr-l_ptr+1 - max(char_c.values()) > k:
                char_c[s[l_ptr]] -= 1
                l_ptr+=1
                
            res = max(res, r_ptr-l_ptr+1)

        return res