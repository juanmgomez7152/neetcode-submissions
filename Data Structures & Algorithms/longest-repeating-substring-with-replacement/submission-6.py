class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res,l_ptr=0,0

        for r_ptr in range(len(s)):
            count[s[r_ptr]]= 1+ count.get(s[r_ptr],0)
            while r_ptr-l_ptr+1 - max(count.values()) > k :#length of string - max count > k
                count[s[l_ptr]] -= 1# move remove the left ptr value count
                l_ptr+=1 #move the left pointer 1 spot 
                
            res = max(res, r_ptr-l_ptr+1) #max(length of string, prev_max)

        return res